import csv

file = open('user_data.csv','r')
f1 = csv.reader(file)
cl = []
for i in f1:
    cl.append(i)
file.close()
print(cl)
with open('all_details.csv','w') as f2:
    f2 = csv.writer(f2)
    f2.writerows(cl)




