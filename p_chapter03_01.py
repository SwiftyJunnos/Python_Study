# Chapter 03-02
# Special Method (Magic Method)
# Python의 핵심 : Sequence, Iterator, Functions, Class

# "Special Method"?
# Class 안에 정의할 수 있는 특별한 (Built-In) 메서드
# __METHOD__

# 기본형
print(int) # <class 'int'>
print(float) # <class 'float'>

# 모든 속성 및 메서드 출력
print(dir(int))
print(dir(float))

n = 10

print(n.__doc__)
print(n + 100, n.__add__(100))
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제
import typing

class Fruit:
    def __init__(self, name, price):
        self._name: str = name
        self._price: float = price

    def __str__(self) -> str:
        return "Fruit: {} , {}".format(self._name, self._price)

    def __add__(self, x: 'Fruit') -> float:
        return self._price + x._price

    def __sub__(self, x: 'Fruit') -> float:
        return self._price - x._price

    def __le__(self, x: 'Fruit') -> bool:
        return True if self._price <= x._price else False

    def __ge__(self, x: 'Fruit') -> bool:
        return True if self._price >= x._price else False

s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

print(s1._price + s2._price)
print(s1 + s2) # __add__ 매직 메서드 활용
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2, s2 - s1)
print(s1, s2)
