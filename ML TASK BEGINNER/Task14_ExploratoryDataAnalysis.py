import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Titanic.csv")

# Display basic information
print("Dataset Info:\n", df.info())

# Display summary statistics
print("\nSummary Statistics:\n", df.describe())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Countplot of Survived
plt.figure(figsize=(6, 4))
sns.countplot(x="Survived", data=df, palette="coolwarm")
plt.title("Survival Count")
plt.show()

# Countplot of Survived by Gender
plt.figure(figsize=(6, 4))
sns.countplot(x="Survived", hue="Sex", data=df, palette="viridis")
plt.title("Survival by Gender")
plt.show()

# Boxplot for Age Distribution by Survival
plt.figure(figsize=(6, 4))
sns.boxplot(x="Survived", y="Age", data=df, palette="pastel")
plt.title("Age Distribution by Survival")
plt.show()

# Heatmap of missing values
plt.figure(figsize=(8, 5))
sns.heatmap(df.isnull(), cmap="viridis", cbar=False)
plt.title("Missing Values Heatmap")
plt.show()
