# Chapter02-03
# 파이썬 심화
# 클래스 상세 설명
# Class, Static, Instance method
import typing

class Car():
    """
    Car class
    """

    price_per_raise = 1.2

    def __init__(self, company, details):
        self._company: str = company
        self._details = details

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)

    # Instance Method
    # self를 사용하기 때문에 인스턴스 자체의 값 사용
    def detail_info(self):
        print("Instance ID : {}".format(id(self)))
        print("Car detail info : {} {}".format(self._company, self._details.get("price")))

    def price(self):
        return self._details.get("price")

    def raised_price(self):
        return self._details.get("price") * Car.price_per_raise

    # Class Method
    @classmethod
    def raise_price(cls, percentage):
        if  not (percentage > 1):
            print("Please enter 1 or more.")
            return
        cls.price_per_raise = percentage

    # Static Method : parameter를 받지 않음
    @staticmethod
    def is_manufactured_by(car: "Car", manufacturer: str) -> bool:
        if car._company.lower() == manufacturer.lower():
            return True
        else:
            return False

car1 = Car("Ferrari", {"color" : "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color" : "Black", "horsepower": 270, "price": 5000})

print("Car1 price: {}".format(car1.price()))
print("Car1 raised price: {}".format(car1.raised_price()))

print("Car2 price: {}".format(car2.price()))
print("Car2 raised price: {}".format(car2.raised_price()))

# Class Method 사용
Car.raise_price(0.8)
Car.raise_price(1.4)

is_manufactured_by_BMW = Car.is_manufactured_by(car2, "BMW")
print(is_manufactured_by_BMW)
