import pymysql
import pandas as pd
import numpy

db = pymysql.connect(host='103.218.161.81', user='kktmlab_RW', password='kktmlab1', db='db_smart_ev', charset='utf8')
curs = db.cursor()

sql = """select r.date,r.time,r.state,r.door_state,r.event_floor,r.current_floor,r.event  from db_smart_ev.data_raw as r order by r.date, r.time"""
sql2 = """insert into data_bin(`binary`) values (%s)"""

curs.execute(sql)
rows = curs.fetchall()
lst = []

dict = {'nan': '0', 'STOP': '001', 'STOP/DOWN': '010', 'STOP/UP': '011', 'RUN/DOWN': '100', 'RUN/UP': '101',
        'CarCall': '01', 'HallCallDown': '10',
        'HallCallUp': '11', 'DOOR CLOSE 처리중': '0001', 'DOOR CLOSE 처리중 DN LAMP ON': '0010', 'DOOR CLOSE 처리중 UP LAMP ON': '0011',
        'DOOR OPEN 처리중': '0100', 'DOOR OPEN 처리중 DN LAMP ON': '0101', 'DOOR OPEN 처리중 UP LAMP ON': '0110', 'DOOR 닫힘상태': '0111',
        'DOOR 닫힘상태 DN LAMP ON': '1000', 'DOOR 닫힘상태 UP LAMP ON': '1001', "B1": "0001", "1F": "0010", "2F": "0011",
        "3F": "0100", "4F": "0101", "5F": "0110", "6F": "0111", "7F": "1000", "8F": "1001", "9F": "1010", "10F": "1011",
        "11F": "1100"}
for date, time, state, door, ev_floor, cu_floor, event in rows:
    str_tmp = ""
    str_tmp = str_tmp + format(int(str(date)[2:4]), 'b').zfill(5)
    str_tmp = str_tmp + format(int(str(date)[4:6]), 'b').zfill(4)
    str_tmp = str_tmp + format(int(str(date)[6:8]), 'b').zfill(5)
    str_tmp = str_tmp + format(int(str(time).zfill(6)[0:2]), 'b').zfill(5)
    str_tmp = str_tmp + format(int(str(time).zfill(6)[2:4]), 'b').zfill(6)
    str_tmp = str_tmp + format(int(str(time).zfill(6)[4:6]), 'b').zfill(6)
    str_tmp = str_tmp + dict[state].zfill(3)
    str_tmp = str_tmp + dict[door].zfill(4)
    str_tmp = str_tmp + dict[ev_floor.strip()].zfill(4)
    str_tmp = str_tmp + dict[cu_floor.strip()].zfill(4)
    str_tmp = str_tmp + dict[event].zfill(2)
    curs.execute(sql2, str_tmp)
    db.commit()