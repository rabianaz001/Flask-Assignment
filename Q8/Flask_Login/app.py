from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Flask-Login

login_manager = LoginManager()
login_manager.init_app(app)

# Mock user database (replace with your database ORM)
class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = generate_password_hash(password)

users = {'user1': User('user1', 'password1')}

# User loader function
@login_manager.user_loader
def load_user(username):
    return users.get(username)

# Routes
@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user(User)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
