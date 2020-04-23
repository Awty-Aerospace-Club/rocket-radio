""" This file's purpose is to convert csv produced by receiver.py into database fields, which will be inserted into a MySQL db, that can be addressed by a react-graphing app...
soon to come"""
import csv, MySQLdb, yaml

with open('database-cfg.yaml') as cfg:
    config = yaml.load(cfg, Loader=yaml.FullLoader)

db = MySQLdb.connect(
    host=config['host'],
    user=config['username'],
    database="RocketRadio"
)

cursor = db.cursor()
data = csv.reader(file("output.csv"))

for row in data:
    cursor.execute('INSERT INTO SensorData(time, altitude, accelX, accelY, accelZ, gyroX, gyroY, gyroZ)' \
    'VALUES("%s", "%s", "%s")', row)

db.commit()
cursor.close()




