import pymysql
import datetime
import pandas as pd

db = pymysql.connect(host='103.218.161.81', user='kktmlab_RO', password='kktmlab1', db='db_smart_ev', charset='utf8')
curs = db.cursor()

query = """select b.binary from db_smart_ev.data_bin as b;"""

curs.execute(query)
rows = curs.fetchall()

hallcall_list = []

for row,_ in rows:
    if row[46:48] == '10' or row[46:48] == '11':
        for after_hallcall,_ in rows:
            if ((int(row[9:14],2) == int(after_hallcall[9:14],2)) or (int(row[9:14],2)+1 == int(after_hallcall[9:14],2))) \
                and (after_hallcall[34:38] == '0100' or after_hallcall[34:38] == '0101' or after_hallcall[34:38] == '0110') \
                and (int(row[14:19],2) <= int(after_hallcall[14:19],2)) and (int(row[19:25],2) <= int(after_hallcall[19:25],2)) and (int(row[25:31],2) < int(after_hallcall[25:31],2)) \
                and (after_hallcall[42:46] == row[38:42]):
                d_time = str(int(after_hallcall[14:19],2)) +':'+ str(int(after_hallcall[19:25],2)) +':'+ str(int(after_hallcall[25:31],2))
                e_time = str(int(row[14:19],2)) +':'+ str(int(row[19:25],2)) +':'+ str(int(row[25:31],2))
                w_time = datetime.datetime.strptime(d_time, '%H:%M:%S') - datetime.datetime.strptime(e_time, '%H:%M:%S')
                hallcall_list.append([row[0:14], e_time, d_time, str(w_time),])
                break

eliminate_list = []
for i in range(1,len(hallcall_list)):
    if hallcall_list[i-1][2] == hallcall_list[i][2]:
        eliminate_list.append(i)
eliminate_list.reverse()
for i in eliminate_list:
    del hallcall_list[i]

hallcall_df = pd.DataFrame(data = hallcall_list, columns = ['event_bin','e_time','d_time','w_time'])
hallcall_df.to_csv('./w_time.csv')