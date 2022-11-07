from TravelAgent import TravelAgent


def main():
    travel_agent = TravelAgent("Go Jaan")
    trip_info1 = travel_agent.set_trip_one_city_one_way(
        'DAC', 'PRA', '10/11/2022')
    # print('Aircraft', trip_info1.aircraft)
    # print('Price', trip_info1.price)

    trip_cities = ['DUB', 'LHR', 'SYD', 'JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_round(
        trip_cities, '19/10/2022')

    print("Price", trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)


if __name__ == "__main__":
    main()
