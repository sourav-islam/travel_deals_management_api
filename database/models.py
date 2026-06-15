from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TravelDeal(db.Model):
    """
    deals table model
    """


    __tablename__ = "deals"

    id = db.Column(db.Integer, primary_key=True)

    destination = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    travel_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """
        Convert model object to dictionary
        """


        return {
            "id": self.id,
            "destination": self.destination,
            "price": self.price,
            "platform": self.platform,
            "rating": self.rating,
            "travel_type": self.travel_type
        }