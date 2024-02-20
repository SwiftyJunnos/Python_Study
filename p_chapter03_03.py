# Chapter03-03
from math import sqrt

# Tuple
from typing import Tuple

pt1: Tuple[float, float] = (1.1, 5.0)
pt2: Tuple[float, float] = (2.5, 1.5)
print(pt1, pt2)

l_length1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_length1)

# Named Tuple
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

pt3 = Point(1.1, 5.0)
pt4 = Point(2.5, 1.5)
print(pt3, pt4)

l_length2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_length2)

# Dictionary to Tuple
from typing import Dict

dict: Dict[str, int] = {"x": 75, "y": 55}
pt5 = Point(**dict) # Keyword Unpacking
print(pt5)
print(pt3.x + pt5.x)

# NamedTuple Methods
temp = [52, 38]

p4 = pt3._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(pt3._fields, pt5._fields)

# _asdict() : OrderedDict 반환
print(pt3._asdict())

# 반 20명, 4개의 반 (A, B, C, D)
class Classes(NamedTuple):
    rank: str
    number: str

numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(students)

students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [
        str(n) for n in range(1, 21)
    ]
]
for s in students2:
    print(s)

print(students == students2)
