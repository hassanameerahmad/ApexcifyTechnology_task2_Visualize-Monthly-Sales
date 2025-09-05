# Import libraries

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file

data = pd.read_csv("sales.csv")

# Show the data

print("Monthly Sales Data:")
print(data)

# Plot the sales trend
plt.plot(data["Month"], data["Sales"], marker='o', color='blue')

# Add title and labels
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Save the figure before showing
plt.savefig("monthly_sales_trend.png")

# Show the plot
plt.show()


