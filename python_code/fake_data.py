from csvquery import *
from random import uniform

fields = [
    "time",
    "altitude",
    "accelX",
    "accelY",
    "accelZ",
    "gyroX",
    "gyroY",
    "gyroZ",
]

data = ",".join(fields)

o = 120
v = 40
g = -4.9
period = 5

accelXma = []
accelZma = []
gyroXma = []
gyroYma = []
gyroZma = []

def moving_average(l):
    l.append(uniform(-0.2, 0.2))
    if len(l) > period: l.pop(0)
    return sum(l) / len(l)

for j in range(10000):
    i = j / 50
    time = i + uniform(0, 0.01)
    t = i - o
    altitude = max(0, g*t*t + v * t)
    accelY = v if round(t) == 0 else (g if altitude > 0 else 0)
    accelX = moving_average(accelXma) if altitude > 0 else 0
    accelZ = moving_average(accelZma) if altitude > 0 else 0
    gyroX = moving_average(gyroXma) if altitude > 0 else 0
    gyroY = moving_average(gyroYma) if altitude > 0 else 0
    gyroZ = moving_average(gyroZma) if altitude > 0 else 0

    column = [
        time,
        altitude,
        accelX,
        accelY,
        accelZ,
        gyroX,
        gyroY,
        gyroZ
    ]

    column = [str(round(x, 5)) for x in column]
    data += "\n" + ",".join(column)

with open("../csv/fake_data.csv", "w+", newline="") as file:
    print(data, file=file)

dataset = open_csv("fake_data.csv")
dataset.print_table()