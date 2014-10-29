import os
from flask import Flask, render_template
from flask.ext.cake import Cake

app = Flask(__name__, template_folder='./')
cake = Cake(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
