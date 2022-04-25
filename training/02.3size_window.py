import csv

read = open('./06.csv', 'r')
write = open('./07.dataset.csv', 'w')
try:
    reader = csv.reader(read)
    writer = csv.writer(write)
    X1 = []
    X2 = []
    X3 = []
    Y = []
    for row in reader:
        if len(X1)==0:
            X1 = row
            continue
        elif len(X2)==0:
            X2 = row
            continue
        elif len(X3)==0:
            X3 = row
            continue
        elif len(Y)==0:
            Y = row
            writer.writerow((X1[1], X2[1], X3[1], Y[1]))
            continue
        elif len(X1)*len(X2)*len(X3)*len(Y)!=0:
            X1 = X2
            X2 = X3
            X3 = Y
            Y = row
            writer.writerow((X1[1], X2[1], X3[1], Y[1]))
finally:
    read.close()
    write.close()