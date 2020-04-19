import csv
import json

from flask import Flask, request
flag = False
app = Flask(__name__)


@app.route('/')
def hello_world() :
    return json.dumps('Hello Guys!')

@app.route('/users/details')
def listing() :
    with open('data/users.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)

    return json.dumps(li)

@app.route('/users/register', methods=['POST'])
def create() :
    if flag == False :
        return json.dumps("Authentication error")
    with open('data/users.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id','name','contact_number','address','password'])
        cnt = json.loads(listing())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Success")

@app.route('/users/login',methods=['POST'])
def login():
    login_data = list(request.json.values())
    db = json.loads(listing())
    values=[]
    for i in db:
        values.append([i['name'],i['password']])
    if login_data in values:
        global flag
        flag=True

        return json.dumps("Login Successful")
    else:
        return json.dumps("Login Failed")

@app.route('/users/modify/<id>', methods=['PATCH'])
def edit(id) :
    if flag == False :
        return json.dumps("Authentication error")
    id = int(id)
    cnt = json.loads(listing())
    if id>len(cnt):
        return json.dumps("User not in the DB")
    cnt[id - 1]['password'] = request.json['password']
    with open('data/users.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'name', 'contact_number', 'address', 'password'])
        f1.writeheader()
        f1.writerows(cnt)

    return json.dumps("Modified password successfully")

@app.route('/users/delete/<int:id>', methods=['DELETE'])
def delete(id) :
    if flag==True:
        cnt = json.loads(listing())
        cnt.pop(id - 1)
        for i in range(len(cnt)) :
            cnt[i]['id'] = str(i + 1)
        with open('data/users.csv', 'w') as f1 :
            f1 = csv.DictWriter(f1, fieldnames=['id', 'name', 'email', 'mobile', 'age'])
            f1.writeheader()
            f1.writerows(cnt)

        return json.dumps("Deleted")
    else:
        return json.dumps("Authentication error")

################Start of the bus
@app.route('/buses',methods=['POST'])

def listingb() :
    if flag==False:
        return json.dumps("Authentication error")

    with open('data/buses.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)

    return json.dumps(li)

@app.route('/buses/register', methods=['POST'])

def createb() :
    if flag == False :
        return json.dumps("Authentication error")
    with open('data/buses.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id', 'bus_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        cnt = json.loads(listingb())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Success")

@app.route('/buses/search',methods=['POST'])

def show() :
    if flag == False :
        return json.dumps("Authentication error")
    number = request.json['bus_number']
    cnt = json.loads(listingb())
    for i in cnt:
        if i['bus_number']==number:
            flags = "Found in the DB"
            break
        else:
            flags = "Not in the DB"
    return json.dumps(flags)


@app.route('/buses/modify/<id>', methods=['PATCH'])

def editbbb(id) :
    if flag == False :
        return json.dumps("Authentication error")
    id = int(id)
    cnt = json.loads(listingb())
    if id>len(cnt):
        return "Bus not in the DB"
    cnt[id - 1] = request.json
    cnt[id-1]['id']=str(id)

    with open('data/buses.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'bus_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        f1.writeheader()
        f1.writerows(cnt)

    return json.dumps("Modified successfully")

@app.route('/buses/delete/<int:id>', methods=['DELETE'])
def delss(id):
    if flag == False :
        return json.dumps("Authentication error")
    cnt = json.loads(listingb())
    cnt.pop(id - 1)
    for i in range(len(cnt)) :
        cnt[i]['id'] = str(i + 1)
    with open('data/buses.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'bus_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        f1.writeheader()
        f1.writerows(cnt)

    return json.dumps("deletebd")



################Start of the train
@app.route('/trains',methods=['POST'])

def listingt() :
    if flag == False :
        return json.dumps("Authentication error")
    with open('data/trains.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)

    return json.dumps(li)

@app.route('/trains/register', methods=['POST'])

def createt() :
    if flag == False :
        return json.dumps("Authentication error")
    with open('data/trains.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id', 'train_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        cnt = json.loads(listingt())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Success")

@app.route('/trains/search',methods=['POST'])
def searcht() :
    if flag == False :
        return json.dumps("Authentication error")
    number = request.json['train_number']
    cnt = json.loads(listingt())
    for i in cnt:
        if i['train_number']==number:
            flags = "Found in the DB"
            break
        else:
            flags = "Not in the DB"
    return json.dumps(flag)

@app.route('/trains/modify/<id>', methods=['PATCH'])
def editt(id) :
    if flag == False :
        return json.dumps("Authentication error")
    id = int(id)
    cnt = json.loads(listingt())
    if id>len(cnt):
        return "train not in the DB"
    cnt[id - 1] = request.json
    cnt[id-1]['id']=str(id)

    with open('data/trains.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'train_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        f1.writeheader()
        f1.writerows(cnt)

    return json.dumps("Modified successfully")

@app.route('/trains/delete/<int:id>', methods=['DELETE'])
def deletet(id) :
    if flag == False :
        return json.dumps("Authentication error")
    cnt = json.loads(listingt())
    cnt.pop(id - 1)
    for i in range(len(cnt)) :
        cnt[i]['id'] = str(i + 1)
    with open('data/trains.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id','train_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        f1.writeheader()
        f1.writerows(cnt)

    return json.dumps("deletebd")

if __name__ == '__main__' :
    app.run(debug=True)
