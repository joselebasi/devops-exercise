from warnings import catch_warnings
from flask import Flask,jsonify,request
import os
from redis import Redis

from multiprocessing import Value

redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'),
              port=os.getenv('REDIS_PORT', 6379))
app = Flask(__name__)

@app.route("/")
def hello():
    return {"path":"root","version":"1.4"}

@app.route('/getcounter',methods = ['POST', 'GET'])
def getcounter():
    if request.method == 'POST':
        redis.incr('counter')
        return {"status":"ok"}
    else:
        try:
            hits = int(redis.get('counter'))
        except:
            return jsonify(count=0)   
    return jsonify(count=hits)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
