import sys

def state():

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    for key , value in capital_cities.items():
        if value == sys.argv[1]:
            for k, v in states.items():
                if v == key:
                    print(k)
                    return
    else:
        print("Unknown capital city")
        return

if __name__ == "__main__":
    if len(sys.argv) == 2:
        state(sys.argv[1])