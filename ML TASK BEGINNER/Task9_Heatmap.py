import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Student Performance.csv')

# Select only the numerical columns
numerical_columns = ['math score', 'reading score', 'writing score']
numerical_data = df[numerical_columns]

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap of Student Performance Scores')
plt.show()
