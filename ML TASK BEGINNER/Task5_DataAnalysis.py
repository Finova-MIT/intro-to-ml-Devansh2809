import pandas as pd
import numpy as np

df = pd.read_csv("Student Performance.csv")

print(df)

# Identify numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns

mean_values = df[numerical_cols].mean()
median_values = df[numerical_cols].median()
standard_deviation=df[numerical_cols].std()


print("\nMean:\n", mean_values)
print("\nMedian:\n", median_values)
print("\nStandard Deviation:\n", standard_deviation)
