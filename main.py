from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
   pass


@app.route('/promotion')
def promotion():
    pass


@app.route('/image_mars')
def mars():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
