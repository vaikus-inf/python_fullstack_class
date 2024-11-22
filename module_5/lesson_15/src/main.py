from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', hello='Hello, world!')

@app.route('/logo/<string:name>/<string:surname>/<int:age>')
def person(name, surname, age):
    return render_template('user.html', name=name, surname=surname, age=age, title='Данные пользователя')

if __name__ == '__main__':
    app.run()