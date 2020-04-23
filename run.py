import os
from flask_cors import CORS
from flask import request
from app import create_app


# config_name = os.getenv("FLASK_CONFIG")
app = create_app("development")
CORS(app)

# white = ['https://covidx.app', 'http://localhost:3000/']
# @app.after_request
# def add_cors_headers(response):
#     r = request.referrer[:-1]
#     if r in white:
#         response.headers.add('Access-Control-Allow-Origin', r)
#         response.headers.add('Access-Control-Allow-Credentials', 'true')
#         response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#         response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
#         response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
#         response.headers.add('Access-Control-Allow-Headers', 'Authorization')
#         response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
#     return response



if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)