# Chapter04-02

# Tuple Advanced
# Unpacking
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

# Mutable vs Immutable (list vs tuple)
l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l)) # id 값이 모두 달라짐
print(m, id(m)) # id 값이 동일

# * 2: 새로운 객체를 생성하여 값을 곱합니다.
# *= 2: 기존 객체의 값을 직접 수정합니다.

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환
# sort : 정렬 후 객체 직접 변경
f_list = ["orange", "apple", "mango", "papaya", "lemon", "strawberry", "coconut"]
print(f_list)
print("sorted - ", sorted(f_list))
print("sorted (reversed) - ", sorted(f_list, reverse = True))
print("sorted (length) - ", sorted(f_list, key = len))
print("sorted (lambda) - ", sorted(f_list, key = lambda x: x[-1])) # 마지막 글자를 기준으로 정렬
print("sorted (reversed lambda) - ", sorted(f_list, key = lambda x: x[-1], reverse = True))
print(f_list)

print("sort - ", f_list.sort(), f_list)
print("sort (reversed) - ", f_list.sort(reverse = True), f_list)

# list vs array
# list : 융통성, 다양한 자료형, 범용적 사용
# array : 숫자 기반, 단일 자료형
