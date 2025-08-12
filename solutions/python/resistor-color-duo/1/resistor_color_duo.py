def value(colors):
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    first_two = colors[:2]

    return int((str(color_codes[first_two[0]])) + str(color_codes[first_two[1]]))
