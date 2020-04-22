import csvquery, mysql.connector, yaml

data = csvquery.open_csv("output.csv")

db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

cursor = db.cursor()


