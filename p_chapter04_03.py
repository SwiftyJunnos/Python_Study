# Chapter04_03

# Hash-Table : Key에 Value를 저장하는 구조 (__dict__)
# Python에서는 dict 사용
# key -> 해슁 함수 -> 해쉬 주소 -> value
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) # Error! (unhashable type: 'list') - mutable type이기 때문

# Dict setdefault
source = (
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5")
)
new_dict1 = {}
new_dict2 = {}

# without setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# using setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)

# Caution
new_dict3 = { k: v for k, v in source }
print(new_dict3) # remove duplicants
