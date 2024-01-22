from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User Profile :{username}'

if __name__ =='__main__':
    app.run(debug=True)