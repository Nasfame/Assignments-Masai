import csv

user = input().split(',')
dict_user = {'username': user[0], 'password': user[1]}

with open('users.csv', 'r') as f1:
    f1 = csv.DictReader(f1)
    cnt = []
    for i in f1:
        cnt.append(i)

if dict_user in cnt:
    print("User Already Exits")
else:
    cnt.append(dict_user)
    with open('users.csv', 'w') as f1:
        f1 = csv.DictWriter(f1, fieldnames=['username', 'password'])
        f1.writeheader()
        f1.writerows(cnt)
