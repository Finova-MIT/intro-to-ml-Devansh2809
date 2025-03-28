import pandas as pd
import matplotlib.pyplot as plt


df_student = pd.read_csv("Student Performance.csv")

# Group data by gender and calculate average scores
gender_group = df_student.groupby("gender")[["math score", "reading score", "writing score"]].mean()

# Create a figure with multiple subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Line plot
gender_group.plot(kind="line", marker="o",  ax=axes[0])
axes[0].set_title("Line Plot: Average Scores by Gender")
axes[0].set_ylabel("Average Score")

# Bar plot
gender_group.plot(kind="bar", ax=axes[1])
axes[1].set_title("Bar Plot: Average Scores by Gender")
axes[1].set_ylabel("Average Score")

# Scatter plot
for subject in ["math score", "reading score", "writing score"]:
    axes[2].scatter(df_student["gender"], df_student[subject], label=subject)
axes[2].set_title("Scatter Plot: Scores by Gender")
axes[2].set_ylabel("Score")
axes[2].legend()

plt.tight_layout()
plt.show()
