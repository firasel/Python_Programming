class Trip:
    def __init__(self, trip_cities,  start_date, aircraft, price, route="") -> None:
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft = None
        self.trip_route = route
        self.price = price
        self.aircraft = aircraft

    def __repr__(self) -> str:
        return f'Trip: {self.trip_cities} Aircraft: {self.aircraft} Route: {self.trip_route} Price: {self.price}'
