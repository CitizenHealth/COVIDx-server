import os
import sys
# from flask_cors import CORS
# from app import create_app


# config_name = os.getenv("FLASK_CONFIG")
# application = create_app("production")
# CORS(application)

# if __name__ == "__main__":
#     from waitress import serve
#     serve(application, host="0.0.0.0", port=8080)



os.environ['FLASK_CONFIG'] = 'production'
os.environ['SECRET_KEY'] = 'bdc7a4581f8195e3e3bfbe1df5dc5a0de401b5a912e8e86a'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:^zT_UIsJ5Au1(v6e@aa19bixxzoxyunw.cxnedy40wg8c.us-west-2.rds.amazonaws.com/covidx_db'

from run import app as application