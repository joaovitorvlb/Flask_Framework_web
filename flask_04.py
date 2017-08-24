from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/params/<name>')
def params(name):
    return 'The parameter is : {}' .format(name) 

if __name__ == '__main__':
    app.run( debug=True, host = '192.168.1.118', port=8000)
