# 함수 선언
def flatten(data):
    output = []
    for value in data:   
        if type(value) == list:
            output += flatten(value)

        else:
            output.append(value)

    return output


example = [[1,2,3], [4, [5,6]], 7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))