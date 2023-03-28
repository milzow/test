# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self, student):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(student),
            self.get_average(student)
        )

    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() == value.get_sum()
    # 생략
    # def __eq__(self, value):
    #     return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

# 학생을 선언합니다.
student_a = Student("윤인성", 87, 98, 88, 95),
student_b = Student("박나래", 66, 66, 66, 66),

# 비교합니다.
student_a == 10
print("student_a == 10", student_a == 10)
print("student_b == 20", student_a == 20)

