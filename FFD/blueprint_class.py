from flask import Blueprint,request
import json,csv,jwt,time

class_ = Blueprint('class',__name__)

@class_.route('/student') # Shows details of students in the school interms of classes
def listing_stu() :
    with open('data/students_class.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)
    return json.dumps(li)
@class_.route('/teacher') # Dhows how teachers are assigned to classes and sections
def listing_tch() :
    with open('data/teacher_class.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)
    return json.dumps(li)

@class_.route('/student/register', methods=['POST'])
def create_stu() :
    print("Hello")
    with open('data/students_class.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id','student_id','class_id','section_id'])
        cnt = json.loads(listing_stu())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Student registered successfully")
@class_.route('/teacher/register', methods=['POST'])
def create_tch() :
    with open('data/teacher_class.csv', 'a') as f1 :
        f1 = csv.DictWriter(f1,fieldnames=['id','teacher_id','class_id','section_id'])
        cnt = json.loads(listing_stu())
        values = request.json
        print(values)
        values['id']=len(cnt)+1
        f1.writerow(values)
    return json.dumps("Teacher registered successfully")

@class_.route('/student/modify/<int:id>/<auth_token>', methods=['PATCH'])
def edit_stu(id,auth_token) :
    decoded = jwt.decode(auth_token,'hiro')
    if decoded['time']<time.time() or decoded['role']!='staff':   # Authentication only staff can modify stu details
        return json.dumps("Prankster")
    cnt = json.loads(listing_stu())
    if id>len(cnt):
        return json.dumps("Sorry Data unavailable")
    cnt[id-1]=request.json
    cnt[id-1]['id']=id
    with open('data/students_class.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id','student_id','class_id','section_id'])
        f1.writeheader()
        f1.writerows(cnt)
    return json.dumps("Student assigned successfully")
@class_.route('/teacher/modify/<int:id>/<auth_token>', methods=['PATCH'])
def edit_tch(id, auth_token) :
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] != 'staff' or decoded['id']!=str(id) :  # Authentication only staff can modify tch details
        return json.dumps("Prankster")
    cnt = json.loads(listing_tch())
    if id > len(cnt):
        return json.dumps("Sorry Data unavailable")
    cnt[id - 1] = request.json
    cnt[id - 1]['id'] = id
    cnt[id-1]['teacher_id']=decoded['id']
    with open('data/teacher_class.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'teacher_id', 'class_id', 'section_id'])
        f1.writeheader()
        f1.writerows(cnt)
    return json.dumps("Teacher assigned successfully")


@class_.route('/student/delete/<int:id>/<auth_token>', methods=['DELETE'])
def delete_stu(id,auth_token) :
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] != 'staff' or decoded['id'] != str(id) :  # Authentication only staff can modify tch details
        return json.dumps("Prankster")
    cnt = json.loads(listing_stu())
    if len(cnt)<id:
        return json.dumps("Resourse unavailable")
    cnt.pop(id - 1)
    for i in range(len(cnt)) :
        cnt[i]['id'] = str(i + 1)
    with open('data/students_class.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'student_id', 'class_id', 'section_id'])
        f1.writeheader()
        f1.writerows(cnt)
    return json.dumps("Deleted")
@class_.route('/teacher/delete/<int:id>/<auth_token>', methods=['DELETE'])
def delete_tch(id,auth_token) :
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] != 'staff' :  # Authentication only staff can modify tch details
        return json.dumps("Prankster")
    cnt = json.loads(listing_tch())
    if len(cnt)<id:
        return json.dumps("Resourse unavailable")
    cnt.pop(id - 1)
    for i in range(len(cnt)) :
        cnt[i]['id'] = str(i + 1)
    print(cnt)
    with open('data/teacher_class.csv', 'w') as f1 :
        f1 = csv.DictWriter(f1, fieldnames=['id', 'teacher_id', 'class_id', 'section_id'])
        f1.writeheader()
        f1.writerows(cnt)
    return json.dumps("Deleted")

@class_.route('/student/search/<auth_token>',methods=['POST'])
def search_stu(auth_token):
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] != 'student' :
        return json.dumps("Not a student")
    cnt = json.loads(listing_stu())
    for i in cnt:
        if i['id']==decoded['id']:
            return json.dumps(i)
    return json.dumps("NOT IN DB")

@class_.route('/teacher/search/<auth_token>',methods=['POST'])
def search_tch(auth_token):
    decoded = jwt.decode(auth_token, 'hiro')
    if decoded['time'] < time.time() or decoded['role'] != 'staff' :
        return json.dumps("Not a staff")
    cnt = json.loads(listing_tch())
    ans=[]
    for i in cnt:
        if i['id']==decoded['id']:
            ans.append(i)
    return json.dumps(i)







