import csv

user = input().split(',')
dict_user = {'username': user[0], 'password': user[1]}

with open('users.csv', 'r') as f1:
    f1 = csv.DictReader(f1)
    cnt = []
    for i in f1:
        cnt.append(i)

our_users = []

for i in cnt:
    for y in i.values():
        our_users.append(y)

if dict_user in cnt:
    print("Login Successful")
elif user[0] not in our_users:
    print("User Not Found")

else:
    print("Wrong Password")