# 클래스를 선언합니다.
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------학생 목록------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

# 학생 리스트를 선언합니다.
Student("윤인성", 88, 66, 77, 88)
Student("구자욱", 88, 66, 77, 88)
Student("배수빈", 88, 66, 77, 88)
Student("최신구", 88, 66, 77, 88)
Student("노구", 88, 166, 77, 88)
Student("김재협", 88, 66, 77, 88)
Student("박조찬", 88, 66, 77, 88)
Student("구라철", 88, 66, 77, 88)
Student("이민기", 88, 66, 77, 88)
Student("김하기", 88, 66, 77, 88)
Student("염수산", 88, 66, 77, 88)
Student("함주경", 88, 66, 77, 88)
Student("박은애", 88, 66, 77, 88)

# 현재 생성된 학생을 모두 출력합니다.
Student.print()
