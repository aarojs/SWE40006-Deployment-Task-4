from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "SWE40006 Deployment Task 4 - This is a Flask app running inside a container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


