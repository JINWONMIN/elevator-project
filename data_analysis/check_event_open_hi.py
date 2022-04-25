import pymysql
import datetime
import pandas as pd

db = pymysql.connect(host='103.218.161.81', user='kktmlab_RO', password='kktmlab1', db='db_smart_ev', charset='utf8')
curs = db.cursor()

query = """select b.binary from db_smart_ev.data_bin as b;"""

curs.execute(query)
rows = curs.fetchall()

hallcall_list = []

bin_list = [row[0] for row in rows]

for index, event_occur in enumerate(bin_list):
    if event_occur[46:48] == '10' or event_occur[46:48] == '11':
        for door_open in bin_list[index:]:
            if ((int(event_occur[9:14],2) == int(door_open[9:14],2)) or (int(event_occur[9:14],2)+1 == int(door_open[9:14],2))) \
                and (door_open[34:38] == '0100' or door_open[34:38] == '0101' or door_open[34:38] == '0110') \
                and (door_open[42:46] == event_occur[38:42]):
                d_time = str(int(door_open[14:19],2)) +':'+ str(int(door_open[19:25],2)) +':'+ str(int(door_open[25:31],2))
                e_time = str(int(event_occur[14:19],2)) +':'+ str(int(event_occur[19:25],2)) +':'+ str(int(event_occur[25:31],2))
                w_time = datetime.datetime.strptime(d_time, '%H:%M:%S') - datetime.datetime.strptime(e_time, '%H:%M:%S')
                hallcall_list.append([event_occur[0:14], e_time, d_time, str(w_time),])
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