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
                                            <input id="check_1" type="checkbox" class="form-check-input" name="eng_1">
                                            <label class="form-check-label" for="check_1">Инженер-исследователь</label>
                                            <br/>
                                            <input id="check_2" type="checkbox" class="form-check-input" name="eng_2">
                                            <label class="form-check-label" for="check_2">Инженер-строитель</label>
                                            <br/>
                                            <input id="check_3" type="checkbox" class="form-check-input" name="pilot">
                                            <label class="form-check-label" for="check_3">Пилот</label>
                                            <br/>
                                            <input id="check_4" type="checkbox" class="form-check-input" name="meteo">
                                            <label class="form-check-label" for="check_4">Метеоролог</label>
                                            <br/>
                                            <input id="check_5" type="checkbox" class="form-check-input" name="eng_3">
                                            <label class="form-check-label" for="check_5">Инженер по жизнеобеспечению</label>
                                            <br/>
                                            <input id="check_6" type="checkbox" class="form-check-input" name="eng_4">
                                            <label class="form-check-label" for="check_6">Инженер по радиоционной защите</label>
                                            <br/>
                                            <input id="check_7" type="checkbox" class="form-check-input" name="doctor">
                                            <label class="form-check-label" for="check_7">Врач</label>
                                            <br/>
                                            <input id="check_8" type="checkbox" class="form-check-input" name="biolog">
                                            <label class="form-check-label" for="check_8">Кибербиолог</label>
                                            <br/>
                                            <input id="check_9" type="checkbox" class="form-check-input" name="phys">
                                            <label class="form-check-label" for="check_9">Квантовый физик</label>
                                            <br/>
                                            <input id="check_10" type="checkbox" class="form-check-input" name="prog">
                                            <label class="form-check-label" for="check_10">Программист</label>
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
                                    <form method="post" enctype="multipart/form-data">
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
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['eng_1'])
        print(request.form['eng_2'])
        print(request.form['eng_3'])
        print(request.form['eng_4'])
        print(request.form['pilot'])
        print(request.form['doctor'])
        print(request.form['phys'])
        print(request.form['prog'])
        print(request.form['meteo'])
        print(request.form['biolog'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    main2()
