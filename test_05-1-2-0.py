def mul(*values):
    out_put = 1
    for value in values:
        out_put *= value

    return out_put

# 함수를 호출합니다.
print(mul(5,7,9,10))
