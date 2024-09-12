
class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self.show_list = []
        self.__row = rows
        self.__col = cols
        self._hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        new_show = id, movie_name, time
        self.show_list.append(new_show)
        new_seats = [[0 for _ in range(self.__col)] for _ in range(self.__row)]
        self._seats[id] = new_seats

    def show_id_validator(self, id):
        if id not in self._seats:
            print("Show id is invalid \n")
            return False
        else:
            return True

    def book_seats(self, id, *args):
        if id not in self._seats:
            print("Show id is invalid \n")
            return
        else:
            for tup in args:
                if (
                    tup[0] - 1 < 0
                    or tup[1] - 1 < 0
                    or tup[0] - 1 >= self.__row
                    or tup[1] - 1 >= self.__col
                ):
                    print("Seat row or column is invalid \n")
                elif self._seats[id][tup[0] - 1][tup[1] - 1] == 1:
                    print("Seat is already booked \n")
                else:
                    self._seats[id][tup[0] - 1][tup[1] - 1] = 1
                    print(f"Seat ({tup[0]}, {tup[1]})booked successfully  \n")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show Name: {show[1]}, Show ID: {show[0]}, Show Time: {show[2]}")
        print("\n")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Show id is invalid \n")
            return
        else:
            for col in self._seats[id]:
                print(col)
            print("\n")

cinema = Hall(8, 8, 1)
cinema.entry_show(1001, "Pathan", "12/9/24 3:00PM")
cinema.entry_show(1002, "Jawan", "12/9/24 5:00PM")
cinema.entry_show(1004, "Dunki", "15/9/24 5:00PM")
cinema.entry_show(1005, "Kush kush hota hein", "15/9/24 5:00PM")

while True:
    print("Options:")
    print("1. View all show today")
    print("2. View available seats")
    print("3. Book ticket")
    print("4. exit \n")
    option = int(input("Enter your option: "))
    print("\n")
    if option == 4:
        break
    elif option == 1:
        cinema.view_show_list()
    elif option == 2:
        show_id = int(input("Enter show ID: "))
        print("\n")
        cinema.view_available_seats(show_id)
    elif option == 3:
        show_id = int(input("Enter show ID: "))
        print("\n")
        if cinema.show_id_validator(show_id):
            seat_number = int(input("Number of seat you want to book: "))
            print("\n")
            for i in range(0, seat_number):
                row = int(input("Enter row number: "))
                print("\n")
                col = int(input("Enter column number: "))
                print("\n")
                cinema.book_seats(show_id, (row, col))
    else:
        print("Option is invalid \n")



