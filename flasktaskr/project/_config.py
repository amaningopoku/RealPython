import os

# grab the folder where this script live
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "flasktaskr.db"
USERNAME = "admin"
PASSWORD = "admin"
WTF_CSRF_ENABLED = True
SECRET_KEY = "b'v\x82\x1d=\x9e\xd5d\xf2\xee\xa6\xa8.\x82\x02=\xd1 U\x02\xaa\x05\xff&\xaa\x17'"

# define the full path for the db
DATABASE_PATH = os.path.join(basedir, DATABASE)