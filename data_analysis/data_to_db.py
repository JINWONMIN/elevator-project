import pymysql
import pandas as pd
import numpy

db = pymysql.connect(host='127.0.0.1', user='system', password='1234', db='good', charset='utf8')
curs = db.cursor()

sql = """insert into data_raw values (%s,%s,%s,%s,%s,%s,%s,%s)"""

fd = pd.read_csv(r"C:\Users\minjw\Desktop\프로젝트 1조 기획\프로젝트 1조 기획\final.csv", encoding = 'utf8', low_memory=False)
for index in range(len(fd.index)):
    row = fd.iloc[index].values.tolist()
    #print(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
    try:
        curs.execute(sql, [str(i) for i in row])
        db.commit()
    except Exception as e:
        print(e)
        pass

    pip install pandas

    