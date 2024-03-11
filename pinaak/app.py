#imports-----------------------------------------------------
from flask import Flask, render_template, request
from tinydb import TinyDB, Query
#initialize--------------------------------------------------
app = Flask(__name__)
db = TinyDB('db.json')
User = Query()

#functions---------------------------------------------------
def initialize_table():
    global table, table2
    table = db.table('data')
    table2 = db.table('meta-data')

def count_visiter():
    t = table2.search(User.name == "visitor")
    print(t, type(t))
    if t == []:
        table2.insert({"name": "visitor", "v_count": 1})
    else: 
        t = t[0]['v_count'] + 1
        table2.update({'v_count': t})

def count_subscriber():
    t = table2.search(User.name == 'subscriber')
    print(t)
    if t == []:
        table2.insert({"name": "subscriber", "s_count": 1})
    else:
        t = t[0]['s_count'] + 1
        table2.update({'s_count': t})

#routes------------------------------------------------------
@app.route('/')
def home():
    count_visiter()
    return render_template('index.html', title='Thanks')

@app.route('/upvote', methods=['POST'])
def response():
    count_subscriber()
    type = request.form.get('type')
    username = request.form.get('username')
    email = request.form.get('email')
    if type == 'budget':
        table.insert({"username": username, "email": email, "signfor": type})
    elif type == 'mid':
        table.insert({"username": username, "email": email, "signfor": type})
    return render_template("success.html", title="Success")

@app.route('/about')
def method_name():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    initialize_table()
    app.run(debug=True)
