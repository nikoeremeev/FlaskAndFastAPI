from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/html/')
def get_html():
    students = [{"first_name": "Ivan0", "last_name": "Ivanov0", "age": 31, "average_score": 4.3},
                {"first_name": "Ivan1", "last_name": "Ivanov1", "age": 25, "average_score": 4.9},
                {"first_name": "Ivan2", "last_name": "Ivanov2", "age": 45, "average_score": 4.0},
                {"first_name": "Ivan3", "last_name": "Ivanov3", "age": 18, "average_score": 3.9}
                ]
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run()
