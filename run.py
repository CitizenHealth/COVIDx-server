import os
from flask_cors import CORS
from app import create_app


config_name = os.getenv("FLASK_CONFIG")
app = create_app(config_name)
CORS(app)

if __name__ == "__main__":
    app.run()