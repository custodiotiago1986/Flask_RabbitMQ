from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)
process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_sending():
    global process
    if process is None:
        process = subprocess.Popen(['python', 'send_data.py'])
    return 'Sending started'

@app.route('/stop', methods=['POST'])
def stop_sending():
    global process
    if process is not None:
        process.terminate()
        process = None
    return 'Sending stopped'

if __name__ == '__main__':
    app.run(debug=True)
