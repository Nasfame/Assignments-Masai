from flask import Flask,request
import csv,json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/listing')
def list():

    with open('data/groceries.csv','r') as f1:
        f1 = csv.DictReader(f1)
        li=[]
        for i in f1:
            li.append(i)
        content = json.dumps(li)
    return content

@app.route('/create',methods=['POST'])
def create():

    with open('data/groceries.csv','a') as f2:
        f2 = csv.writer(f2)
        f2.writerow([request.json['item'],request.json['quantity'],'false'])

    return "Successfully Created"

@app.route('/edit/<int:item_no>',methods=['POST']) ## assuming itemno is the line number in file
def modify(item_no):

    cnt = json.loads(list())
    cnt[item_no] = {'item':request.json['item'],'quantity':request.json['quantity']}
    with open('data/groceries.csv','w') as f1:
        f1=csv.DictWriter(f1,fieldnames=['item','quantity','purchased'])
        f1.writeheader()
        f1.writerows(cnt)
    return "All went well"

@app.route('/delete/<int:item_no>',methods=['POST'])
def deli(item_no):
    cnt = json.loads(list())
    cnt.pop(item_no)
    with open('data/groceries.csv','w') as f1:
        f1=csv.DictWriter(f1,fieldnames=['item','quantity','purchased'])
        f1.writeheader()
        f1.writerows(cnt)
    return "All went well"

@app.route('/purchased/<int:item_no>',methods=['POST'])
def purp(item_no):
    cnt = json.loads(list())
    cnt[item_no]['purchased'] = 'true'
    with open('data/groceries.csv','w') as f1:
        f1=csv.DictWriter(f1,fieldnames=['item','quantity','purchased'])
        f1.writeheader()
        f1.writerows(cnt)

    return "Deal"
@app.route('/purchased')
def purchase():
    cnt = json.loads(list())
    pur = []
    for i in cnt:
        if i['purchased']=='true':
            pur.append(i['item'])

    return json.dumps(pur)

if __name__ == '__main__':
    app.run(debug=True)