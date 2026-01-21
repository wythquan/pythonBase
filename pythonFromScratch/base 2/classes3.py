class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def print_info(self):
        print(f"Year: {self.year}, city: {self.city}")

class School(Building):
    students = None

    def __init__(self, students, year, city):
        super().__init__(year, city)
        self.students = students

    def print_info(self):
        print(f"Students: {self.students} year: {self.year}, city: {self.city}")

class House(Building):
    pass

class Shop(Building):
    pass


school = School(30, 2000, "Kosice")
school.print_info()
house = House(2000, "Kosice")
shop = Shop(2000, "Kosice")