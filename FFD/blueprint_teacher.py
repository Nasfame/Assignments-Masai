from flask import Blueprint,request
import json,csv,jwt,time

staff = Blueprint('staff',__name__)


@staff.route('/details') # Shows details of teachers in the school
def listing() :
    with open('data/teachers.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)
    return json.dumps(li)

@staff.route('/register', methods=['POST'])
def create() :
    with open('data/teachers.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id','name','subject','years_of_experience'])
        cnt = json.loads(listing())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Success")

@staff.route('/login',methods=['POST'])
def login():
    login_data = list(request.json.values())
    db = json.loads(listing())
    values=[]
    role=''
    id =''
    for i in db:
        values.append([i['name']])
        if i['name']== login_data[0]:
            role='staff'
            id = i['id']
            break

    payload = {'username':login_data[0],'id':id,'role':role,'time':time.time()+3600}  # Logged Out
    encode_jwt = jwt.encode(payload, 'hiro')
    return {'auth_token':encode_jwt.decode()} #converts bits to string

@staff.route('/modify/<int:id>/<auth_token>', methods=['PATCH'])
def edit(id,auth_token) :
    decoded = jwt.decode(auth_token,'hiro')
    if decoded['time']<time.time() or decoded['role']!='staff':
        return json.dumps("Impostor")
    cnt = json.loads(listing())
    if id>len(cnt):
        return json.dumps("Sorry Data unavailable")


    if decoded['username'] == cnt[id-1]['name'] or decoded['role']=='admin': # Authentication
        cnt[id - 1] = request.json
        cnt[id - 1]['id'] = str(id)
        with open('data/teachers.csv', 'w') as f1 :
            f1 = csv.DictWriter(f1, fieldnames=['id','name','subject','years_of_experience'])
            f1.writeheader()
            f1.writerows(cnt)
        return json.dumps("Modified details successfully")
    else:
        return json.dumps("Incorrect username!")

@staff.route('/delete/<int:id>/<auth_token>', methods=['DELETE'])
def delete(id,auth_token) :
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] != 'staff' :
        return json.dumps("Impostor")

    cnt = json.loads(listing())
    if len(cnt)<id:
        return json.dumps("Resourse unavailable")

    if decoded['username'] == cnt[id - 1]['name'] or decoded['role'] == 'admin' :
        cnt.pop(id - 1)
        for i in range(len(cnt)) :
            cnt[i]['id'] = str(i + 1)
        with open('data/teachers.csv', 'w') as f1 :
            f1 = csv.DictWriter(f1, fieldnames=['id','name','subject','years_of_experience'])
            f1.writeheader()
            f1.writerows(cnt)
    return json.dumps("Deleted")

