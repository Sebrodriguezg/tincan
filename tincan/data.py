# Simulación de ondas longitudinales en cilindros con diferentes propiedades
# --------------------------------------------------------------------------
# En este bloque se define un diccionario
# con los parámetros físicos de distintos materiales (cuerdas o cilindros).
# Cada entrada contendrá:
#   - Módulo de Young (E)
#   - Densidad volumétrica (rho0)
#   - Diámetro del cilindro (D)
#   - Coeficiente de amortiguamiento (alpha)

# Diccionario con materiales a simular
# Las unidades son: E [Pa], rho0 [kg/m³], D [m]

cuerdas = {
    'cuerda1': {
        'E': 5.96e06,   # Pa
        'rho0': 444.839,  # kg/m³
        'D': 3.05e-3,     # m (1 mm)
        'alpha': 0.001 # amortiguamiento leve
    },
    'cuerda2': {
        'E': 1.67e07,
        'rho0': 529.390,
        'D': 2.03e-3,
        'alpha': 0.001
    },
    'cuerda3': {
        'E': 5.12e08,
        'rho0': 537.373,
        'D': 0.39e-3,
        'alpha': 0.001
    },
    'cuerda4': {
        'E': 8.0e7,
        'rho0': 320.495,
        'D': 0.53e-3,
        'alpha': 0.002
    },
    'cuerda5': {
        'E': 9.36e08,
        'rho0': 994.719,
        'D': 0.32e-3,
        'alpha': 0.001
    },
}
