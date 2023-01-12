from All_Airports import all_airports
from Air_Lines import air_lines
from Trip import trip
from itertools import permutations


class travel_agent:
    def __init__(self, name):
        self.name = name
        self.trips = None
        self.allairports = all_airports()
        self.airlines = air_lines()

    def set_trip_one_city_one_way(self, start, end, date):
        """
        :param start:
        :param end:
        :param date:
        :return: aircraft, price

        notes : use airlines to select aircraft
        """
        price = self.allairports.ticket_price(start, end)
        distance = self.allairports.distance_between_two_airport(start, end)
        # print(distance)
        aircraft = self.airlines.get_aircraft_by_distance(distance)
        trp = trip([start, end], aircraft, price, date, [start, end])
        return trp

    def set_trip_one_city_round_way(self, start, end, start_date, ):
        ftrip = self.set_trip_one_city_one_way(start, end, start_date)
        rtrip = self.set_trip_one_city_one_way(end, start, start_date)
        return [ftrip, rtrip]

    def set_trip_two_city_one_way(self, trip_cities, start_date, ):
        trip1 = self.set_trip_one_city_one_way(trip_cities[0], trip_cities[1], start_date)
        trip2 = self.set_trip_one_city_one_way(trip_cities[1], trip_cities[2], start_date)
        return [trip1, trip2]

    def set_trip_multi_city_one_way_fixed_route(self, trip_cities, start_date):
        trip_list = []
        for i in range(len(trip_cities) - 1):
            trp = self.set_trip_one_city_one_way(trip_cities[i], trip_cities[i + 1], start_date)
            trip_list.append(trp)
        return trip_list

    def set_trip_multi_city_flexible_route(self, trip_cities, start_date):
        my_city = trip_cities[0]
        flexible_cities = trip_cities[1:]

        min_cost = float('inf')
        selected_trip = None
        for sequence in permutations(flexible_cities):
            fixed_route = [my_city] + list(sequence)
            fixed_route_trips = self.set_trip_multi_city_one_way_fixed_route(fixed_route, start_date)
            price = 0
            for trp in fixed_route_trips:
                price += trp.cost
            if price < min_cost:
                min_cost = price
                selected_trip = fixed_route_trips
        return selected_trip, min_cost

    def __repr__(self):
        return f'Travel_agent : {self.name}'


if __name__ == '__main__':
    T_agent = travel_agent('FLY BIMAN')
    trp_cities = ['DUB', 'LHR', 'SYD', 'JFK', 'ORD']
    trip_info_2 = T_agent.set_trip_multi_city_flexible_route(trp_cities, '12/10/2025')

    print(trip_info_2[1])
    for trp in trip_info_2[0]:
        print(trp)
