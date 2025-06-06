import os
from flask import  Flask, jsonify

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/api')
def get_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = f.read()
            return jsonify(eval(data))
    except FileNotFoundError:
        return jsonify({"error:" "Data File not founs."}), 404
    except Exception as e:
        return jsonify({"error:" f"An error occured: {str(e)}"}), 500
    
if __name__ == '__main__':
    app.run(debug=True)