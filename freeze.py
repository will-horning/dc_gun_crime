import shutil
from app import app
from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
	freezer.freeze()
	shutil.copy2('./build/index.html', './index.html')
	shutil.copy2('./build/static/bundle.js', './static/bundle.js')
	shutil.copy2('./build/static/bundle.css', './static/bundle.css')