import json
import csv

with open('user_data.json','r') as f1:
    cnt= f1.readline()
    ct = json.loads(cnt)

for i in ct:
    i['occupation']='Techie'
cti = json.dumps(ct)

with open('user_data.json','w') as f1:
    f1.writelines(cti)


with open('user_data_csv.csv','w') as f1:
    f1 = csv.writer(f1)
    for i in ct:
        if i['age']>18:

            actual = list(map(str,i.values()))
            f1.writerow(actual)








