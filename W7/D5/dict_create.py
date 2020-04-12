import csv
with open('all_details.csv','r') as f1:
    f1 = csv.reader(f1)
    cl=[]
    for i in f1:
        cl.append(i)
with open('dict_data.csv','w') as f2:
    f2 = csv.writer(f2)
    f2.writerow(['Name','Age','Gender','Japan'])
    f2.writerows(cl)

