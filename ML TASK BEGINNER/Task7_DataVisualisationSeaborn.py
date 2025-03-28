import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = np.random.normal(loc=50, scale=15, size=200)  # Normal distribution

# Create a box plot
plt.figure(figsize=(6, 4))
sns.boxplot(y=data, color="skyblue")
plt.title("Box Plot of Data Distribution")
plt.show()

# Creating a histogram
plt.figure(figsize=(6, 4))
sns.histplot(data, bins=20, kde=False, color="lightcoral")
plt.title("Histogram of Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Creating a density plot
plt.figure(figsize=(6, 4))
sns.kdeplot(data, fill=True, color="green")
plt.title("Density Plot")
plt.xlabel("Value")
plt.show()
