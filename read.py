
#La liste des aéroports

#import flight_map
from airport import Airport
from flight import Flight
import csv

class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []

    # aeroports

with open("./fichier_doc/aeroports.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)
    read_airports = [row for row in reader]

print(read_airports)

# flights
with open("./fichier_doc/flights.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)
    read_flight = [row for row in reader]

print(read_flight)
