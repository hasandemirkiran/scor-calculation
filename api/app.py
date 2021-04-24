import sqlite3
from flask import g
from flask import Flask
import time

# DATABASE = '/path/to/database.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


# @app.route('/')
# def index():
#     cur = get_db().cursor()
#     ...



# def make_dicts(cursor, row):
# return dict((cursor.description[idx][0], value)
#             for idx, value in enumerate(row))

# db.row_factory = make_dicts

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}