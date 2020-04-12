import csv

file = open("user_data.csv",'r')
f = csv.reader(file)
nl = []
al=[]
for i in f:
    nl.append(i[0])
    al.append(i[1])

file.close()