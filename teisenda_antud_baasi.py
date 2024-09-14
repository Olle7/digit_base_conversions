from math import log
from timeit import timeit

def number_to_base(n,base):
    number=[]
    for digit in range(int(log(n+0.500001,base)),-1,-1):
        number.append(n//base**digit%base)
    return number
def first_numbers_in_base_simple(n, base):
    numbers=[]
    for i in range(n):
        numbers.append(tuple(number_to_base(i,base)))
    return numbers
def first_numbers_in_base(n, base):
    if n<2:
        if n:
            return [(0,)]
        return []
    numbers=[(0,),(1,)]
    base-=1
    l=-1
    num=[1]
    for i in range(n-2):
        if num[-1]==base:
            num[-1]=0
            for i in range(l,-1,-1):
                if num[i]==base:
                    num[i]=0
                else:
                    num[i]+=1
                    break
            else:
                num=[1]+num
                l+=1
        else:
            num[-1]+=1
        numbers.append(tuple(num))#replace tuple(num) with num.copy() if you want resutl to contain lists instead of tuples.
    return numbers

def first_numbers_in_base_with_0fill(digits, base):
    if base==0:
        return []
    number=[0]*digits
    numbers=[number.copy()]
    base=base-1
    while True:
        for i in range(digits-1,-1,-1):
            if number[i]==base:
                number[i]=0
            else:
                number[i]+=1
                numbers.append(number.copy())
                break
        else:
            return numbers


print(first_numbers_in_base_with_0fill(0, 0))
input("ST")
#tests:
assert(first_numbers_in_base_simple(23, 2)==first_numbers_in_base_simple(23, 2))
assert(first_numbers_in_base_simple(10, 3)==first_numbers_in_base_simple(10,3))
assert(first_numbers_in_base_simple(40, 4)==first_numbers_in_base_simple(40, 4))
assert(first_numbers_in_base_simple(300, 77)==first_numbers_in_base_simple(300, 77))


print("base2")
print("uus:", timeit("first_numbers_in_base2(100,2)", globals={"first_numbers_in_base2":first_numbers_in_base}, number=100000) / 100000)
print(timeit("first_numbers_in_base2(62308,2)", globals={"first_numbers_in_base2":first_numbers_in_base}, number=200) / 200)
print(timeit("first_numbers_in_base2(62308,3)", globals={"first_numbers_in_base2":first_numbers_in_base}, number=200) / 200)
print(timeit("first_numbers_in_base2(62308,10)", globals={"first_numbers_in_base2":first_numbers_in_base}, number=200) / 200)
print(timeit("first_numbers_in_base2(62308,120)", globals={"first_numbers_in_base2":first_numbers_in_base}, number=200) / 200)
print()