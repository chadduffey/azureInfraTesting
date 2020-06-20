import random

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "We're up!\n"

# Returns a random bad password from the Daniel Miessler maintianed SecLists repository:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/darkweb2017-top1000.txt
@app.route('/password', methods=['GET'])
def password():
    lines = open('pwds.txt').read().splitlines() 
    return random.choice(lines) + "\n"

if __name__ == '__main__':
    app.run(debug=True)