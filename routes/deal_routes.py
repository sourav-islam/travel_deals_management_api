import logging
from http import HTTPStatus
from flask import Blueprint,request, jsonify
from services.deal_service import DealService
from utils.validator import validate_deal, validate_search_query

deal_bp = Blueprint("deals", __name__)
logger = logging.getLogger(
    __name__
)

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



# -------------------------
# 4. SEARCH DEALS
# -------------------------
@deal_bp.route(
    "/search",
    methods=["GET"]
)
def search_deals():
    """
    Search for travel deals based on query filters.

    Args:
        destination (str, optional): The destination location to filter by.
        platform (str, optional): The booking platform utilized for the search.
        travel_type (str, optional): The specific category of travel being searched.

    Returns:
        tuple: A JSON payload of matching deals or an error message alongside an HTTP status code.
    """


    destination = request.args.get(
        "destination"
    )

    platform = request.args.get(
        "platform"
    )

    travel_type = request.args.get(
        "travel_type"
    )

    validation_error = (
        validate_search_query(
            destination,
            platform,
            travel_type
        )
    )

    if validation_error:

        logger.warning(
            f"Invalid search request: "
            f"{validation_error}"
        )

        return (
            jsonify(
                {
                    "message":
                    validation_error
                }
            ),
            HTTPStatus.BAD_REQUEST
        )

    logger.info(
        "Search request received"
    )

    deals = (
        DealService.search_deals(
            destination,
            platform,
            travel_type
        )
    )

    return (
        jsonify(
            [
                deal.to_dict()
                for deal in deals
            ]
        ),
        HTTPStatus.OK
    )