import random
import requests

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "We're up!\n"

# Returns a random bad password from the Daniel Miessler maintianed SecLists repository:
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/darkweb2017-top1000.txt
@app.route('/password', methods=['GET'])
def password():
    source = "https://passwordfunctionexample.blob.core.windows.net/data/pwds.txt?sv=2019-02-02&st=2020-06-24T13%3A27%3A01Z&se=2030-01-01T16%3A00%3A00Z&sr=b&sp=r&sig=7vQ9lzdataV60EpalaXeRGV6mNtzBOCZDCGWG3mjF1Y%3D"
    response = requests.get(source)
    data = response.text
    lines = data.splitlines() 
    return random.choice(lines) + "\n"

if __name__ == '__main__':
    app.run(debug=True)