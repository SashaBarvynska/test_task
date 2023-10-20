from flask import Flask
from src.app import create_app

from config import Config


if __name__ == "__main__":
    app: Flask = create_app(Config)
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
