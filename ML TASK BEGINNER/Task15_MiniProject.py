import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("food_coded.csv")

# Clean the dataset
data_cleaned = data.dropna(subset=['calories_day', 'weight'])
data_cleaned['weight'] = pd.to_numeric(data_cleaned['weight'], errors='coerce')
data_cleaned = data_cleaned.dropna(subset=['weight'])
data_cleaned['GPA'] = pd.to_numeric(data_cleaned['GPA'], errors='coerce')
data_cleaned['calories_day'] = pd.to_numeric(data_cleaned['calories_day'], errors='coerce')

# Perform analysis
average_gpa = data_cleaned['GPA'].mean()
average_calories_day = data_cleaned['calories_day'].mean()
average_weight_by_gender = data_cleaned.groupby('Gender')['weight'].mean()

# Bar chart for average weight by gender
plt.figure(figsize=(10, 6))
average_weight_by_gender.plot(kind='bar', color=['blue', 'orange'])
plt.title('Average Weight by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Weight')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'], rotation=0)
plt.tight_layout()
plt.show()

# Pie chart for GPA and daily calorie distribution
plt.figure(figsize=(10, 6))
plt.pie([average_gpa, average_calories_day], labels=['Average GPA', 'Average Daily Calories'], 
        autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff'])
plt.title('Distribution of GPA and Daily Calories')
plt.axis('equal')
plt.tight_layout()
plt.show()

