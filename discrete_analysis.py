import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Plot average signal strength with error bars.')
parser.add_argument('-s', '--separate', action='store_true', help='Plot each data frame separately')
args = parser.parse_args()

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

# calculate average and standard deviation for each time interval
def calculate_stats(df, start, end):
    interval_df = df[(df['Time'] >= start) & (df['Time'] < end)]
    avg_signal_strength = interval_df['Signal strength (dBm)'].mean()
    std_signal_strength = interval_df['Signal strength (dBm)'].std()
    return avg_signal_strength, std_signal_strength

time_intervals = np.arange(10, 105, 10)

if args.separate:
    for df, label in zip(dfs, df_labels):
        avg_signal_strengths = []
        std_signal_strengths = []
        for start in time_intervals:
            avg, std = calculate_stats(df, start, start + 5)
            avg_signal_strengths.append(avg)
            std_signal_strengths.append(std)

        plt.figure(figsize=(10, 6))
        plt.errorbar((time_intervals - 10) / 5 * 0.3, avg_signal_strengths, yerr=std_signal_strengths, label=label, fmt='-o')
        plt.xlabel('Distance (m)')
        plt.ylabel('Average Signal Strength (dBm)')
        plt.title(f'Discrete Signal Strength Measurements ({label})')
        plt.legend()
        plt.grid(True)
        plt.show()
else:
    plt.figure(figsize=(10, 6))
    for df, label in zip(dfs, df_labels):
        avg_signal_strengths = []
        std_signal_strengths = []
        for start in time_intervals:
            avg, std = calculate_stats(df, start, start + 5)
            avg_signal_strengths.append(avg)
            std_signal_strengths.append(std)

        plt.errorbar((time_intervals - 10) / 5 * 0.3, avg_signal_strengths, yerr=std_signal_strengths, label=label, fmt='-o')

    plt.xlabel('Distance (m)')
    plt.ylabel('Average Signal Strength (dBm)')
    plt.title('Discrete Signal Strength Measurements')
    plt.legend()
    plt.grid(True)
    plt.show()
