""" This file's purpose is to convert csv produced by receiver.py into database fields, which will be inserted into a MySQL db, that can be addressed by a react-graphing app...
soon to come"""
import csv

with open('databas-cfg.yaml') as cfg:
    config = yaml.load(cfg, Loader=yaml.FullLoader)

data = csvquery.open_csv("output.csv")

db = mysql.connector.connect(
    host=config[host],
    user=config[user],
    database="RocketRadio"
)

cursor = db.cursor()


