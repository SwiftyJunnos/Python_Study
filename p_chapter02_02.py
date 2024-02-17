# Chapter02-02
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

class Car():
    """
    Car class
    Author : Lee
    Date : 2019.11.08
    """

    # 클래스 변수 : 모든 인스턴스들이 공유하는 변수 (static...)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr : {} - {}".format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print("Instance ID : {}".format(id(self)))
        print("Car detail info : {} {}".format(self._company, self._details.get("price")))

# Self 의미
car1 = Car("Ferrari", {"color" : "White", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color" : "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color" : "Silver", "horsepower": 300, "price": 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

# == (값 비교)
print(car1._company == car2._company)
# === (인스턴스 비교)
print(car1 is car2)

# dir : 프로퍼티 명들
print(dir(car1))
print(dir(car2))

# __dict__ : Dictionary 형태로 프로퍼티명과 값
print(car1.__dict__)

# __doc__ : Class document
print(Car.__doc__)
print(car1.__doc__)

car1.detail_info()

# __class__ : 해당 인스턴스의 클래스
print(car1.__class__, car2.__class__)
# Car 클래스의 id
print(id(car1.__class__), id(car2.__class__))

# 첫 번째 인자 self를 직접 줄 수도 있다.
Car.detail_info(car1) # == car1.detail_info()
Car.detail_info(car2)


# 클래스 변수
print(car1.car_count)
print(car1.__dict__) # car_count가 존재하지 않음
print(dir(car1)) # car_count 존재

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
print(Car.car_count)

# 인스턴스 네임스페이스 검색 후 없으면 상위(클래스)에서 검색
# 같은 이름일 경우 인스턴스 프로퍼티 -> 클래스 프로퍼티
