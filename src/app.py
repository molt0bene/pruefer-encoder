from flask import Flask, render_template, request
from interface.graph_decoder import GraphDecoder

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_code', methods=['POST'])
def get_code():
    data = request.form['decoder']

    try:
        data = list(map(int, data.split()))
        decoder = GraphDecoder(list(data))
        decoder.perform()
    except:
        return render_template("error.html")
    
    return render_template("success.html")

@app.route('/encode', methods=['POST'])
def encode():
    return render_template("encode.html")

app.run('0.0.0.0', 5050)
