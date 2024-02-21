# Chapter04-01
# Sequence

# 컨테이너(Container) : 서로 다른 타입의 값들 보관 (list, tuple, collections.deque)
a = [3, 3.0, 'a']

# 플랫(Flat) : 단일 타입의 값 보관 (str, bytes, bytearray, array, memoryview)

# 가변 : (list, bytearray, array, memoryview, deque)
# 불변 : (tuple, str, bytes)

# 리스트 & 튜플
# 지능형 리스트 (Comprehending Lists)
chars = "+_)(*&^%$#@!"
code_list1 = []

for s in chars:
    # Unicode List
    code_list1.append(ord(s))
print(code_list1)

code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

# Generator : 연속되는 값을 효율적으로 핸들링 (한번에 하나의 값만 생성 -> 이전 / 이후 값 메모리 보관 X)
import array

tuple_generator = (ord(s) for s in chars)
print(tuple_generator) # 아직 값을 메모리에 할당하지 않음
print(next(tuple_generator))
print(next(tuple_generator))

array_generator = array.array("I", (ord(s) for s in chars))
print(array_generator)
print(array_generator.tolist())

# Generator 예제
classes = ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21))
for s in classes:
    print(s)

#
mark1 = [["~"] * 3 for _ in range(4)]
mark2 = [["~"] * 3] * 4

# 수정
mark1[0][1] = "x"
mark2[0][1] = "x"
print(mark1)
print(mark2)

# [['~', 'x', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
# [['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~']]
# mark2의 경우 1 인덱스의 모든 값이 변경

# mark1의 경우 4개의 리스트를 생성 (id 값 다름)
# mark2의 경우 하나의 리스트를 4개로 복사 (id 값 동일)
print([id(i) for i in mark1])
print([id(i) for i in mark2])
