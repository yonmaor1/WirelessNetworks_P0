import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Plot signal strength and data rate.')
parser.add_argument('-s', '--separate', action='store_true', help='Plot each data frame separately')
parser.add_argument('--los-nlos', action='store_true', help='Plot LOS and NLOS (cardboard) experiments on the same plot')
args = parser.parse_args()

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

if args.los_nlos:
    los_nlos_dfs = [los_df, nlos_cardboard_df]
    los_nlos_labels = ['LOS', 'NLOS (cardboard)']
    
    # plot signal strength
    plt.figure(figsize=(10, 6))
    for df, label in zip(los_nlos_dfs, los_nlos_labels):
        # raw data
        plt.plot(df['Distance'], df['Signal strength (dBm)'], label=label, alpha=0.1)
        # moving averages
        df['Moving Average'] = df['Signal strength (dBm)'].rolling(window=100).mean()
        plt.plot(df['Distance'], df['Moving Average'], label=f'{label} Moving Average', linestyle='--')

    plt.xlabel('Distance (m)')
    plt.ylabel('Signal Strength (dBm)')
    plt.title('Signal Strength vs Distance (LOS and NLOS (cardboard))')
    plt.legend()
    plt.grid(True)
    plt.show()

    # plot data rate
    plt.figure(figsize=(10, 6))
    for df, label in zip(los_nlos_dfs, los_nlos_labels):
        # raw data
        plt.plot(df['Distance'], df['Data rate (Mb/s)'], label=label, alpha=0.1)
        # moving averages
        df['Data Rate Moving Average'] = df['Data rate (Mb/s)'].rolling(window=100).mean()
        plt.plot(df['Distance'], df['Data Rate Moving Average'], label=f'{label} Data Rate Moving Average', linestyle='--')

    plt.xlabel('Distance (m)')
    plt.ylabel('Data Rate (Mb/s)')
    plt.title('Data Rate vs Distance (LOS and NLOS (cardboard))')
    plt.legend()
    plt.grid(True)
    plt.show()
elif args.separate:
    for df, label in zip(dfs, df_labels):
        # plot signal strength
        plt.figure(figsize=(10, 6))
        # raw data
        plt.plot(df['Distance'], df['Signal strength (dBm)'], label=label, alpha=0.1)
        # moving averages
        df['Moving Average'] = df['Signal strength (dBm)'].rolling(window=100).mean()
        plt.plot(df['Distance'], df['Moving Average'], label=f'{label} Moving Average', linestyle='--')

        plt.xlabel('Distance (m)')
        plt.ylabel('Signal Strength (dBm)')
        plt.title(f'Signal Strength vs Distance ({label})')
        plt.legend()
        plt.grid(True)
        plt.show()

        # plot data rate
        plt.figure(figsize=(10, 6))
        # raw data
        plt.plot(df['Distance'], df['Data rate (Mb/s)'], label=label, alpha=0.1)
        # moving averages
        df['Data Rate Moving Average'] = df['Data rate (Mb/s)'].rolling(window=100).mean()
        plt.plot(df['Distance'], df['Data Rate Moving Average'], label=f'{label} Data Rate Moving Average', linestyle='--')

        plt.xlabel('Distance (m)')
        plt.ylabel('Data Rate (Mb/s)')
        plt.title(f'Data Rate vs Distance ({label})')
        plt.legend()
        plt.grid(True)
        plt.show()
else:
    # plot signal strength
    plt.figure(figsize=(10, 6))
    for df, label in zip(dfs, df_labels):

        if label == 'LOS':
            continue
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
        if label == 'LOS':
            continue
        
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