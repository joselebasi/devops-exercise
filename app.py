from flask import Flask,jsonify
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is my test ABRAXAS!!!"

@app.route('/getcounter')
def getcounter():
    out = counter.value
    return jsonify(count=out)

@app.route("/postrequest", methods=["POST"])
def postrequest():
    with counter.get_lock():
        counter.value += 1
        out = counter.value
    return {"status":"Ok"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
