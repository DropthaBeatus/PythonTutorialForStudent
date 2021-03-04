import copy
import sys

def elevation_count(list):
    x = 0
    highest_peak_index = 0
    while x < len(list):
        if list[highest_peak_index] < list[x]:
            highest_peak_index = x

        x += 1
    return shift(list[highest_peak_index:], 1, 0) + shift(list[:highest_peak_index+1], -1, 0)


def shift(list, move, count):
    if len(list) > 2:
        x = 0
        max = len(list)-1
        if move < 0:
            x = max
        second_highest = 1
        sh_index = 0
        x = x + move
        while max > x >= 0:
            if list[x] >= second_highest:
                second_highest = list[x]
                sh_index = x
            x = x + move

        if move < 0:
            list.pop(max)
            temp_list = list[slice(sh_index, max)]
            count = count + shift(list[:sh_index+1], move, calculate_water(temp_list,second_highest))
            return count
        else:
            list.pop(0)
            temp_list = list[slice(0,sh_index)]
            count = count + shift(list[sh_index:], move, calculate_water(temp_list,second_highest))
            return count

    else:
        return count


def calculate_water(list, second_highest):
    total_area = 0
    if len(list) > 2:
        for ele in list:
            total_area += second_highest - ele
        return total_area
    return total_area



test = elevation_count([0,1,0,2,1,0,1,3,2,1,2,1])
print("The area of the place is {}".format(test))
test = elevation_count([3,1,0,2,1,0,1,3,2,1,2,1])
print("The area of the place is {}".format(test))

r = []
for x in range(0,50):
    r.append(x)
test = elevation_count(r)
print("The area of the place is {}".format(test))




    #TODO make sure to add for water being added to sides.
