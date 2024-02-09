from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('dashboard'))

    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username', 'Guest')
    return render_template('dashboard.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
