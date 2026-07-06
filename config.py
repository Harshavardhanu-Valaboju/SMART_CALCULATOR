import os

class Config:

    SECRET_KEY = "smart_vision_calculator"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    DEBUG = True