'''
#index is broken
def bin_search(rotatedArr, num, index):
    lengthArr = len(rotatedArr)
    start = int(lengthArr/2) - 1
    if num == rotatedArr[start]:
        return index + int(start) + (lengthArr%2) * -1 + 1
    elif lengthArr <= 1:
        return -1
    elif rotatedArr[start] < num:
        index += start + (lengthArr%2)
        print(rotatedArr[start+1:])
        return bin_search(rotatedArr[start+1:], num, index)
    elif rotatedArr[start] > num:
        index = abs(index + int(start/2))
        print(rotatedArr[:start])
        return bin_search(rotatedArr[:start], num, index)
'''

def bin_search(rotatedArr, num):
    lengthArr = len(rotatedArr)
    start = int(lengthArr/2) - 1
    if num == rotatedArr[start]:
        return True
    elif lengthArr <= 1:
        return False
    elif rotatedArr[start] < num:
        print(rotatedArr[start+1:])
        return bin_search(rotatedArr[start+1:], num)
    elif rotatedArr[start] > num:
        return bin_search(rotatedArr[:start], num)

def rotate_arr(arr, rotate):
    if abs(rotate) > len(arr) -1:
        rotate = rotate % len(arr)
    if rotate > 0:
        return arr[rotate:] + arr[:rotate]
    elif rotate == 0:
        return arr
    else:
        return arr[rotate:] + arr[:rotate]

#14
#arr = [1,2,3,5,6,7,10,11,21,67,78,79,81,85,101,142]
#print(bin_search(arr, 101, 0))

6
arr = [0,1,2,3,5,6,7,10,11,21,67,78,79,81,85,101]
#print(bin_search(arr, 10, 0))
print(rotate_arr(arr,5))
print(rotate_arr(arr,-25))

#11
#arr = [1,2,3,5,6,7,10,11,21,67,78,79,81,85,101]
#print(bin_search(arr, 78, 0))

