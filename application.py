import os
from flask_cors import CORS
from app import create_app


# config_name = os.getenv("FLASK_CONFIG")
application = create_app("production")
CORS(application)

if __name__ == "__main__":
    from waitress import serve
    serve(application, host="0.0.0.0", port=8080)