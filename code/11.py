import numpy as np
import matplotlib.pyplot as plt

data = {"Under 18": 43, "18-19": 44, "20-24": 34, "25-29": 23, "30-34": 21, "Over 34": 26}

x = list(data.keys())
y = list(data.values())

fig, ax = plt.subplots(figsize=(9, 9))
ax.bar(x, y, color ="blue", width = 0.4)
plt.bar_label(ax.containers[0], label_type='edge', color='red', rotation=90, fontsize=15, padding=10)
 
plt.xlabel("Age group")
plt.ylabel("Percentage of mothers who smokes")
plt.title("Bar graph of age and smoking status")
plt.grid()
plt.show()

age = np.array([9, 18.5, 22, 27, 32, 37])
percent = np.array([43, 44, 34, 23, 21, 26])

var_age = np.mean((age - np.mean(age))**2)
var_percent = np.mean((percent - np.mean(percent))**2)
cov = np.mean((age - np.mean(age))*(percent - np.mean(percent)))
print(cov)
cor = cov / np.sqrt(var_age * var_percent)
print(cor)

import scipy.stats as stats
import numpy as np
  
# Make a 5 x 4 table
dataset = np.array([[4, 13, 17, 11], [4, 6, 9, 12],
                    [2, 7, 4, 2], [5, 13, 10, 12],
                    [5, 6, 14, 12]])
  
# Finding Chi-squared test statistic, 
# sample size, and minimum of rows and
# columns
X2 = stats.chi2_contingency(dataset, correction=False)[0]
N = np.sum(dataset)
minimum_dimension = min(dataset.shape)-1
  
# Calculate Cramer's V
result = np.sqrt((X2/N) / minimum_dimension)
  
# Print the result
print(result)