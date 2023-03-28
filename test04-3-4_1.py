# 1부터 100까지의 숫자의 양끝 숫자 1 * 99, 2 * 98 ..., 99 * 1 형태로 곱 했을때 
# 곱한 값이 최대가 되는 경우는 어떤 숫자를 곱했을 때인지 찾기

max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    # 최대값 구하기
    current = i * j
    if current > max_value:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))
