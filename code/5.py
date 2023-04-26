import numpy as np 
import pylab 
import scipy.stats as stats
import matplotlib.pyplot as plt

measurements = np.array([252, 262, 267, 270, 272, 274, 276, 277, 278, 280, 281, 283, 284, 286, 288, 290, 292, 296, 302])
quantiles = np.arange(1, measurements.shape[0] + 1) / (measurements.shape[0] + 1)
print(quantiles)
#plt.scatter(quantiles, measurements)
#plt.grid()
#plt.show()
stats.probplot(measurements, dist="uniform", plot=pylab)
pylab.title("Quantile plot")
pylab.xlabel("Quantiles of uniform")
pylab.ylabel("Gestational age")
pylab.grid()
pylab.show()

plt.hist(measurements, np.arange(250,305, 5)) 
plt.title("histogram") 
plt.show()