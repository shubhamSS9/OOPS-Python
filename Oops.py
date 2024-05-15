class Car:
    total_car = 0


    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        

    def get_brand(self):
        return self.__brand

    def name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"
        

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"   


obj = Car("mahendra", "thar")
print(obj.__brand)
print(obj.__model)

obj2 = Car("suzuki", "Swift")
print(obj2.brand)
print(obj2.model)

obj3=Car("TATA", "Nexon")
print(obj3.brand)
print(obj3.model)
print("*******************")
print(obj3.name())


print("************")

tesla = ElectricCar("Tasla", "Model s3", "85Kwh")
print(tesla.model, tesla.__brandbrand, tesla.battery_size)
print(tesla.name())

print(tesla.fuel_type)

print("*********")

print(tesla.brand())
