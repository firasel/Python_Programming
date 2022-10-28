class Star_Cinema:
    hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self, self)

    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))
        seats = []
        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                temp.append(False)
            seats.append(temp)
        self.seats[id] = seats


hall1 = Hall(3, 2, 1)
hall2 = Hall(15, 10, 2)
hall3 = Hall(5, 15, 3)

hall1.entry_show(1, "Mr. Robot", "22 Oct 2022, 08:00 pm")
hall1.entry_show(2, "Mr. Robot 2", "23 Oct 2022, 07:00 pm")

print(hall1.__dict__)

print(hall1.hall_list)
print()
print(hall3.hall_list)
