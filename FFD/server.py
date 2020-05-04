import csv,json,jwt
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
        f1 = csv.DictWriter(f1,fieldnames=['id','name','contact_number','address','password','role'])
        cnt = json.loads(listing())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        values['role']='user'
        f1.writerow(values)
    return json.dumps("Success")

@app.route('/users/login',methods=['POST'])
def login():
    login_data = list(request.json.values())
    db = json.loads(listing())
    values=[]
    role=''
    for i in db:
        values.append([i['name'],i['password']])
        if i['name']== login_data[0]:
            role = i['role']
    payload = {'username':login_data[0],'status':'LO','role':role}  # Logged Out

    if login_data in values:
        global flag
        flag=True
        payload['status']='LI'   # Logged In
        encode_jwt = jwt.encode(payload,'hiro')
        return {'auth_token':encode_jwt.decode()}
    else:
        return {'auth_token':encode_jwt.decode()}

@app.route('/users/modify/<id>/<auth_token>', methods=['PATCH'])
def edit(id,auth_token) :
    decoded = jwt.decode(auth_token,'hiro')
    if flag==False:
        return json.dumps("Service QUiting!")
    if decoded['status']=='LO':
        return json.dumps("Process encountered a rail road spike")
    id = int(id)
    cnt = json.loads(listing())
    if id>len(cnt):
        return json.dumps("User not in the DB")
    cnt[id - 1]['password'] = request.json['password']
    if decoded['username'] == cnt[id-1]['name'] or decoded['role']=='admin':
        with open('data/users.csv', 'w') as f1 :
            f1 = csv.DictWriter(f1, fieldnames=['id', 'name', 'contact_number', 'address', 'password','role'])
            f1.writeheader()
            f1.writerows(cnt)
        return json.dumps("Modified password successfully")
    else:
        return json.dumps("Don't Trick me Mister!")

@app.route('/users/delete/<int:id>/<auth_token>', methods=['DELETE'])
def delete(id,auth_token) :
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['status']=='LI':
        cnt = json.loads(listing())
        cnt.pop(id - 1)
        for i in range(len(cnt)) :
            cnt[i]['id'] = str(i + 1)
        if decoded['username'] == cnt[id - 1]['name'] or decoded['role'] == 'admin' :
            with open('data/users.csv', 'w') as f1 :
                f1 = csv.DictWriter(f1, fieldnames=['id', 'name', 'contact_number','address','password','role'])
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

@app.route('/buses/register/<auth_token>', methods=['POST'])
def createb(auth_token) :
    if jwt.decode(auth_token, 'hiro')['role']!='admin' :
        return json.dumps("Authentication error")
    with open('data/buses.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id', 'bus_number', 'departure_loc', 'arrival_loc', 'journey_duration','fare'])
        cnt = json.loads(listingb())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Success")

@app.route('/buses/search/<auth_token>',methods=['POST'])
def show(auth_token) :
    if jwt.decode(auth_token, 'hiro')['role']=='' :
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


@app.route('/buses/modify/<id>/<auth_token>', methods=['PATCH'])
def editbbb(id,auth_token) :
    if flag == False :
        return json.dumps("Authentication error")
    if jwt.decode(auth_token, 'hiro')['role']!='admin':
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

@app.route('/buses/delete/<int:id>/<auth_token>', methods=['DELETE'])
def delss(id,auth_token):
    if flag == False :
        return json.dumps("Authentication error")
    if jwt.decode(auth_token, 'hiro')['role'] != 'admin' :
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

@app.route('/trains/register/<auth_token>', methods=['POST'])

def createt(auth_token) :
    if flag == False :
        return json.dumps("Authentication error")
    if jwt.decode(auth_token, 'hiro')['role'] != 'admin' :
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

@app.route('/trains/modify/<id>/<auth_token>', methods=['PATCH'])
def editt(id,auth_token) :
    if flag == False :
        return json.dumps("Authentication error")
    if jwt.decode(auth_token, 'hiro')['role'] != 'admin' :
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

@app.route('/trains/delete/<int:id>/<auth_token>', methods=['DELETE'])
def deletet(id,auth_token) :
    if flag == False :
        return json.dumps("Authentication error")
    if jwt.decode(auth_token, 'hiro')['role'] != 'admin' :
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
