from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello World!</h1>"


@app.route('/home')
def home():
    return "<h1>Home Page</h1>"


@app.route('/about')
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5001)
