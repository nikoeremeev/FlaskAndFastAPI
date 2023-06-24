from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b'8c2cc6271fbbd09c1adcde79cb82cfc0449dc2268ace3288a1450565da24ab13'
'''
Генерация секретного ключа
>>> import secrets
>>> secrets.token_hex()
'''


@app.route('/')
def index():
    return 'Hi'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=False)
