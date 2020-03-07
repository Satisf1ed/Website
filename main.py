from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    list_prom = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                 'Присоединяйся!'
                 ]

    return '<br/>'.join(list_prom)


@app.route('/image_mars')
def mars():
    return f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    <title>Привет, Марс!</title>
  <head>
  <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for("static", filename="img/image_mars.jpg")}" alt="нэ получилось" />
    <br/>Вот она какая, красная планета.
  </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
