from warnings import catch_warnings
from flask import Flask,jsonify,request
import os
from redis import Redis

from multiprocessing import Value

#redis = Redis(host=os.getenv('REDIS_HOST', 'redis-service'),
#              port=os.getenv('REDIS_PORT', 30001))
redis = Redis(host=os.getenv('REDIS_HOST', 'redis'),
              port=os.getenv('REDIS_PORT', 6379),
              password='a-very-complex-password-here')
app = Flask(__name__)
pod_name=os.getenv('MY_POD_NAME', 'pod-01')

@app.route("/")
def hello():
    return {"path":"/","version":"1.8","pod-name":pod_name}

@app.route('/getcounter',methods = ['POST', 'GET'])
def getcounter():
    
    if request.method == 'POST':
        redis.incr('counter')        
        return {"method":"POST","status":"ok","pod-name":pod_name}
    else:
        try:
            hits = int(redis.get('counter'))
        except:
            return {"method":"GET","count":"0","pod-name":pod_name}  
    return {"method":"GET","count":hits,"pod-name":pod_name}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
