import pandas as pd

import matplotlib.pyplot as plt

# Read the CSV files
los_df = pd.read_csv('data/yon_los.csv')
nlos_cardboard_df = pd.read_csv('data/yon_nlos_cardboard.csv')
nlos_wood_df = pd.read_csv('data/yon_nlos_wood.csv')
nlos_steel_df = pd.read_csv('data/yon_nlos_steel.csv')

df_labels = ['LOS', 'NLOS (cardboard)', 'NLOS (wood)', 'NLOS (steel)']
dfs = [los_df, nlos_cardboard_df, nlos_wood_df, nlos_steel_df]

# clean the data
for df in dfs:
    df['No.'] = df['No.'].astype(int)
    df['Signal strength (dBm)'] = df['Signal strength (dBm)'].str.replace('dBm', '').astype(float)
    df['Time'] = df['Time'].astype(float)
    df['Distance'] = df['Time'] / 5 * 0.3 # meters
    df['Data rate (Mb/s)'] = df['Data rate (Mb/s)'].astype(float)

    df = df[df['Time'] <= 10]

# plot signal strength
plt.figure(figsize=(10, 6))
for df, label in zip(dfs, df_labels):
    # raw data
    plt.plot(df['Distance'], df['Signal strength (dBm)'], label=label, alpha=0.1)
    # moving averages
    df['Moving Average'] = df['Signal strength (dBm)'].rolling(window=100).mean()
    plt.plot(df['Distance'], df['Moving Average'], label=f'{label} Moving Average', linestyle='--')

plt.xlabel('Distance (m)')
plt.ylabel('Signal Strength (dBm)')
plt.title('Signal Strength vs Distance')
plt.legend()
plt.grid(True)
plt.show()

# plot data rate
plt.figure(figsize=(10, 6))
for df, label in zip(dfs, df_labels):
    # raw data
    plt.plot(df['Distance'], df['Data rate (Mb/s)'], label=label, alpha=0.1)
    # moving averages
    df['Data Rate Moving Average'] = df['Data rate (Mb/s)'].rolling(window=100).mean()
    plt.plot(df['Distance'], df['Data Rate Moving Average'], label=f'{label} Data Rate Moving Average', linestyle='--')

plt.xlabel('Distance (m)')
plt.ylabel('Data Rate (Mb/s)')
plt.title('Data Rate vs Distance')
plt.legend()
plt.grid(True)
plt.show()