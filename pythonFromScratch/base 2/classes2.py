class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, happy):
        self.set_data(name ,age, happy)

    def set_data(self, name, age, happy = None):
        self.name = name
        self.age = age
        self.isHappy = happy

    def get_data(self):
        return f"{self.name}, age: {self.age}, is happy: {self.isHappy}"
    
    def print_data(self):
        print(f"{self.name}, age: {self.age}, is happy: {self.isHappy}")

cat1 = Cat("Barsik", 3, True)
# cat1.set_data("Barsik", 3, True)

cat2 = Cat("Destroyer", 1, False)
# cat2.set_data("Destroyer", 1, False)

cat1_data = cat1.get_data()
cat2_data = cat2.get_data()
print(f"{cat1_data}\n{cat2_data}")

