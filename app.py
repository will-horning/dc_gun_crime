import os
from flask import Flask, render_template
from flask.ext.cake import Cake
from flaskext.markdown import Markdown
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
cake = Cake(app)
assets = Environment(app)

js = Bundle(
    'js/lib/prism.js',
    'js/lib/jquery.min.js',
    'js/lib/leaflet.js',
    'js/lib/jquery-ui-1.10.0.custom.min.js',
    'js/lib/jquery-ui-timepicker-addon.js',
    'js/lib/jQDateRangeSlider-min.js',
    'js/lib/main.js',
    filters='jsmin',
    output='js/lib/bundle.%(version)s.js'
)

css = Bundle(
    'css/stylesheet.css',
    'css/prism.css',
    'css/jquery-ui-1.10.0.custom.min.css',
    'css/leaflet.css',
    'css/iThing.css',
    filters='cssmin',
    output='css/bundle.%(version)s.css'
)

assets.register('js_all', js)
assets.register('css_all', css)

@app.route('/', methods=['GET'])
def index():
    with open('./index.html', 'w') as f:
        f.write(render_template('index.html'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
