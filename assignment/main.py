import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("C:\Users\Administrator\.vscode-cli\Gao-Lan-pfad\assignment/daily_HKA_RF_2024.csv")

# Replace 'Trace' with a small value for visualization
data['數值/Value'] = data['數值/Value'].replace('Trace', 0.05).astype(float)

# Create a Date column for easier plotting
data['Date'] = pd.to_datetime(data[['年/Year', '月/Month', '日/Day']])

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['數值/Value'], label='Rainfall (mm)', color='b')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.title('Daily Rainfall at Hong Kong International Airport (2024)')
plt.grid(True)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
