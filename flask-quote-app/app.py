import os
import random
from flask import Flask

app = Flask(__name__)

QUOTES = [
    "\"Make it work, make it right, make it fast.\" - Kent Beck",
    "\"The only way to go fast is to go well.\" - Robert C. Martin",
    "\"Continuous improvement is better than delayed perfection.\" - Mark Twain",
    "\"If it hurts, do it more often.\" - Martin Fowler",
    "\"Simplicity is prerequisite for reliability.\" - Edsger Dijkstra",
    "\"First, solve the problem. Then, write the code.\" - John Johnson",
    "\"Automate everything that can be automated.\" - DevOps principle",
    "\"Software is never finished, only released.\" - common engineering saying",
    "\"If it's not automated, it's not really deployed.\"",
    "\"Deploy small, deploy often, roll back quickly.\"",
]

@app.route('/')
def home():
    app_env = os.environ.get('APP_ENV', 'development')
    quote = random.choice(QUOTES)
    return f"[{app_env.upper()}] Software Deployment quote of the day: {quote}"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)