# 사용자 정의 예외를 생성합니다.
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self) -> str:
        return self.message

    def print(self):
        print("####오류 정보####")
        print("메시지:", self.message)
        print("값:", self.value)

# 예외를 발생
try:
    raise CustomException("그냥", 263)
except CustomException as e:
    e.print()