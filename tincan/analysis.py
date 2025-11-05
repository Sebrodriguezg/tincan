from joblib import Parallel, delayed
import numpy as np
import pandas as pd
from tincan.simulation import run_simulation

def calcular_area_espectral_energia(u, dt):
    """Calcula el área espectral de la energía cinética (proporcional a la velocidad al cuadrado)."""
    v = np.gradient(u, dt)
    V = np.fft.rfft(v)
    freqs = np.fft.rfftfreq(len(v), d=dt)
    S_v = np.abs(V)**2
    area = np.trapz(S_v, freqs)
    return area, freqs, S_v

def simular_y_medir_ganancia(nombre, props, L0, T_axial, A0, T_total, Nx, CFL, modo_barrido):
    """Ejecuta una simulación completa y calcula la ganancia espectral."""
    res = run_simulation(
        cuerda=props, L0=L0, T_axial=T_axial, A0=A0,
        T_total=T_total, Nx=Nx, CFL=CFL, modo_barrido=modo_barrido
    )

    uL = res['uL_series']
    u0 = res['source_signal']

    area_L, freqs, S_L = calcular_area_espectral_energia(uL, res['dt'])
    area_0, _, S_0 = calcular_area_espectral_energia(u0, res['dt'])

    ganancia = area_L / area_0 if area_0 > 0 else 0.0

    return {
        "nombre": nombre,
        "L": res["L"],
        "c": res["c"],
        "area_entrada": area_0,
        "area_salida": area_L,
        "ganancia_espectral": ganancia,
        "freqs": freqs,
        "S_L": S_L,
        "L0": L0,
        "T_axial": T_axial
    }

def ejecutar_barrido_parametros(longitudes_iniciales, tensiones, cuerdas, A0, T_total, Nx, CFL, modo_barrido):
    tareas = [
        (nombre, props, L0, T)
        for L0 in longitudes_iniciales
        for T in tensiones
        for nombre, props in cuerdas.items()
    ]

    print(f"Ejecutando {len(tareas)} simulaciones en paralelo...")

    resultados = Parallel(n_jobs=-1, backend="loky")(
        delayed(simular_y_medir_ganancia)(
            nombre, props, L0, T, A0, T_total, Nx, CFL, modo_barrido
        )
        for nombre, props, L0, T in tareas
    )

    df = pd.DataFrame(resultados)
    df = df.dropna(subset=["ganancia_espectral"])

    ranking = (
        df.loc[df.groupby("L0")["ganancia_espectral"].idxmax(), ["L0", "nombre", "T_axial", "ganancia_espectral"]]
        .sort_values("L0")
        .reset_index(drop=True)
    )

    return df, ranking
