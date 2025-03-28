import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Electric_Production.csv')

# Convert the 'DATE' column to datetime format
data['DATE'] = pd.to_datetime(data['DATE'])

# Set the 'DATE' column as the index
data.set_index('DATE', inplace=True)

# Plot the time series
data.plot(figsize=(12, 6), legend=False)
plt.title('Electric Production Time Series')
plt.xlabel('Date')
plt.ylabel('Electric Production ')
plt.grid()
plt.show()
