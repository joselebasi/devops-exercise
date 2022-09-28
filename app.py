from warnings import catch_warnings
from flask import Flask,jsonify,request
import os
from redis import Redis

from multiprocessing import Value

#redis = Redis(host=os.getenv('REDIS_HOST', 'redis-service'),
#              port=os.getenv('REDIS_PORT', 30001))
redis = Redis(host=os.getenv('REDIS_HOST', 'redis-master'),
              port=os.getenv('REDIS_PORT', 6379))
app = Flask(__name__)

@app.route("/")
def hello():
    return {"path":"root","version":"1.6"}

@app.route('/getcounter',methods = ['POST', 'GET'])
def getcounter():
    if request.method == 'POST':
        redis.incr('counter')
        return {"method":"POST","status":"ok"}
    else:
        try:
            hits = int(redis.get('counter'))
        except:
            return {"method":"GET","count":"0"}  
    return {"method":"GET","count":hits}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
