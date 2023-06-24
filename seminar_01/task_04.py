from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/len/<text>')
def len_text(text):
    return f'{len(text) = }'


if __name__ == '__main__':
    app.run()
