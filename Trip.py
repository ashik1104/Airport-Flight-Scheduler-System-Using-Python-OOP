class trip:
    def __init__(self, trip_cities, aircraft, cost, start_date, route=''):
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft_typ = aircraft
        self.trip_route = route
        self.cost = cost

    def __repr__(self):
        # return f'Trip: {self.trip_cities} Aircraft: {self.aircraft_typ} route: {self.trip_route} cost: {self.cost}'
        return f'Trip: {self.trip_cities} cost: {self.cost}'
