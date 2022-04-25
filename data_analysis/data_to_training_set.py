#%%
import pymysql
import pandas as pd
import numpy
import random
import time
from llist import dllist, dllistnode
db = pymysql.connect(host='103.218.161.81', user='kktmlab_RW', password='kktmlab1', db='db_smart_ev', charset='utf8')
curs = db.cursor()

sql = """select b.binary,b.id  from db_smart_ev.data_bin as b order by b.id"""
sql2 = """insert into ideal_floor values (%s, %s, %s)"""

curs.execute(sql)
rows = curs.fetchall()
count =0
bin_lst = []
res_bin =[]
dict = {'nan': '0', 'STOP': '001', 'STOP/DOWN': '010', 'STOP/UP': '011', 'RUN/DOWN': '100', 'RUN/UP': '101',
        'CarCall': '01', 'HallCallDown': '10',
        'HallCallUp': '11', 'DOOR CLOSE 처리중': '0001', 'DOOR CLOSE 처리중 DN LAMP ON': '0010', 'DOOR CLOSE 처리중 UP LAMP ON': '0011',
        'DOOR OPEN 처리중': '0100', 'DOOR OPEN 처리중 DN LAMP ON': '0101', 'DOOR OPEN 처리중 UP LAMP ON': '0110', 'DOOR 닫힘상태': '0111',
        'DOOR 닫힘상태 DN LAMP ON': '1000', 'DOOR 닫힘상태 UP LAMP ON': '1001', "B1": "0001", "1F": "0010", "2F": "0011",
        "3F": "0100", "4F": "0101", "5F": "0110", "6F": "0111", "7F": "1000", "8F": "1001", "9F": "1010", "10F": "1011",
        "11F": "1100"}

for full_binary,_ in rows:
    bin_lst.append(full_binary)

# 10010101110000(date)14 => [0:14]
# 01010011111000011(time)17 => [14:31]
# 001(state)3  => [31:34]
# 0111(doorstate)4 => [34:38]
# 0000(ev_floor)4 => [38:42]
# 0001(cu_floor)4 => [42:46]
# 00(event)2 => [46:48]

for index, f_bin in enumerate(bin_lst):
    if (str(f_bin[31:34])=='001'):
        for comp_bin in bin_lst[index+1:]:
            if (str(comp_bin[46:48])== '10' or str(comp_bin[46:48])=='11'):
            #    res_bin.append([str(f_bin[0:15])+str(f_bin[15:32]), str(comp_bin[39:43])])
                curs.execute(sql2, (str(f_bin), str(comp_bin[38:42]), int(index+1)))
                break
    db.commit()

