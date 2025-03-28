import pandas as pd
import matplotlib.pyplot as plt


df_student = pd.read_csv("Student Performance.csv")

# Group data by gender and calculate average scores
gender_group = df_student.groupby("gender")[["math score", "reading score", "writing score"]].mean()

# Plot grouped data by gender
plt.figure(figsize=(6, 5))
gender_group.plot(kind="bar", ax=plt.gca())
plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")

plt.show()
