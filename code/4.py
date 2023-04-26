import numpy as np
import matplotlib.pyplot as plt

def normal(x: float, mu: float, sigma: float) -> float:
    return (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))


x = np.linspace(90, 270, num=1000)

normal_vec = np.vectorize(normal)

prob_normal = normal_vec(x, 180, 80/3)

plt.plot(x, prob_normal, "b")
#plt.xlabel("Chiều cao (inches)")
plt.xlabel("Cân nặng (pounds)")
plt.grid()
plt.show()