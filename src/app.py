from flask import Flask, render_template, request
from threading import Thread
from interface.graph_decoder import GraphDecoder
from interface.graph_encoder_painter import GraphEncoderPainter

app = Flask(__name__)

def threaded(fn):
    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_code', methods=['POST'])
def get_code():
    data = request.form['decoder']

    try:
        data = list(map(int, data.split()))
    except:
        print('Something went wrong')
        return
    
    decoder = GraphDecoder(list(data))
    decoder.perform()
    return render_template("success.html")

@app.route('/encode', methods=['POST'])
def encode():
    graph_painter = GraphEncoderPainter()
    result = graph_painter.perform()
    print(result)
    return render_template("success.html")

app.run('0.0.0.0', 5050)
