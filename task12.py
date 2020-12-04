
JSON file

[
    [

    {"name":"charishma", "age":19,"city":"guntur"},
    [1,2,3,4,5],
    [6,7,8,9,10],
    "Myself",
    16,
    16.2,
    true,
    null]
]


#importing JSON file into MYSQL database
import sqlite3
import json
connection = sqlite3.connect("test.db")
print("Database Opened")
cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE MY"
                   "("
                   + "dictinary BLOB,"
                   + "list BLOB,"
                   + "tuple BLOB,"
                   + "string varchar(50),"
                   + "Integer INTEGER,"
                   + "flo FLOAT,"
                   + "Bool BOOLEAN,"
                   + "None BLOB"
                     ");")
except Exception as ex:
    print("Error :", ex)
else:
    print("Table created")
datafile = open("examole.json")
dataset = json.load(datafile)
dataframe = []
for row in dataset:
    data = (str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4]),
            float(row[5]), bool(row[6]), row[7])
    dataframe.append(data)

try:
    cursor.executemany("INSERT INTO MY VALUES (?,?,?,?,?,?,?,?)", dataframe)
except Exception as ex:
    print("Error : ", ex)
else:
    connection.commit()
    print("Data inserted")
try:
    cursor.execute("SELECT * from MY")
except Exception as ex:
    print("Error : ", ex)
else:
    for row in cursor.fetchall():
        print(row)
connection.close()
