from app import app
from flask_frozen import Freezer

app.config['FREEZER_DESTINATION'] = './'
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
