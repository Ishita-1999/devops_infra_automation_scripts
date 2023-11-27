from flask import Flask, request, jsonify

app = Flask(__name__)
key_value_store = {}

@app.route('/get/<key>', methods=['GET'])
def get_key(key):
    value = key_value_store.get(key)
    if value is not None:
        return jsonify({key: value})
    else:
        return jsonify({"error": "Key not found"}), 404

@app.route('/set', methods=['POST'])
def set_key():
    data = request.get_json()
    if 'key' in data and 'value' in data:
        key = data['key']
        value = data['value']
        key_value_store[key] = value
        return jsonify({"message": "Key-value pair set successfully"})
    else:
        return jsonify({"error": "Invalid request data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
