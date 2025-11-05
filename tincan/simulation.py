import numpy as np

def crear_malla(cuerda, L0, T_axial, Nx=160, CFL=0.9):
    E = cuerda['E']
    rho0 = cuerda['rho0']
    D = cuerda['D']
    alpha = cuerda['alpha']
    A = np.pi * (D / 2)**2
    epsilon = T_axial / (E * A)
    L = L0 * (1 + epsilon)
    rho_eff = rho0 * (L0 / L)
    c = np.sqrt(E / rho_eff)
    dx = L / (Nx - 1)
    dt = CFL * dx / c
    return {
        'x': np.linspace(0, L, Nx),
        't_dt': dt,
        'dx': dx,
        'L': L,
        'rho_eff': rho_eff,
        'c': c,
        'alpha': alpha,
        'Nx': Nx
    }

def generar_barrido(t_array, f_min=20.0, f_max=20000.0, modo='linear'):
    tmax = t_array[-1] if len(t_array) > 0 else 1.0
    if modo == 'linear':
        f_t = f_min + (f_max - f_min) * (t_array / tmax)
        phase = 2 * np.pi * (f_min * t_array + (f_max - f_min) / (2 * tmax) * t_array**2)
    elif modo == 'log':
        f_t = f_min * (f_max / f_min)**(t_array / tmax)
        log_ratio = np.log(f_max / f_min)
        phase = 2 * np.pi * (f_min * tmax / log_ratio) * ((f_max / f_min)**(t_array / tmax))
    else:
        raise ValueError("modo debe ser 'linear' o 'log'")
    s = np.sin(phase)
    return f_t, s

def run_simulation(cuerda, L0, T_axial, A0, T_total, Nx, CFL, modo_barrido, snap_limit=200):
    mesh = crear_malla(cuerda, L0, T_axial, Nx=Nx, CFL=CFL)
    dx = mesh['dx']
    dt = mesh['t_dt']
    Nx = mesh['Nx']
    Nt = int(np.ceil(T_total / dt))
    t = np.linspace(0, Nt * dt, Nt)

    f_t, s_t = generar_barrido(t, f_min=20.0, f_max=20000.0, modo=modo_barrido)
    source_signal = A0 * s_t

    u_prev = np.zeros(Nx)
    u = np.zeros(Nx)
    u_next = np.zeros(Nx)
    uL_series = np.zeros(Nt)

    snapshots = []
    snap_interval = max(1, Nt // snap_limit)

    r2 = (mesh['c'] * dt / dx)**2
    damp_coeff = 2 * mesh['alpha'] * dt

    for n in range(Nt):
        u_next[1:-1] = ((2 - damp_coeff) * u[1:-1] -
                        (1 - 0.5 * damp_coeff) * u_prev[1:-1] +
                        r2 * (u[2:] - 2 * u[1:-1] + u[:-2]))

        u_next[0] = source_signal[n]
        u_next[-1] = u_next[-2]

        u_prev, u = u, u_next.copy()
        uL_series[n] = u[-1]

        if n % snap_interval == 0:
            snapshots.append(u.copy())

    return {
        'x': mesh['x'],
        't': t,
        'u_final': u,
        'snapshots': np.array(snapshots),
        'dt': dt,
        'dx': dx,
        'rho_eff': mesh['rho_eff'],
        'c': mesh['c'],
        'L': mesh['L'],
        'Nx': Nx,
        'Nt': Nt,
        'source_signal': source_signal,
        'f_t': f_t,
        'uL_series': uL_series
    }
