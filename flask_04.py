from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name = 'nama is default', num = 'nums is default'):
    return 'The parameter is : {} {}' .format(name, num) 

if __name__ == '__main__':
    app.run( debug=True, host = '192.168.1.118', port=8000)
