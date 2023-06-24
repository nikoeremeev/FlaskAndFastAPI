from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1: int, num2: int):
    return f'{num1 + num2}'


if __name__ == '__main__':
    app.run()
