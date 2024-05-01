from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/info')
def information():
    return 'Сегодня отличная погода!'

@app.route('/world')
def surrounding_world():
    return '''Россия - это огромная страна с богатейшей природой, которая поражает своей красотой и мощью. 
              <br>От бескрайних лесов до высоких гор, от прекрасных рек до безбрежных степей - 
              Россия предлагает множество вариантов для любителей природы.'''

if __name__ == '__main__':
    app.run()
    