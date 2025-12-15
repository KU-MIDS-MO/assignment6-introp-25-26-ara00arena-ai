import numpy as np
def get_random_subset_of_naturals_up_to_20():
    universe = np.arange(1,21)
    coin_flips=np.random.randint(0, 2, size=20)
    mask=(coin_flips==1)
    return universe[mask]
