import pymysql
import datetime
import pandas as pd
import collections
db = pymysql.connect(host='103.218.161.81', user='kktmlab_RO', password='kktmlab1', db='db_smart_ev', charset='utf8')
curs = db.cursor()
curs2 = db.cursor()

query = """select b.binary, b.id from db_smart_ev.data_bin as b;"""
query2 ="SELECT * from db_smart_ev.ideal_floor order by id;"
curs.execute(query)
rows1 = curs.fetchall()

bi_dic ={}

hallcall_list = []
#bin_list = [row[0] for row in rows1]

curs2.execute(query2)
rows2 = curs2.fetchall()

ideal_list =[]

for row in rows1:
   bi_dic[row[1]] = row[0]


"""




"""
#b0, f1, i2
for row in rows2:
    if str(row[0])[14:19] == '00000':
        bi_dic[row[2]] = str(row[0][0:42])+str('0011')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00001':
        bi_dic[row[2]] = str(row[0][0:42])+str('0011')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00010':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00011':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00100':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00101':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00110':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='00111':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01000':
        bi_dic[row[2]] = str(row[0][0:42])+str('0101')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01001':
        bi_dic[row[2]] = str(row[0][0:42])+str('0110')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01010':
        bi_dic[row[2]] = str(row[0][0:42])+str('0101')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01011':
        bi_dic[row[2]] = str(row[0][0:42])+str('0101')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01100':
        bi_dic[row[2]] = str(row[0][0:42])+str('0101')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01101':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01110':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='01111':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10000':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10001':
        bi_dic[row[2]] = str(row[0][0:42])+str('0011')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10010':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10011':
        bi_dic[row[2]] = str(row[0][0:42])+str('0100')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10100':
        bi_dic[row[2]] = str(row[0][0:42])+str('0011')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10101':
        bi_dic[row[2]] = str(row[0][0:42])+str('0011')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10110':
        bi_dic[row[2]] = str(row[0][0:42])+str('0010')+str(row[0][46:48])
        continue
    elif str(row[0])[14:19]=='10111':
        bi_dic[row[2]] = str(row[0][0:42])+str('0011')+str(row[0][46:48])
        continue



od = collections.OrderedDict(sorted(bi_dic.items()))
bin_list = [x for _, x in od.items()]

# 10010101110000(date)14 => [0:14]
# 01010011111000011(time)17 => [14:31]
# 001(state)3  => [31:34]
# 0111(doorstate)4 => [34:38]
# 0000(ev_floor)4 => [38:42]
# 0001(cu_floor)4 => [42:46]
# 00(event)2 => [46:48]


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
hallcall_df.to_csv('./w_time_lstm.csv')
