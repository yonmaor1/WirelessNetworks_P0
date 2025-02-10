import pandas as pd

import matplotlib.pyplot as plt

# Read the CSV files
los_df = pd.read_csv('data/los.csv')
nlos_df = pd.read_csv('data/nlos.csv')

los_df['Signal strength (dBm)'] = los_df['Signal strength (dBm)'].str.replace('dBm', '').astype(float)
nlos_df['Signal strength (dBm)'] = nlos_df['Signal strength (dBm)'].str.replace('dBm', '').astype(float)

plt.figure(figsize=(10, 6))
plt.plot(los_df['No.'], los_df['Signal strength (dBm)'], label='LOS', alpha=0.5)
plt.plot(nlos_df['No.'], nlos_df['Signal strength (dBm)'], label='NLOS', alpha=0.5)

plt.xlabel('Number')
plt.ylabel('Signal Strength')
plt.title('Signal Strength vs Number')

# moving averages
los_df['Moving Average'] = los_df['Signal strength (dBm)'].rolling(window=50).mean()
nlos_df['Moving Average'] = nlos_df['Signal strength (dBm)'].rolling(window=50).mean()

plt.plot(los_df['No.'], los_df['Moving Average'], label='LOS Moving Average', linestyle='--')
plt.plot(nlos_df['No.'], nlos_df['Moving Average'], label='NLOS Moving Average', linestyle='--')

plt.legend()

plt.grid(True)
plt.show()