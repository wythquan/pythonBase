class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, happy):
        self.name = name
        self.age = age
        self.isHappy = happy

    def get_data(self):
        return f"{self.name}, age: {self.age}, is happy: {self.isHappy}"

cat1 = Cat()
cat1.set_data("Barsik", 3, True)
# cat1.name = "Barsik"
# cat1.age = 3
# cat1.isHappy = True

cat2 = Cat()
cat2.set_data("Destroyer", 1, False)

cat1_data = cat1.get_data()
cat2_data = cat2.get_data()
print(f"{cat1_data}\n{cat2_data}")

# cat2.name = "Destroyer"
# cat2.age = 1
# cat2.isHappy = False

# print(cat1.name, cat2.name)