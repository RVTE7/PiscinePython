from re import X
import sys

def initDict():
  states = {
        "Oregon"    : "OR",
        "Alabama"   : "AL",
        "New Jersey": "NJ",
        "Colorado"  : "CO"
  }
  capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
  return states, capital_cities

def argToList(arg):
  a = arg.split(",")
  return a

def cleanArg(a):
  return [i.strip().title() for i in a if i.strip()], [i.strip() for i in a if i.strip()]

def search(d, c):

  states, capital_cities = initDict()
  
  for i in range(len(d)):
    if d[i] in states:
      print(capital_cities[states[d[i]]], " is the capital of ", d[i])
    elif d[i] in capital_cities.values():
      f = list(capital_cities.keys())[list(capital_cities.values()).index(d[i])]
      g = list(states.keys())[list(capital_cities.keys()).index(f)]
      print(d[i], " is the capital of ", g)
    else:
      print(c[i], " is neither a capital city nor a state")

if __name__ == '__main__':
  if len(sys.argv) == 2:
     a = argToList(sys.argv[1])
     b, c = cleanArg(a)
     search(b, c)