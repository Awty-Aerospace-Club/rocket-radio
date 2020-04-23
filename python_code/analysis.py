""" This file's purpose is to convert csv produced by receiver.py into database fields, which will be inserted into a MySQL db, that can be addressed by a react-graphing app...
soon to come"""
import csv, MySQLdb, yaml

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

with open('database-cfg.yaml') as cfg:
    config = yaml.load(cfg, Loader=yaml.FullLoader)

db = MySQLdb.connect(
    host=config['host'],
    user=config['username'],
    database="RocketRadio"
)

cursor = db.cursor()
data = csv.reader(open("output.csv", "r"))

for row in data:
    cursor.execute(f'INSERT INTO SensorData({", ".join(fields)})' \
    'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)

db.commit()
cursor.close()




