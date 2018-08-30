from flask import Flask, render_template, send_file, redirect, url_for

app = Flask(__name__)


my_list = []

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

@app.route('/resume')
def resume():
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/pdf')
def pdf():
    file_name = 'res.pdf'
    return redirect(url_for('static', filename='/'.join(['pdfs', file_name])), code=301)


if __name__ == '__main__':
    app.run(debug=True)