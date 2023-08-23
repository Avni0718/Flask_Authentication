from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Data: List of colors
colors = ['red', 'blue', 'green', 'yellow']

# Example dictionary of API keys (replace with your actual keys)
api_keys = {
    'Avni': 'Pyramid@123',
    'key2': 'Flask'
}

@auth.verify_password
def verify_api_key(username, password):
    if username in api_keys and password == api_keys[username]:
        return username

@app.route('/get_colors', methods=['GET'])
@auth.login_required
def get_colors():
    return jsonify(colors)

if __name__ == '__main__':
    app.run(debug=True)
