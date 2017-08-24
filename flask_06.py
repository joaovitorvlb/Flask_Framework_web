from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='my_name'):
    age = 21
    my_list = [1, 2, 3, 4]
    return render_template('user.html', nome=name, age=age, list=my_list)

if __name__ == '__main__':
    app.run( debug=True, host = '192.168.1.118', port=8000)
