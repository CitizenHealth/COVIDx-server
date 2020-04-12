import os
import sys


os.environ['FLASK_CONFIG'] = 'production'
os.environ['SECRET_KEY'] = 'bdc7a4581f8195e3e3bfbe1df5dc5a0de401b5a912e8e86a'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:^zT_UIsJ5Au1(v6e@aa19bixxzoxyunw.cxnedy40wg8c.us-west-2.rds.amazonaws.com/covidx_db'


from run import app as application