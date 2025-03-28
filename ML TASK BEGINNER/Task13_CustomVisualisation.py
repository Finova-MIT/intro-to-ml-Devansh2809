import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_student = pd.read_csv("Student Performance.csv")

# Group data by gender and calculate average scores
gender_group = df_student.groupby("gender")[["math score", "reading score", "writing score"]].mean()

# Set Seaborn style
sns.set_style("whitegrid")

# Create a figure with customized aesthetics
fig, ax = plt.subplots(figsize=(8, 6))

# Define custom colors
custom_colors = ["#ff9999", "#66b3ff", "#99ff99"]

# Bar plot with custom colors and edge color
gender_group.plot(kind="bar", color=custom_colors, edgecolor="black", ax=ax)

# Customize labels and title
ax.set_title("Customized Bar Plot: Average Scores by Gender", fontsize=14, fontweight="bold", color="#333333")
ax.set_ylabel("Average Score", fontsize=12, fontweight="bold")
ax.set_xlabel("Gender", fontsize=12, fontweight="bold")

# Customize legend
ax.legend(title="Subjects", title_fontsize=12, fontsize=10, loc="upper right", frameon=True)

# Rotate x-axis labels
plt.xticks(rotation=0, fontsize=11)

plt.show()
