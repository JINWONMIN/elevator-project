from collections import Counter
import csv
lst = []
lst2 =[]
with open(r'C:\Users\jiho_lab\Desktop\HOHO\06_Elevator\04_data\all_ev.csv', 'r', encoding='UTF8') as reader:
    for line in reader:
        lst.append("".join(line.split()))
del lst[0]
for i in lst:
#    lst2.append(i[0:2])
    lst2.append(i)
result = Counter(lst2)
for key in result:
    print (key)
for key in result:
    print (result[key])
