def handClose():
  print('handClose')
  return

def handOpen():
  print('handOpen')
  return

def handStop():
  print('handStop')
  return


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

@app.route("/<action>/<option>", methods=['POST'])
def onPost(action, option):
  print("Handling action: /" + action + "/" + option)
  runnable = actions[action][option]
  target=runnable['function']
  args=runnable['arguments']
  threading.Thread(
    target=runnable['function'],
    args=runnable['arguments']).start()
  return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=False)
