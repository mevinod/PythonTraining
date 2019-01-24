class Car:
    def __init__(self, model_name, year, price):
        self.model_name = model_name
        self.year = year
        self.price = price

    def incremented_price(self):
        return (self.price * 10) / 100


class SuperCar(Car):
    pass


honda = SuperCar('City', 2017, 55000)
print(honda.price, honda.year, honda.model_name)

print("Price incremented by ", honda.incremented_price())
