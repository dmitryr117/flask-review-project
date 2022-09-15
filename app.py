from core.config import Config
from core.app import create_app

if __name__ == '__main__':
    app = create_app(Config)
    app.run(debug=True)