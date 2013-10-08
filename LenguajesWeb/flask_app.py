from flask import Flask, request, render_template
from apps.Matches import get_re_matches
from apps.AFND import create_AFND
from apps.Global import *
from apps.Thompson import *

application = app = Flask(__name__)
app.config["DEBUG"] = True

def get_simbols(states):
    simbols = []
    for s in states:
        for k in s.transitions.keys():
            if not k in simbols:
                simbols.append(k)
    return simbols


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    e = request.form['error']
    return render_template('error',e=e)

@app.route('/tables', methods=['POST'])
def cosas():
    re = request.form['regex']
    text = request.form['text']
    try:
        State.id = 0
        afnd = create_AFND(re)
        states = sorted(afnd.values(), key = lambda s: int(s.name) if s.name != 's' and s.name != 'f' else -1)
        simbols = get_simbols(states)
        #simbols.append(Global.epsilon)
        found = get_re_matches(afnd, text)
        return render_template('tabla.html',found=found, simbols=simbols, states=states, re=re)
    except Exception, e:
        return render_template('error.html',e=e)

if __name__ == '__main__':
    app.run()
