# 모듈을 가져옵니다.
from functools import wraps

# 함수로 데코레이터를 생성합니다.
def test(function):
    @wraps(function)
    
def wrapper(*arg, **kwargs):
    print("인사가 시작되었습니다.")
    function(*arg, **kwargs)
    print("인사가 종료되었습니다.")
    return wrapper