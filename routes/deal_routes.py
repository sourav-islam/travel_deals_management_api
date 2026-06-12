from flask import Blueprint, request, jsonify
from services.deal_service import DealService
from utils.validator import validate_deal

deal_bp = Blueprint("deals", __name__)


# -------------------------
# 1. CREATE DEAL
# -------------------------
@deal_bp.route("/", methods=["POST"])
def create_deal():

    data = request.get_json()

    # validation
    errors = validate_deal(data)
    if errors:
        return jsonify({"errors": errors}), 400

    deal = DealService.create_deal(data)

    return jsonify(deal.to_dict()), 201


# -------------------------
# 2. GET ALL DEALS
# -------------------------
@deal_bp.route("/", methods=["GET"])
def get_all_deals():

    deals = DealService.get_all_deals()

    return jsonify([
        deal.to_dict() for deal in deals
    ]), 200


# -------------------------
# 3. GET SINGLE DEAL
# -------------------------
@deal_bp.route("/<int:deal_id>", methods=["GET"])
def get_deal(deal_id):

    deal = DealService.get_deal_by_id(deal_id)

    if not deal:
        return jsonify({"message": "Deal not found"}), 404

    return jsonify(deal.to_dict()), 200