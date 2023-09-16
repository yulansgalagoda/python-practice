# create dictionaries using an expression
# can replace for loops and certain lambda functions

# dictionary = {key: expression for (key/value) in iterable}

# temp_in_F = {
#     "New York": 32,
#     "Boston": 75,
#     "Los Angeles": 100,
#     "Chicago": 50
# }
# temp_in_C = {key: round((value-32)*(5/9)) for (key, value) in temp_in_F.items()}
# print(temp_in_C)


# dictionary = {key: expression for (key/value) in iterable if conditional}

# weather = {
#     "New York": "snowing",
#     "Boston": "sunny",
#     "Los Angeles": "sunny",
#     "Chicago": "cloudy"
# }
# sunny_cities = {key: value for (key, value) in weather.items() if value == "sunny"}
# all_cities = {key: value if value == "sunny" else "not sunny" for (key, value) in weather.items()}
#
# print(sunny_cities)
# print(all_cities)


weather = {
    "New York": 32,
    "Boston": 75,
    "Los Angeles": 100,
    "Chicago": 50
}


def check_temp(value):
    if value >= 70:
        return "Hot"
    else:
        return "Cold"


all_cities = {key: check_temp(value) for (key, value) in weather.items()}
print(all_cities)