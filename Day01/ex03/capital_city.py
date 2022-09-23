import sys

def search_cap():

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

    if sys.argv[1] in states:
        x = states[sys.argv[1]]
    else:
        x = "Unknown state"

    def inner_search_cap():
        if x in  capital_cities:
            print(capital_cities[x])
        else:
            print("Unknown state")

    inner_search_cap()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        search_cap()
       

