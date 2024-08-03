from flask import Flask, render_template, jsonify
import threading
import receive_data

app = Flask(__name__)
data_list = receive_data.data_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_list)

if __name__ == '__main__':
    threading.Thread(target=receive_data.receive_data, daemon=True).start()
    app.run(debug=True, port=5001)
