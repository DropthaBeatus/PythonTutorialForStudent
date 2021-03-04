import re

def analyze_data(code):

    code_list = {"(":")",
                 "[":"]",
                 "{":"}"}

    code_list_reverse = {")": "(",
                        "]": "[",
                        "}": "{"}

    list = []
    print(code_list)

    code = re.sub(r"[^](){}[]", "", code)
    print(code)
    for char in code:
        print(list)
        if char in code_list:
            list.append(char)
        elif char in code_list_reverse:
            if code_list_reverse[char] == list[len(list)-1]:
                list.pop(len(list)-1)
            else:
                return False
        else:
            return False


    if len(list) < 1:
        return True
    else:
        return False





print(analyze_data("{}[][asdfadsfa[]asdfasdfa()]asdfasdf+_+_+SDFSDfsd"))
print(analyze_data("{}[][}asdfadsfa[]asdfasdfa()asdfasdf+_+_+SDFSDfsd"))

