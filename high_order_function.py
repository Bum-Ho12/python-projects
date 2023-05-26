import math
from functools import reduce

def area(r):
    return math.pi*(r**2)

#map function
def map_order():
    radii = [2,5,7,4,4,6]
    ar = list(map(area,radii))
    print(ar)

#filter function
def filter_function():
    lst = [-1,3,5,-9,-7,-5,4]
    neg = list(filter(lambda x:x<0,lst))
    pst = list(filter(lambda x:x>0,lst))
    print("negative list -> ",neg)
    print("positive list -> ",pst)

#reduce function
def reduce_function():
    lst = [2,5,7,4,4,6]
    print(reduce(lambda a,b:a+b,lst))



if __name__ == "__main__":
    print("Select option:\n 1 -> map\n2 -> filter\n 3 -> reduce")
    option = int(input())
    if option ==1:
        map_order()
    elif option ==2:
        filter_function()
    elif option ==3:
        reduce_function()
    else:
        print("Undefined")
