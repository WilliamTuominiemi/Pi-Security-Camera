import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/right', methods=['GET'])
def right():
    print('right')
    return "<h1>RIGHT</p>"


@app.route('/left', methods=['GET'])
def left():
    print('left')
    return "<h1>LEFT</p>"


app.run()
