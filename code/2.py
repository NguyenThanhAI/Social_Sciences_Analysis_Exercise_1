import numpy as np
import matplotlib.pyplot as plt


lower = np.array([0, 5, 10, 15])
upper = np.array([5, 10, 15, 60])

percent = np.array([16, 25, 14, 45])

plt.bar(lower, percent/(upper-lower), width=upper - lower, ec="k", align="edge")
plt.xticks(lower.tolist() + [upper.tolist()[-1]], rotation=45)
plt.xlabel("Number of cigarettes (per day)")
plt.ylabel("Percent per cigarette")
plt.grid()
plt.show()