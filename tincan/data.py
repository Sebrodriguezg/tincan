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
    'acero': {
        'E': 2.1e11,   # Pa
        'rho0': 7850,  # kg/m³
        'D': 1e-3,     # m (1 mm)
        'alpha': 0.001 # amortiguamiento leve
    },
    'aluminio': {
        'E': 6.9e10,
        'rho0': 2700,
        'D': 1e-3,
        'alpha': 0.001
    },
    'cobre': {
        'E': 1.1e11,
        'rho0': 8960,
        'D': 1e-3,
        'alpha': 0.001
    },
    'nylon': {
        'E': 3.0e9,
        'rho0': 1150,
        'D': 1e-3,
        'alpha': 0.002
    }
}
