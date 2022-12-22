from airport import Airport
from flight import Flight
import csv


class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []
        self.aeroport_code = []

    def import_airports(self, csv_file):
        with open("/fichier_doc/aeroports.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    airport = Airport(row[0], row[1], row[2], row[3])
                    self.airports.append(airport)
                    line_count += 1
        print(f'Processed {line_count} airports.')

    def import_flights(self, csv_file):
        with open("/fichier_doc/flights.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    flight = Flight(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    self.flights.append(flight)
                    line_count += 1
            print(f'Processed {line_count} flights.')
         #

           def airports(self) -> list[Airport]:
               return self.airports

                    airport_list = AirportList()
                    airport_list.airports(Airport("src_airport_code . ", "dst_code", "dst_airport_code"))
                    airport_list.airports(Airport(""))



    def airport_find(self, airport_code: str) -> Airport:
        for airport in self.airports:
            if airport.code == airport_code:
                print(f"${self.airport}")
            else:
                return None

    #  Vol direct entre deux aéroports

    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool:
        for flight in self.flights:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
                return False

        #  Recherche des vols et aéroports accessibles à partir d'une ville donné

    def flights_where(self, airport_code: str) -> list[Flight]:
        lv = ("")
        return lv

        # [flight for flight in self.flights if flight.src_code == airport_code or flight.dst_code == airport_code]

    def airports_from(self, airport_code: str) -> list[Airport]:
        return
        flights = self.flights_where(airport_code)
        airport_codes = {flight.dst_code for flight in flights}
        return
        [self.airport_find(code) for code in airport_codes]
