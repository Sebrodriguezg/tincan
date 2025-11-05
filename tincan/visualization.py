import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_summary(res, material, modo_barrido):
    """Genera y muestra las gráficas principales de la simulación."""

    # Figura 1: mapa espacio-temporal del desplazamiento
    plt.figure(figsize=(8, 4))
    plt.imshow(
        res['snapshots'].T,
        extent=[0, res['t'][-1], 0, res['L']],
        origin='lower',
        aspect='auto',
        cmap='RdBu_r'
    )
    plt.colorbar(label='Desplazamiento [m]')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Posición x [m]')
    plt.title(f'Onda en {material.capitalize()} (barrido {modo_barrido})')
    plt.tight_layout()
    plt.show()

    # Figura 2: señal en el extremo libre (x = L)
    plt.figure(figsize=(7, 3))
    plt.plot(res['t'], res['uL_series'], lw=0.8)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Desplazamiento extremo libre [m]')
    plt.title('Respuesta temporal en el extremo libre')
    plt.tight_layout()
    plt.show()

    # Figura 3: espectro (FFT) del extremo libre
    U = np.fft.rfft(res['uL_series'])
    freqs = np.fft.rfftfreq(len(res['uL_series']), d=res['dt'])

    plt.figure(figsize=(7, 3))
    plt.plot(freqs, np.abs(U), lw=0.8)
    plt.xlim(0, 20000)
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Amplitud |U(f)|')
    plt.title('Espectro del extremo libre')
    plt.tight_layout()
    plt.show()

def plot_ganancia_comparison(resultados):
    """Visualización: espectros normalizados"""
    plt.figure(figsize=(8, 4))
    for r in resultados:
        # Normalizar el espectro para la comparación visual
        S_L_normalized = r["S_L"] / np.max(r["S_L"]) if np.max(r["S_L"]) > 0 else r["S_L"]
        plt.plot(r["freqs"], S_L_normalized, label=f"{r['nombre']} (η={r['ganancia_espectral']:.3f})")

    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Potencia relativa [a.u.]")
    plt.title("Espectros en el extremo libre (normalizados)")
    plt.legend()
    plt.xlim(0, 20000)
    plt.tight_layout()
    plt.show()
