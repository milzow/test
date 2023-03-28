# 100명의 사람이 나누어 앉는 경우의 수 구하기
# 한개의 테이블에는 최대 10명
# 혼자 앉는 사람은 없음.   1<테이블에 앉는 사람<=10
# 일때 나누어 지는 경우의 수

#앉힐수있는 최소사람의 수 = 2
#앉힐수있는 최대사람의 수 = 10
#전체 사람의 수 = 100
minsit = 2
maxsit = 10
allman = 100

memo = {
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 4
}

def sitablecnt(leftsit, sit):       #남은사람수, 앉힌사람수
    key = str([leftsit, sit])       #남은사람수, 앉힌사람수
    # 종료 조건
    if key in memo:
        return memo[key]

    if leftsit < 0:
        # 무효이므로 0을 리턴
        return 0
    if leftsit == 0:
        # 유효하므로 수를 세기 위해 1을 리턴
        return 1

    # 재귀처리
    output = 0
    for i in range(sit, maxsit + 1): # 앉힌사람수, 앉힐 수 있는 최대사람수 => 앉힐 수 있는 사람수... 2, 3, 4, 5, 6, 7, 8, 9, 10
        output += sitablecnt(leftsit - i, i) # 남은 사람수에서 앉힐 수 있는 사람수를 뺄수 있으면 1가지 경우의 수가 됨.

    # 메모화 처리
    memo[key] = output

    # 종료
    return output

print(sitablecnt(allman, minsit))
