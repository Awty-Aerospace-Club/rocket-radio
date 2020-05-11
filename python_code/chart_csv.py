import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['altitude', 'accelX', 'accelY', 'accelZ', 'accelZ', 'gyroX', 'gyroY', 'gyroZ']
df = pd.read_csv("output.csv", names=headers)
print(df)

for i in headers:
    plt.plot(df['time'], df[i])