import numpy as np
import matplotlib.pyplot as plt
import time

from numba import jit

# TODO # What is @jit and numba?
@jit(nopython=True)
def energy(system, i, j, L):
    """Energy function of spins connected to site (i, j)."""
    """
        E = H = -J sigma_ij SUM(sigma_neighbours)
    """
    return -1. * system[i, j] * (system[np.mod(i - 1, L), j] + system[np.mod(i + 1, L), j] +
                                 system[i, np.mod(j - 1, L)] + system[i, np.mod(j + 1, L)])


@jit
def prepare_system(L):
    """Initialize the system."""
    """
        Numpy array with each element represents one lattice site. Each site can have either +1 or -1 as it's state.
    """
    system = 2 * (0.5 - np.random.randint(0, 2, size=(L, L)))
    return system


@jit(nopython=True)
def measure_energy(system):
    """
        Calculate the total energy of the lattice system.
    """
    L = system.shape[0]
    E = 0
    for i in range(L):
        for j in range(L):
            E += energy(system, i, j, L) / 2. # Why divided by 2? # TODO
    return E


@jit(nopython=True)
def metropolis_loop(system, T, N_sweeps, N_eq, N_flips):
    """ Main loop doing the Metropolis algorithm."""
    # initial energy of the system
    E = measure_energy(system)

    # size of the lattice (number of sites in one dimension)
    L = system.shape[0]
    
    E_list = []
    for step in range(N_sweeps + N_eq):
        # pick one random lattice site coordinate (i,j)
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)

        # calculate the energy difference (after flip - before flip = -2 * before flip)
        dE = -2. * energy(system, i, j, L)

        if dE <= 0.:
            # if energy difference < 0 -> flip the spin
            system[i, j] *= -1
            # new energy of the system after the spin on site (i,j) got flipped
            E += dE
        elif np.exp(-1. / T * dE) > np.random.rand():
            # else (if energy difference > 0), flip the spin on site (i,j) with probability exp(-beta dE/T)
            system[i, j] *= -1
            # new energy of the system after the spin on site (i,j) got flipped
            E += dE

        if step >= N_eq and np.mod(step, N_flips) == 0:
            # measurement
            E_list.append(E)

    # the energy of the system from every measurement
    return np.array(E_list)


if __name__ == "__main__":
    """ Scan through some temperatures """
    # Set parameters here
    L = 4  # Linear system size = lattice size, if L = 4 then there are 4*4 = 16 lattice sites
    N_sweeps = 5000  # Number of steps for the measurements = number of steps to be done after N_eq is reached
    N_eq = 1000  # Number of equilibration steps before the measurements start = wait until this much iteration first before doing the 1st measurement
    N_flips = 10  # Number of steps between measurements = after N_eq is reached, do measurement every N_flips steps
    N_bins = 10  # Number of bins use for the error analysis = do this much time and average the result to get a better estimation for the value (reducing statistical error)

    T_range = np.arange(1.5, 3.1, 0.1) # temperature of the system, [1.5, 3.1) with 0.1 increment

    C_list = []
    system = prepare_system(L)

    # do iteration for every temperature chosen
    for T in T_range:
        C_list_bin = []
        for k in range(N_bins):
            # do the Metropolis algo, get the system energy from every measurement
            Es = metropolis_loop(system, T, N_sweeps, N_eq, N_flips)

            # averaging all the measurement
            mean_E = np.mean(Es)
            mean_E2 = np.mean(Es**2)

            # WHAT IS THIS? # TODO
            # variance^2 / (LT)^2 ?
            C_list_bin.append(1. / T**2. / L**2. * (mean_E2 - mean_E**2))
        
        # average the results from N_bins times of running for statistical reason
        C_list.append([np.mean(C_list_bin), np.std(C_list_bin) / np.sqrt(N_bins)])

        print(T, mean_E, C_list[-1])

    # Plot the results
    C_list = np.array(C_list)
    plt.errorbar(T_range, C_list[:, 0], C_list[:, 1]) # plot (with error bar = std dev) the average energy variance of the system vs temperature

    Tc = 2. / np.log(1. + np.sqrt(2)) # temperature where the critical point happens
    print(Tc)

    plt.axvline(Tc, color='r', linestyle='--')
    plt.xlabel('$T$')
    plt.ylabel('$c$')
    plt.show()
