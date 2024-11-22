from flask import Flask, render_template
from auth import AuthForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'logomachine_hello_world'

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth_user():
    form = AuthForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template('auth.html', form=form, title='Авторизация')

if __name__ == '__main__':
    app.run()