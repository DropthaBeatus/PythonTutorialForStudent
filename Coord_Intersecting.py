class rectangle():
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

def find_intersection(rectangle_a, rectangle_b):
    if rectangle_a.x <= rectangle_b.x <= rectangle_a.width + rectangle_a.x:
        return True
    elif rectangle_a.y <= rectangle_b.y <= rectangle_a.height + rectangle_a.y:
        return True
    elif rectangle_b.x <= rectangle_a.x <= rectangle_b.width + rectangle_a.x:
        return True
    elif rectangle_b.y <= rectangle_a.y <= rectangle_b.height + rectangle_b.y:
        return True
    else:
        return False




b = rectangle(-1, -1, 5, 5)
a = rectangle(4, 4, 5, 2)

print(find_intersection(a,b))
print(find_intersection(b,a))

y = rectangle(1, 1, 5, -5)
t = rectangle(3, 2, -5, 2)

print(find_intersection(y,t))
print(find_intersection(t,y))
print(find_intersection(t,t))


y = rectangle(1, 1, -5, -5)
t = rectangle(3, 2, -1, -2)

print(find_intersection(y,t))
print(find_intersection(t,y))
print(find_intersection(t,t))
