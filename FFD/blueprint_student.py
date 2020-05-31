from flask import Blueprint,request
import json,csv,jwt,time

student = Blueprint('student',__name__)

@student.route('/details') # Shows details of students in the school
def listing() :
    with open('data/students.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)
    return json.dumps(li)

@student.route('/register', methods=['POST'])
def create() :
    with open('data/students.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id','name','email','gender','password','contact_number','address','father_name','mother_name'])
        cnt = json.loads(listing())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Success")

@student.route('/login',methods=['POST'])
def login():
    login_data = list(request.json.values())
    db = json.loads(listing())
    values=[]
    role=''
    id=''
    for i in db:
        values.append([i['name']])
        if i['name']== login_data[0] and i['password']==login_data[1]:
            role='student'
            id = i['id']
            break
    payload = {'username':login_data[0],'id':id,'role':role,'time':time.time()+3600}#  LoggedOutafter 1hr 3600sec
    encode_jwt = jwt.encode(payload, 'hiro')
    return {'auth_token':encode_jwt.decode()}         #converts bits to string

@student.route('/modify/<int:id>/<auth_token>', methods=['PATCH'])
def edit(id,auth_token) :
    decoded = jwt.decode(auth_token,'hiro')
    if decoded['time']<time.time() or decoded['role']=='':
        return json.dumps("Prankster")
    cnt = json.loads(listing())
    if id>len(cnt):
        return json.dumps("Sorry Data unavailable")

    if decoded['username'] == cnt[id-1]['name'] or decoded['role']=='admin': # Authentication
        cnt[id - 1]['password'] = request.json['password']
        with open('data/students.csv', 'w') as f1 :
            f1 = csv.DictWriter(f1, fieldnames=['id','name','email','gender','password','contact_number','address','father_name','mother_name'])
            f1.writeheader()
            f1.writerows(cnt)
        return json.dumps("Modified password successfully")
    else:
        return json.dumps("Incorrect username!")

@student.route('/delete/<int:id>/<auth_token>', methods=['DELETE'])
def delete(id,auth_token) :
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] == '' :
        return json.dumps("Impostor")

    cnt = json.loads(listing())
    if len(cnt)<id:
        return json.dumps("Resourse unavailable")

    if decoded['username'] == cnt[id - 1]['name'] or decoded['role'] == 'staff' :
        cnt.pop(id - 1)
        for i in range(len(cnt)) :
            cnt[i]['id'] = str(i + 1)
        with open('data/students.csv', 'w') as f1 :
            f1 = csv.DictWriter(f1,fieldnames=['id','name','email','gender','password','contact_number','address','father_name','mother_name'])
            f1.writeheader()
            f1.writerows(cnt)
    return json.dumps("Deleted")

