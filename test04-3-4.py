# 1부터 100까지의 숫자의 양끝 숫자 1 * 99, 2 * 98 ..., 99 * 1 형태로 곱 했을때 
# 곱한 값이 최대가 되는 경우는 어떤 숫자를 곱했을 때인지 찾기

max_value = 0
a = 0
b = 0

for i in range(1, 100, 1):
    j = 100 - i

    # 최대값 구하기
    if i * j < a * b:
        max_value = a * b
    else:
        a = j
        b = i

print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))
