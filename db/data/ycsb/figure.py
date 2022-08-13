# figure.py
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

workload = input('Which workload you\'d like to get? (type in workload letter) ')
csv_path = f'~/Develop/GOODLab-Test/db/data/ycsb/extracted-data/workload-{workload}-report.csv'
fig_filename = f'workload-{workload}.png'
df = pd.read_csv(csv_path)

x = np.array(df['Threads'].to_list())
y1 = np.array(df['MySQL'].to_list())
y2 = np.array(df['RocksDB'].to_list())

plt.plot(x, y1, label='MySQL')
plt.plot(x, y2, label='RocksDB')
plt.legend()

#plt.title(f'Workload {workload.upper()} - MySQL & RocksDB Throughtput')
plt.xlabel('Threads')
plt.ylabel('Throughtput(ops/sec)')

plt.savefig(fig_filename)