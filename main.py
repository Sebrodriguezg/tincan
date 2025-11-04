import numpy as np
from tincan.data import cuerdas
from tincan.simulation import run_simulation
from tincan.analysis import ejecutar_barrido_parametros
from tincan.visualization import plot_simulation_summary, plot_ganancia_comparison

def main():
    # Parámetros para una simulación individual
    material = 'acero'
    L0 = 0.01
    T_axial = 200.0
    A0 = 1e-6
    T_total = 0.08
    Nx = 160
    CFL = 0.9
    modo_barrido = 'linear'

    # Ejecutar una simulación individual
    res = run_simulation(
        cuerda=cuerdas[material],
        L0=L0,
        T_axial=T_axial,
        A0=A0,
        T_total=T_total,
        Nx=Nx,
        CFL=CFL,
        modo_barrido=modo_barrido
    )

    # Visualizar resultados de la simulación individual
    print("=== Resumen de la simulación individual ===")
    print(f"Material: {material}")
    print(f"Longitud final L = {res['L']:.3f} m")
    print(f"Velocidad de onda c = {res['c']:.1f} m/s")
    print(f"Δx = {res['dx']:.4e} m, Δt = {res['dt']:.4e} s")
    print(f"Nx = {res['Nx']}, Nt = {res['Nt']}")

    plot_simulation_summary(res, material, modo_barrido)

    # Parámetros para el barrido de parámetros
    longitudes_iniciales = [1, 5, 10, 25, 50, 75, 100]
    tensiones = np.linspace(1, 20, 20)

    # Ejecutar barrido de parámetros
    df_completo, df_ranking = ejecutar_barrido_parametros(
        longitudes_iniciales, tensiones, cuerdas, A0, T_total, Nx, CFL, modo_barrido
    )

    # Visualizar comparación de eficiencias
    resultados_filtrados = [grupo.iloc[0].to_dict() for nombre, grupo in df_completo.groupby('nombre')]
    plot_ganancia_comparison(resultados_filtrados)

    # Imprimir ranking
    print("\\n=== Mejor material y tensión para cada longitud inicial ===")
    print(df_ranking.to_string(index=False))

    # Guardar resultados en CSV
    df_completo.to_csv("results/resultados_completos.csv", index=False)
    df_ranking.to_csv("results/ranking_por_longitud_inicial.csv", index=False)

    print("\\nResultados guardados en la carpeta 'results'")

if __name__ == "__main__":
    main()
