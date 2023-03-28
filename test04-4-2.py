# 리스트 내포를 사용해본 코드 입니다.
# 1 ~ 100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고
# 그 숫자들의 합을 구하는 코드
out_put = [ i for i in range(1, 101, 1) if "{:b}".format(i).count("0") == 1]
for i in out_put:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(out_put))
