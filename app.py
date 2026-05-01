
from flask import Flask, request
import redis
import string
import random

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

@app.route('/')
def home():
    return "Hello babe "

@app.route('/shorten')
def shorten():
    url = request.args.get('url')
    code = generate_code()
    r.set(code, url)
    return f"Short URL: /{code}"

@app.route('/<code>')
def redirect_url(code):
    url = r.get(code)
    if url:
        return f"Original URL: {url.decode()}"
    return "Not found"

app.run(host='0.0.0.0', port=5001)
