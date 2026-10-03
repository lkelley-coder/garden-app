def get_season_advice(season):
    """Return gardening advice based on the given season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the given plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Ask the user for input and print personalised gardening advice."""
    season = input("Enter the season (e.g. summer, winter): ").lower()
    plant_type = input("Enter the plant type (e.g. flower, vegetable): ").lower()

    advice = get_season_advice(season) + get_plant_advice(plant_type)
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
