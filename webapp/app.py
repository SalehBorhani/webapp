from flask import Flask, request, jsonify
import redis


app = Flask(__name__)

# Connect to the Redis server
client = redis.Redis(host='redis-master', port=6379)

@app.route('/set', methods=['POST'])
def set_data():
    data = request.get_json() 
    keys =[]
    values = []
    for key, value in data.items():
        keys.append(key)
        values.append(value)
    key_dict = str({keys[0]:values[0]})
    value_dict = str({keys[1]:values[1]})
    client.set(key_dict, value_dict)

    return jsonify({"Status":"OK"})

@app.route('/get', methods=['GET', 'POST'])
def get():
    data = request.get_json()
    return client.get(str(data))
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

