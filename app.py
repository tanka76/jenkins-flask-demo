from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From Flask App!'


@app.route('/home')
def home():
    return 'Welcome to Home Page!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)