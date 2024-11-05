from app import my_app

from utils.config import get


if __name__ == "__main__":
    my_app.run(port=get("FLASK_PORT"))