import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/news/')
def get_news():
    news = [
        {"title": "Заголовок 1", "text": "lorem10", "date": datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")},
        {"title": "Заголовок 2", "text": "lorem20", "date": datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")},
        {"title": "Заголовок 3", "text": "lorem30", "date": datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")}
    ]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run()
