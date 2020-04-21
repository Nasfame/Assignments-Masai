import csv,json,math
from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def hello_world() :
    return 'Hello World!'

@app.route('/users')
def listing() :
    with open('data/users.csv', 'r') as f1 :
        f1 = csv.DictReader(f1)
        li = list(f1)
        pg_wanted = request.args.get('page',default=1,type=int)
        items_per = request.args.get('total_items',default=5,type=int)
        cur_page_start = (pg_wanted-1)*items_per
        response = li[cur_page_start:cur_page_start+items_per]



    return json.dumps(response)


if __name__ == '__main__' :
    app.run(debug=True)


