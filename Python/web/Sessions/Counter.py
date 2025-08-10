from flask import Flask, session
def index():
   """ При заходе на сайт обнуляем счётчик и даём ссылку на страницу с изменением счётчика """
   session['counter'] = 0
   return '<a href="/counter">Дальше</a>'


def counter():
   """ Увеличиваем счётчик и даём ссылку на страницу с изменением счётчика """
   session['counter'] += 1
   return '<h1>' + str(session['counter']) + '</h1>'
# Создаём объект веб-приложения:
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'VeryStrongKey'
app.add_url_rule('/', 'index', index)   # создаёт правило для URL '/':
                       # запускать функцию index и возвращать её значение.
app.add_url_rule('/counter', 'counter', counter) # создаёт правило для URL 'counter/'


if __name__ == '__main__':
   # Запускаем веб-сервер:
   app.run()