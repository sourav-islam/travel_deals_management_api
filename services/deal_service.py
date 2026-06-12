from database.models import db, TravelDeal


class DealService:

    @staticmethod
    def create_deal(data):
        deal = TravelDeal(
            destination=data["destination"],
            price=data["price"],
            platform=data["platform"],
            rating=data["rating"],
            travel_type=data["travel_type"]
        )

        db.session.add(deal)
        db.session.commit()
        return deal

    @staticmethod
    def get_all_deals():
        return TravelDeal.query.all()

    @staticmethod
    def get_deal_by_id(deal_id):
        return TravelDeal.query.get(deal_id)