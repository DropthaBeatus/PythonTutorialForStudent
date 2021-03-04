

def countLevelUpPlayers(cutOffRank, num, scores):
    if num == 0 or scores is None:
        return 0
    scores.sort(reverse=True)

    x = 0
    prev_score = ''
    for i in scores:
        print(i)
        if prev_score == i:
            x += 1
        elif x == cutOffRank:
            return x
        elif i != '0':
            prev_score = i
            x += 1
        else:
            return x

    return x

def findSubstrings(input):
    dict = {}
    list_in = list(input)
    x = 0

    while x<len(list_in):
        substring = list_in[x]
        if x < len(list_in) -1:
            while list_in[x] == list_in[x+1]:
                x += 1
                substring += list_in[x]
                if x == len(list_in) - 1:
                    break
        if substring in dict:
            dict[substring] = -1
        else:
            dict[substring] = 1
        x+=1

    return_list = []
    for key, value in dict.items():
        if value == 1:
            return_list.append(key)

    return return_list





#print(countLevelUpPlayers(2, 5, ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']))

print(findSubstrings("baddacxb"))

#print(ord('dd'))