import csv
from Aircraft import aircraft


class air_lines:
    def __init__(self):
        self.air_crafts = None
        self.load_air_crafts_data('./Data/aircraft.csv')

    def load_air_crafts_data(self, csv_file):
        aircrafts = {}
        with open(csv_file, 'r') as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                aircrafts[line[0]] = aircraft(line[3], line[0], line[1], line[4])

        file.close()
        self.air_crafts = aircrafts
        # for arc in aircrafts.items():
        #     print(arc)

    def get_aircraft(self, aircraft_code):
        return self.air_crafts[aircraft_code]

    def get_aircraft_by_distance(self, distance):
        for air_craft in self.air_crafts.values():
            if air_craft.flight_range < distance:  # Logic ta gojamil mone hoise
                return air_craft


air_lines()
