from flask import request, Flask, url_for

app = Flask(__name__)


def main2():
    app.run()


@app.route('/form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                             <h1 class="text-center">Анкета претендента</h1>
                             <h3 class="text-center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" placeholder="Введите имя" name="name">
                                    <input class="form-control" placeholder="Введите фамилию" name="surname">
                                    <div class="form-group">
                            </div>
                                     <div>
                                        <form class="login_form" method="post">
                                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Неполное высшее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div>
                                        <br/>
                                        <label for="form-check">Какие у вас профессии?</label>
                                            <div class="form-check">
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Инженер-исследователь</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Инженер-строитель</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Пилот</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Метеоролог</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Инженер по жизнеобеспечению</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Инженер по радиоционной защите</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Врач</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Кибербиолог</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Квантовый физик</label>
                                            <br/>
                                            <input type="checkbox" class="form-check-input" name="accept">
                                            <label class="form-check-label">Программист</label>
                                    </div>
                                    <div>
                                        <br/>
                                        <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    main2()
