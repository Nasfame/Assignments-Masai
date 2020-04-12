import json


cl = [{'name':'Hiro','gender':'M','age':18,'country':'Japan','weight':'40.0'},
{'name':'Hiro','gender':'M','age':18,'country':'Japan','weight':'40.0'},
{'name':'Hiro','gender':'M','age':18,'country':'Japan','weight':'40.0'},
{'name':'Hiro','gender':'M','age':18,'country':'Japan','weight':'40.0'},
{'name':'Hiro','gender':'M','age':18,'country':'Japan','weight':'40.0'}]
print(cl)
daump = json.dumps(cl)
with open('user_data.json','w') as f1:
        f1.write(daump)




