import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 2
fig, axes = plt.subplots(2, 2, figsize=(6, 6))
n_points = [50, 500, 5000, 50000]
for i, ax in enumerate(axes.flatten()):
    x = np.random.normal(a, b, n_points[i])
    ax.hist(x, bins=40, density=True)
    ax.set_title(f"n = {n_points[i]}")
plt.show()