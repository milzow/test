# 1부터 숫자를 하나씩 증가시키면서 더해 합이 10000을 언제 넘기는지 
# 10000을 넘기는 숫자와 그때의 합은?

limit = 10000
i = 1

# sum은 파이썬 내부에서 사용하는 식별자이므로 sum_value라는 변수 이름을 사용합니다.
sum_value = 0

while sum_value < limit:
    sum_value = sum_value + i - 1
    i = i + 1
    
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))