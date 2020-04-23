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
data = csv.reader(open("output.csv", "r"))

fields = data[0]
for row in data[1:]:
    cursor.execute(f'INSERT INTO SensorData({", ".join(fields)})' \
    'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)

db.commit()
cursor.close()




