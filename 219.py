from flask import Flask, render_template, jsonify

app = Flask(__name__)

data = [
    {"id": 1, "name": "Alice"},
     {"id": 2, "name": "Bob"},

]

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/names')
def names():
    return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

app.run()