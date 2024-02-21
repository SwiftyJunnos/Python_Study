# Chapter04_04

# Immutable Dict
from types import MappingProxyType

d = { "key1": "value1" }
d_frozen = MappingProxyType(d) # Read-Only

print(d, id(d))
print(d_frozen, id(d_frozen)) # read-only이ㅁ지만 여전히 unhashable

# d_frozen["key2"] = "value2" # Error - 'mappingproxy' object does not support item assignment
d["key2"] = "value2"

# Set
s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = set(["Apple", "Orange", "Apple", "Orange", "Kiwi"])
s3 = {3}
s4 = set() # {}는 dict
s5 = frozenset({"Apple", "Orange", "Apple", "Orange", "Kiwi"})
print(s1, s2, s3, s4, s5)

s1.add("Melon")
print(s1)
# s5.add("Melon") # Error - 'frozenset' object has no attribute 'add'

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print(dis("{10}")) # faster
print(dis("set([10])"))

# 지능형 집합 (Comprehending Set)

from unicodedata import name

print({name(chr(i), "") for i in range(0, 256)})
