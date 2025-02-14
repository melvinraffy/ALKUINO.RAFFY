class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")


car1 = Car("Audi", "Audi A1 (GB)", 2019)
car2 = Car("Toyota", "Tacoma", 2005)

print("Car 1 Details:")
car1.display_info()
print("\nCar 2 Details:")
car2.display_info()