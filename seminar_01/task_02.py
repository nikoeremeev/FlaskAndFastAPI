from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'Обо мне'


@app.route('/contact/')
def contact():
    return 'Контакты'


if __name__ == '__main__':
    app.run()
