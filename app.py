from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'



@app.route('/login')
def hello():
    return 'login is working'

# new funct
@app.route('/login2')
def hello():
    return 'login2 is working'

@app.route('/register')
def hello():
    return 'register is working'

@app.route('/register2')
def hello():
    return 'register2 is working'

if __name__ == '__main__':
    app.run(debug=True)
