from flask import Flask, render_template

app = Flask(__name__)

my_list = ['this', 'is', 'a', 'list']


@app.route('/')
def index():
    name = 'Christian'
    some_variable = list(name)
    pup_dict={'Sammy': 'Doge'}
    return render_template('index.html',my_variable=my_list)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/senior')
def senior():
    return render_template('senior.html')\

@app.route('/racing')
def race():
    return render_template('race.html')


if __name__ == '__main__':
    app.run(debug=True)