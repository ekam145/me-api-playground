from app.db import create_app
from app.routes import routes
from seed import seed_if_empty

app = create_app()

with app.app_context():
    seed_if_empty()

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run()

