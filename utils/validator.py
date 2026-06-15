ALLOWED_TRAVEL_TYPES = ["Budget", "Luxury", "Adventure", "Family"]

# Validation functions for travel deals
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

    # travel_type (Using case-insensitive check here too for safety)
    current_type = data.get("travel_type", "").strip().lower()
    allowed_lowercased = [t.lower() for t in ALLOWED_TRAVEL_TYPES]
    
    if current_type not in allowed_lowercased:
        errors.append("travel_type must be Budget, Luxury, Adventure, or Family")

    return errors

# Validation for search queries
def validate_search_query(
    destination,
    platform,
    travel_type
):
    """
    Validate incoming search parameters.

    Args:
        destination (str): The target location for the deal search.
        platform (str): The booking platform name to validate.
        travel_type (str): The category of travel to check.

    Returns:
        str: An error message string if validation fails, or None if valid.
    """

    if (
        not destination and
        not platform and
        not travel_type
    ):
        return (
            "At least one search "
            "parameter is required"
        )

    if travel_type:

        # Convert the allowed types list to lowercase for an accurate comparison
        allowed_lowercased = [
            t.lower()
            for t in ALLOWED_TRAVEL_TYPES
        ]

        if (
            travel_type.strip().lower()
            not in
            allowed_lowercased
        ):
            return (
                "Invalid travel type"
            )

    return None