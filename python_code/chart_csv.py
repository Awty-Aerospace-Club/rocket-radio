import pandas as pd
import csv
import matplotlib.pyplot as plt
headers = ['altitude', 'accelX', 'accelY', 'accelZ', 'gyroX', 'gyroY', 'gyroZ']
df = pd.read_csv("output.csv", names=headers)
print(df)

for i in headers:
    plt.plot(df['time'], df[i], label=i)

plt.legend(loc="upper left")
plt.show()
