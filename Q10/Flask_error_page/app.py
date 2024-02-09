from flask import Flask, render_template

app = Flask(__name__)

# Route for handling 404 error (Page Not Found)
@app.route('/404')
def page_not_found():
    return render_template('404.html'), 404

# Route for handling 500 error (Internal Server Error)
@app.route('/500')
def internal_server_error():
    return render_template('500.html'), 500

# Example route
@app.route('/')
def index():
    # Example route, you can replace this with your actual routes
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
