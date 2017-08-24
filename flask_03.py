from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no parametro')
    param_two = request.args.get('params2', 'no parametro')
    return 'The parameter is : {}, {}' .format(param, param_two) 

if __name__ == '__main__':
    app.run( debug=True, host = '192.168.1.118', port=8000)
