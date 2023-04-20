import os
from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route('/goup')
def goup():
    os.system('gpio -1 write 1 33')
    sleep(2.5)
    os.system('gpio -1 write 0 33')
    sleep(8)
    os.system('gpio -1 write 1 35')
    sleep(2.5)
    os.system('gpio -1 write 0 35')
    return 'ok'

if __name__ == '__main__':
    os.system('gpio -1 mode 33 out')
    os.system('gpio -1 mode 35 out')
    app.run('0.0.0.0', 5555)
