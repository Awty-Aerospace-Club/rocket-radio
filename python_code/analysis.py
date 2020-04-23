""" This file's purpose is to convert csv produced by receiver.py into database fields, which will be inserted into a MySQL db, that can be addressed by a react-graphing app...
soon to come"""
import csv, MySQLdb

db = mysql.connector.connect(
    host=config[host],
    user=config[user],
    database="RocketRadio"
)

with open('databas-cfg.yaml') as cfg:
    config = yaml.load(cfg, Loader=yaml.FullLoader)

cursor = db.cursor()
data = csv.reader(file("output.csv"))

for row in data:
    cursor.execute('INSERT INTO SensorData(time, altitude, accelX, accelY, accelZ, gyroX, gyroY, gyroZ)' \
    'VALUES("%s", "%s", "%s")', row)






