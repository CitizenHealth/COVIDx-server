import os
from flask_cors import CORS
from flask import request
from app import create_app


# config_name = os.getenv("FLASK_CONFIG")
app = create_app("development")
whitelist = ['https://covidx.app', 'http://localhost:3000/', 'http://localhost:3001/']
CORS(app, resources={r'/*': {'origins': whitelist}})


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)