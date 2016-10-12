import zmq
context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5680")

def handClose():
  print('handClose')
  socket.send_string("handClose")

def handOpen():
  print('handOpen')
  socket.send_string("handOpen")

def handStop():
  print('handStop')
  socket.send_string("handClose")

actions = {
  'hand' : {
    'close' : {
      'function' : handClose,
      'arguments' : ( )
    },
    'open' : {
      'function' : handOpen,
      'arguments' : ( )
    },
    'stop' : {
      'function' : handStop,
      'arguments' : ( )
    }
  }
}

import threading
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
  templateData = {
      'title' : "Bionic Hand"
  }
  return render_template('index.html', **templateData)

@app.route("/act/<action>/<option>", methods=['POST'])
def onPost(action, option):
  print("Handling action: /act/" + action + "/" + option)
  runnable = actions[action][option]
  target=runnable['function']
  args=runnable['arguments']
  threading.Thread(
    target=runnable['function'],
    args=runnable['arguments']).start()
  return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=False)
