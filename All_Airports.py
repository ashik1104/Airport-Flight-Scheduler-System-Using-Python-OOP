import csv
from Airport import airport
import math


class all_airports:
    def __init__(self):
        self.ALLairports = None
        self.load_airport_data('./Data/airport.csv')

    def load_airport_data(self, file_path):
        airports = {}
        currency_rate = {}
        country_currency = {}

        #  relation between currency name and rate
        with open('./Data/currencyrates.csv', 'r') as file1:
            lines = csv.reader(file1)
            for line in lines:
                currency_rate[line[1]] = line[2]
        file1.close()

        #  relation between country name and currency name
        with open('./Data/countrycurrency.csv', 'r') as file2:
            lines = csv.reader(file2)
            next(lines)
            for line in lines:
                country_currency[line[0]] = line[1]
        file2.close()

        #  create airport
        with open(file_path, 'r', encoding="utf8") as file3:
            lines = csv.reader(file3)

            try:
                for line in lines:
                    country = line[3]
                    if country not in country_currency:
                        continue
                    currency = country_currency[country]
                    if currency not in currency_rate:
                        continue
                    rate = currency_rate[currency]
                    airports[line[4]] = airport(line[4], line[1], line[2], line[3], line[6], line[7], rate)
            except KeyError as e:
                # print('key not found', e)
                pass
            self.Allairports = airports
            # for airp in airports.items():
            #     print(airp)
        file3.close()

    def get_distance_between_two_airports(self, lat1, lon1, lat2, lon2):
        radius = 6371
        lat_dif = math.radians(lat1 - lat2)
        lon_dif = math.radians(lon1 - lon2)
        a = (math.sin(lat_dif / 2) * math.sin(lat_dif / 2) + math.cos(math.radians(lat1)) * math.cos(
            math.radians(lat2)) * math.sin(lon_dif / 2) * math.sin(lon_dif / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c
        return distance

    def distance_between_two_airport(self, airport1_code, airport2_code):
        airport_1 = self.Allairports[airport1_code]
        airport_2 = self.Allairports[airport2_code]
        distance = self.get_distance_between_two_airports(airport_1.lat, airport_1.lon, airport_2.lat, airport_2.lon)
        return distance

    def ticket_price(self, start, end):
        distance = self.distance_between_two_airport(start, end)
        airport1 = self.Allairports[start]
        fare = distance * airport1.rate
        return fare


if __name__ == '__main__':
    world_tour = all_airports()
    fare = world_tour.ticket_price('DAC', 'PRA')
    print('ticket fare', fare)
