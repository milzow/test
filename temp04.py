# 함수 정의
pi = 3.14159264
def number_input():
    output = input("숫자입력> ")
    return float(output)
def get_circumference(radius):
    return 2 * pi * radius
def get_circle_area(radius):
    return pi * radius * radius

# 코드 본문
radius = number_input()
print("반지름 : {:g} 일 때 둘래는 {:2.2f}입니다.".format(radius, get_circumference(radius)))
print("반지름 : {:g} 일 때 면적은 {:2.2f}입니다.".format(radius, get_circle_area(radius)))

