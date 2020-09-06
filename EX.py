import numpy as np
import matplotlib.pyplot as plt

for quantity , suffix in [(1000, "train"), (200, "test")]:
    samples = np.random.multivariate_normal([-2, -2], [[1, 0], [0, 1]], quantity)
    plt.plot(samples[:, 0], samples[:, 1], '.', label="bad ones" + suffix)
    bad_ones = np.column_stack((np.zeros(quantity), samples))

    samples = np.random.multivariate_normal([1, 1], [[1, 0.5], [0.5, 1]], quantity)
    plt.plot(samples[:, 0], samples[:, 1], '.', label="good ones" + suffix)
    good_ones = np.column_stack((np.ones(quantity), samples))

    sample = np.row_stack((bad_ones, good_ones))
    np.savetxt("data/the_good_and_the_bad_ones_" + suffix + ".txt", sample, fmt="%1d %4.2f %4.2f")

plt.legend()
plt.plot()