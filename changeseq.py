from queue import PriorityQueue

def string_org_non_seq(phrase):
    dict_t = {}
    charArr = list(phrase)
    for c in charArr:
        if c in dict_t:
            dict_t[c] += 1
        else:
            dict_t[c] = 1

    priq = PriorityQueue()
    for value, key in dict_t.items():
        priq.put((key * -1, value))

    phrase = ""
    #need to fix test cases here in case its one letter or there are like 5 strings
    while priq.qsize() > 1:
        test1 = priq.get()
        test = priq.get()
        if test1[0] < 0:
            phrase += test1[1]
            priq.put(((test1[0] + 1), test1[1]))
        if test[0] < 0:
            phrase += test[1]
            priq.put(((test[0] + 1), test[1]))

    return phrase

print(string_org_non_seq("aabbatahaqrty"))





