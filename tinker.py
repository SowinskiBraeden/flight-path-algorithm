#! python

airports = [
  "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
  "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"
]

# List of one way flights
routes = [
  ("DSM", "ORD"),
  ("ORD", "BIG"),
  ("BIG", "LGA"),
  ("SIN", "CDG"),
  ("CDG", "SIN"),
  ("CDG", "BUD"),
  ("DEL", "DOH"),
  ("DEL", "CDG"),
  ("TLV", "DEL"),
  ("EWR", "HND"),
  ("HND", "ICN"),
  ("HND", "JFK"),
  ("ICN", "JFK"),
  ("JFK", "LGA"),
  ("EYW", "LHR"),
  ("LHR", "SFO"),
  ("SFO", "SAN"),
  ("SFO", "DSM"),
  ("SAN", "EYW")
]

starting = "LGA"

# Determine the minimum number of routes to use
# that enables any passenger to go from 'LGA' to
# any other airport.

def calculateMinFlightPath() -> int:
  return 0

if __name__ == '__main__':
  # Answer is 3 for this set of airports
  numberOfRoutes = calculateMinFlightPath()
  print(f"The solution {numberOfRoutes} is {'correct' if numberOfRoutes == 3 else 'incorrect'}")
