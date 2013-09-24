from flask import Flask, Request, Response, render_template

application = app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cosas/')
def cosas():
    return "Cosas"

if __name__ == '__main__':
    app.run()