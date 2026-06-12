import os
from flask import Flask
from dotenv import load_dotenv
from database.models import db
from routes.deal_routes import deal_bp

load_dotenv()


def create_app():
    app = Flask(__name__)
    
    # DB config
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # init DB
    db.init_app(app)

    # register routes
    app.register_blueprint(deal_bp, url_prefix="/deals")

    @app.route("/")
    def home():
        return {"message": "Travel Deal API Running"}

    # create tables
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)