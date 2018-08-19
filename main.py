from flask import Flask, render_template

app = Flask(__name__)

my_list = ['this', 'is', 'a', 'list']


@app.route('/')
def index():
    name = 'Christian'
    some_variable = list(name)
    pup_dict={'Sammy': 'Doge'}
    return render_template('index.html',my_variable=my_list)


if __name__ == '__main__':
    app.run(debug=True)