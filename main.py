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
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
     <link rel="stylesheet"
     href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
     integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
     crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    <title>Привет, Марс!</title>
  <head>
  <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for("static", filename="img/image_mars.jpg")}" alt="нэ получилось" />
        <div class="alert alert-dark" role="alert">
            <h5>Человечество вырастает из детства.</h5>
        </div>
        
        <div class="alert alert-success" role="alert">
            <h5>Человечеству мала одна планета.</h5>
        </div>
        
        <div class="alert alert-secondary" role="alert">
            <h5>Мы сделаем обитаемыми безжизненные пока планеты.</h5>
        </div>
        
        <div class="alert alert-warning" role="alert">
            <h5>И начнем с Марса!</h5>
        </div>
        
        <div class="alert alert-danger" role="alert">
            <h5>Присоединяйся!</h5>
        </div>
  </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
