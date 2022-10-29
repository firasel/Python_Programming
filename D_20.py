class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))
        newSeat = [[True for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = newSeat

    def book_seats(self, cs_name, cs_phone, id, seat_list):
        self.cs_name = cs_name
        self.cs_phone = cs_phone
        print(self.seats[id])
        for item in seat_list:
            if self.seats[id][item[0]][item[1]] == True:
                self.seats[id][item[0]][item[1]] = False
            else:
                print(
                    f'Row {item[0]}, Col {item[1]} this seat is not available')


hall1 = Hall(3, 2, 1)
hall2 = Hall(15, 10, 2)
hall3 = Hall(5, 15, 3)

hall1.entry_show("1", "Mr. Robot", "22 Oct 2022, 08:00 pm")
# hall1.entry_show(2, "Mr. Robot 2", "23 Oct 2022, 07:00 pm")
hall1.book_seats("Mr. Abc", "01236547845", "1", [
                 (0, 0), (0, 1), (2, 0), (2, 1)])

print(hall1.__dict__)

# print(hall1.hall_list)
# print()
# print(hall3.hall_list)
