import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({"Under 12": [0.3871, 0.1347],
                   "12": [0.4471, 0.4655],
                   "Over 12": [0.1658, 0.3998]},
                   index=["Smoked", "Non Smoked"])

ax = df.plot(kind="bar", stacked=True, color=["red", "yellow", "blue"])

for rect in ax.patches:
    # Find where everything is located
    height = rect.get_height()
    width = rect.get_width()
    x = rect.get_x()
    y = rect.get_y()
    
    # The height of the bar is the data value and can be used as the label
    label_text = f'{height:.4f}'  # f'{height:.2f}' to format decimal values
    
    # ax.text(x, y, text)
    label_x = x + width / 2
    label_y = y + height / 2

    # plot only when height is greater than specified value
    if height > 0:
        ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=8)

plt.xlabel("Smoking status")
plt.xticks(rotation=0)
plt.ylabel("Percent in each group")

plt.title("Percentage of each education level for both smokers and nonsmokers")

plt.show()