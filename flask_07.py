from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'my_name'
    return render_template('index.html', nome=name)

@app.route('/client')
def client():
    list_name = ['Test1', 'Test2', 'Test3']
    return render_template('client.html', list=list_name)

if __name__ == '__main__':
    app.run( debug=True, host = '192.168.1.118', port=8000)
