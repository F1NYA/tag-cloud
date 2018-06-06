from waitress import serve
from flask_app.app import app
import os

if __name__ == '__main__':
    serve(app, host=os.environ.get("HOST", "localhost"), port=os.environ.get("PORT", 4000), expose_tracebacks=True)

