# 클래스를 선언합니다.
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

# 학생 리스트를 선언합니다.
student = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 88, 88, 88, 12),
    Student("구자욱", 87, 98, 88, 15),
    Student("구자윤", 87, 98, 88, 25),
    Student("윤라인", 87, 98, 88, 80),
    Student("최치수", 87, 98, 88, 75)
]

# 출력합니다.
print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))