# 리스트를 선언합니다.
from cmath import pi


list_a = [1,2,3]

# 리스트 뒤에 요소를 추가하기
print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("#리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)
print()

# 리스트 뒤에 여러개 요소 한번에 추가하기
print("#리스트 뒤에 여러개 요소 한번에 추가하기")
list_b = [6,7,8,9,10]
list_a.extend(list_b)
print(list_a)