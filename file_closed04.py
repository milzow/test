# try except 구문을 사용합니다.
try:
    # 파일을 엽니다.
    file = open("info.txt", "w")
    # 여러가지 처리
    예외.발생()
except Exception as e:
    print(e)

#파일을 닫습니다.
file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed", file.closed)
