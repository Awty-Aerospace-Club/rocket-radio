""" This file's purpose is to convert csv produced by receiver.py into database fields that can be addressed by a react-graphing app...
soon to come"""
import csvquery, mysql.connector, yaml

data = csvquery.open_csv("output.csv")

db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

cursor = db.cursor()


