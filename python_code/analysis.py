""" This file's purpose is to convert csv produced by receiver.py into database fields, which will be inserted into a MySQL db, that can be addressed by a react-graphing app...
soon to come"""
import csvquery, mysql, yaml

data = csvquery.open_csv("output.csv")

db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

cursor = db.cursor()


