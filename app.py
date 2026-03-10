from flask import Flask, jsonify, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-password')
def get_password():
    # Gets the length from the URL, defaults to 12 if not provided
    pw_length = request.args.get('length', default=12, type=int)
    return jsonify({"password": generate_password(pw_length)})

if __name__ == '__main__':
    app.run(debug=True)