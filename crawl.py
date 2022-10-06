import re
import requests
import mysql.connector as database
import json
import time


connection = database.connect(
    user='root',
    password='8K8g&NBU:6Lls2]HsMW}+i',
    host='nas.local',
    database="nihondrive")

#sql = """INSERT INTO Question (Question, OptionT, OptionF, Answer) VALUES (%s, %s, %s, %s)"""
sql = """INSERT INTO Honmen (Question, OptionT, OptionF, Answer) VALUES (%s, %s, %s, %s)"""

loopCount = 1000
for x in range(loopCount):
    r = requests.get("https://nihondrive.com/honmendrivingtest")

    script = re.findall(r'const question.*]\n\n\n' ,r.text, re.DOTALL)[0].replace("const questions = ", "")
    script = script.replace("question", '"question"').replace("optionT:", '"optionT":').replace("optionF:", '"optionF":')
    script = script.replace("correctOption", '"correctOption"')
    script = script.replace("},\n          \n        ]", "}]")


    records = json.loads(script)

    records_to_insert = []
    for o in records:
        records_to_insert.append((o['question']
            ,o['optionT']
            ,o['optionF']
            ,o['correctOption']
            ))

    cursor = connection.cursor()
    cursor.executemany(sql, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into QUESTION table, loop #", x)
    
    time.sleep(1)
