from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=["GET", "PUT"])
def get_time():
  if request.method == "GET":
    time = 0,
    running = '1\n',
    line = 'Recording stopped\n', 
    return {
        "time": time,
        "running": running,
        "line": line, 
        }
  elif request.method == "PUT":
    return {
        "time": 1000,
        "running": '0\n',
        "line": 'Recording\n', 
        }

if __name__ == '__main__':
    app.run(host="localhost", port=3001, debug=True)
