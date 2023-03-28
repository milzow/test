# 태어난 년도를 입력받는다.
str_input = input("태어난 년도를 입력하세요>")
birth_year = int(str_input)

if birth_year % 12 == 0:
    print("{}년도에 태어나 원숭이 띠입니다.".format(birth_year))
elif birth_year % 12 == 1:
    print("{}년도에 태어나 닭띠 입니다.".format(birth_year))
elif birth_year % 12 == 2:
    print("{}년도에 태어나 개띠 입니다.".format(birth_year))
elif birth_year % 12 == 3:
    print("{}년도에 태어나 돼지띠 입니다.".format(birth_year))
elif birth_year % 12 == 4:
    print("{}년도에 태어나 쥐띠 입니다.".format(birth_year))
elif birth_year % 12 == 5:
    print("{}년도에 태어나 소띠 입니다.".format(birth_year))
elif birth_year % 12 == 6:
    print("{}년도에 태어나 범띠 입니다.".format(birth_year))
elif birth_year % 12 == 7:
    print("{}년도에 태어나 토끼띠 입니다.".format(birth_year))
elif birth_year % 12 == 8:
    print("{}년도에 태어나 용띠 입니다.".format(birth_year))
elif birth_year % 12 == 9:
    print("{}년도에 태어나 뱀띠 입니다.".format(birth_year))
elif birth_year % 12 == 10:
    print("{}년도에 태어나 말띠 입니다.".format(birth_year))
else:
    print("{}년도에 태어나 양띠 입니다.".format(birth_year))
