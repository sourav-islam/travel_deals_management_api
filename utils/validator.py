ALLOWED_TRAVEL_TYPES = ["Budget", "Luxury", "Adventure", "Family"]


def validate_deal(data):
    errors = []

    # destination
    if not data.get("destination") or data["destination"].strip() == "":
        errors.append("destination cannot be empty")

    # price
    if "price" not in data or data["price"] <= 0:
        errors.append("price must be positive")

    # rating
    if "rating" not in data or not (1 <= data["rating"] <= 5):
        errors.append("rating must be between 1 and 5")

    # travel_type
    if data.get("travel_type") not in ALLOWED_TRAVEL_TYPES:
        errors.append("travel_type must be Budget, Luxury, Adventure, or Family")

    return errors