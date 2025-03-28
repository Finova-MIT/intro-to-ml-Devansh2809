import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)  
y = np.sin(x)  

plt.plot(x, y, label="Sin(x) Wave",  linewidth=2)

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Chart")
plt.legend()
plt.show()

for i in range(10):
    x = np.random.rand(50) * 10  # Random x values between 0 and 10
    y = np.random.rand(50) * 100  # Random y values between 0 and 100

plt.scatter(x, y, marker="o", label="Data Points")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")

plt.legend()
plt.show()
