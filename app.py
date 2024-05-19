from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'login is working'

@app.route('/login2')
def login2():
    return 'login2 is working'

@app.route('/new-login')
def new_login():
    return 'this is new login'

@app.route('/register')
def register():
    return 'register is working'


if __name__ == '__main__':
    app.run(debug=True)
