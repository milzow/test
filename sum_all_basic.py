# 함수 선언
def sum_all(start, end):
    # 변수 선언
    out_put = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1):
        out_put += i
    # 리턴 합니다.
    return out_put

# 함수를 호출합니다.
print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0, 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))

