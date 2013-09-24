from flask import Flask, request, render_template
from apps.Matches import get_re_matches

application = app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    e = request.form['error']
    return render_template('error',e)

@app.route('/cosas', methods=['POST'])
def cosas():
    re = request.form['regex']
    text = request.form['text']
    found = get_re_matches(re, text)
    return render_template('tabla.html',found=found)

if __name__ == '__main__':
    app.run()