from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

class UserForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        return render_template('result.html', username=username)

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
