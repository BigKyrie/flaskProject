# from flask import Flask
from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

USERS = {
    1: {'name': 'A', 'age': '18', 'gender': 'man', 'text': 'Cute'},
    2: {'name': 'B', 'age': '20', 'gender': 'man', 'text': 'Warm'},
    3: {'name': 'C', 'age': '21', 'gender': 'women', 'text': 'Beautiful'},
    4: {'name': 'D', 'age': '20', 'gender': 'women', 'text': 'Duke'},

}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)
    # todo_list = Todo.query.all()
    # print(todo_list)
    # return render_template('base.html')


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()

    new_todo = Todo(title = "todo 1", complete = False)
    db.session.add(new_todo)
    db.session.commit()
    app.run(debug=True)
# @app.route('/detail/<int:nid>', methods=['GET'])  #
# def detail(nid):
#     user = session.get('user_info')
#     if not user:
#         url = url_for('l1')  #
#         return redirect(url)
#     info = USERS[nid]
#     return render_template('detail.html', info=info)  #


# @app.route('/', methods=['GET', 'POST'], endpoint='l1')  # endpoint 表示别名
# def login():
#     # return redirect('https://www.google.com')
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         user = request.form.get('user')  #
#         pwd = request.form.get('pwd')
#         if user == 'alex' and pwd == '123':
#             return redirect('https://www.google.com')
#             # session['user_info'] = user
#             # return redirect('https://www.google.com')  #
#         return render_template('login.html', error='error password or username')  #


# @app.route('/index', methods=['GET'])
# def index():
#     user = session.get('user_info')
#     if not user:
#         return redirect('/login') #
#     return render_template('index.html', user_dict=USERS)


