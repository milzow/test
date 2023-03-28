# 함수 선언
def sum_all(start=0, end=100, step=1):
    # 변수 선언
    out_put = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1, step):
        out_put += i
    # 리턴합니다.
    return out_put

# 함수 호출
print("A.", sum_all(0,100,10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))
