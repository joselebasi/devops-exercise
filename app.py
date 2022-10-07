from warnings import catch_warnings
from flask import Flask,jsonify,request
import os
from redis import Redis

from multiprocessing import Value

app = Flask(__name__)

#redis = Redis(host=os.getenv('REDIS_HOST', 'redis-service'),
#              port=os.getenv('REDIS_PORT', 30001))

evhost = os.getenv('REDIS_HOST', 'redis')
evport = os.getenv('REDIS_PORT', 6379)
pod_name=os.getenv('MY_POD_NAME', 'pod-01')
developer=os.getenv('NAME_DEV', 'default value')
evpass = os.getenv('REDIS_PASS', 'a-very-complex-password-here')
redis = Redis(host='redis',
              port=6379,
              password='a-very-complex-password-here')

@app.route("/")
def hello():
    print("REDIS CONEXION")
    print("--------------")
    print("host:"+evhost)
    print("port:"+evport)
    print("pass:"+evpass)
    print("--------------")
    return {"path":"/","version":"1.15","pod-name":pod_name,"name-dev":developer}

@app.route('/getcounter',methods = ['POST', 'GET'])
def getcounter():    
    if request.method == 'POST':
        redis.incr('counter')        
        return {"method":"POST","status":"ok","pod-name":pod_name,"name-dev":developer}
    else:
        try:
            hits = int(redis.get('counter'))
        except:
            return {"method":"GET","error":"Connection to redis does not resolve","pod-name":pod_name,"name-dev":developer}  
    return {"method":"GET","count":hits,"pod-name":pod_name,"name-dev":developer}


@app.route('/restart',methods = ['POST'])
def setrestart():
    redis.set('counter',0)
    print("COUNTER RESTARTED")
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
