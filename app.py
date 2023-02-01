# from flask import Flask
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

app.debug = False  #
USERS = {
    1: {'name': 'A', 'age': '18', 'gender': 'man', 'text': 'Cute'},
    2: {'name': 'B', 'age': '20', 'gender': 'man', 'text': 'Warm'},
    3: {'name': 'C', 'age': '21', 'gender': 'women', 'text': 'Beautiful'},
    4: {'name': 'D', 'age': '20', 'gender': 'women', 'text': 'Duke'},

}


@app.route('/detail/<int:nid>', methods=['GET'])  #
def detail(nid):
    user = session.get('user_info')
    if not user:
        url = url_for('l1')  #
        return redirect(url)
    info = USERS[nid]
    return render_template('detail.html', info=info)  #


@app.route('/', methods=['GET', 'POST'], endpoint='l1')  # endpoint 表示别名
def login():
    # return redirect('https://www.google.com')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')  #
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            return redirect('https://www.google.com')
            # session['user_info'] = user
            # return redirect('https://www.google.com')  #
        return render_template('login.html', error='error password or username')  #


# @app.route('/index', methods=['GET'])
# def index():
#     user = session.get('user_info')
#     if not user:
#         return redirect('/login') #
#     return render_template('index.html', user_dict=USERS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=False)
