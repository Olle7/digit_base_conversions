from time import time
from digit_base_conversions import list_of_digits_to_number, number_to_list_of_digits,get_digit,get_digit2,get_digit3,first_numbers_in_base

#print(list(first_numbers_in_base(35,4,0,False)))#OK
#print(list(first_numbers_in_base(10,4,0,False)))

print(list(first_numbers_in_base(4,2,0,False)))

assert list(first_numbers_in_base(10,4,0,False))==[[0], [1], [2], [3], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2]]
assert list(first_numbers_in_base(0,4,0,False))==[]
assert list(first_numbers_in_base(1,4,0,False))==[[0]]
assert list(first_numbers_in_base(35,4,0,False))==[[0], [1], [2], [3], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2], [0, 3], [1, 3], [2, 3], [3, 3], [0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [0, 2, 1], [1, 2, 1], [2, 2, 1], [3, 2, 1], [0, 3, 1], [1, 3, 1], [2, 3, 1], [3, 3, 1], [0, 0, 2], [1, 0, 2], [2, 0, 2]]
assert (list(first_numbers_in_base(0,4,0,False))==[])
assert (list(first_numbers_in_base(1,4,0,False))==[[0]])


assert list(first_numbers_in_base(21,4,0,True))==[[0], [1], [2], [3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 1, 0]]
assert (list(first_numbers_in_base(0,4,0,True))==[])
assert (list(first_numbers_in_base(1,4,0,True))==[[0]])
#print(list(first_numbers_in_base(211,10,2,False)))
#print(list(first_numbers_in_base(21,2,3,True)))#OK
assert list(first_numbers_in_base(21,2,3,True))==[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 1, 1], [1, 0, 1, 0, 0]]
assert list(first_numbers_in_base(0,2,3,True))==[]
assert (list(first_numbers_in_base(1,2,3,True))==[[0,0,0]])

assert (list(first_numbers_in_base(25,4,3,False))==[[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0], [0, 3, 0], [1, 3, 0], [2, 3, 0], [3, 3, 0], [0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [0, 2, 1]])
assert (list(first_numbers_in_base(25,10,3,False))==[[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0], [8, 0, 0], [9, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0], [4, 2, 0]])
assert (list(first_numbers_in_base(15,2,2,False))==[[0, 0], [1, 0], [0, 1], [1, 1], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1]])
#input()
#print(list_of_digits_to_number([3,7,5],10,most_signicant_digit_first=False))
#print(list_of_digits_to_number([3,7,5],10,most_signicant_digit_first=True))

assert get_digit(7832983,10,-2,True)==0
assert get_digit(7832983,10,-1,True)==0
assert get_digit(7832983,10,0,True)==7
assert get_digit(7832983,10,1,True)==8
assert get_digit(7832983,10,2,True)==3
assert get_digit(7832983,10,3,True)==2

assert get_digit(7832983,10,-3,False)==0
assert get_digit(7832983,10,-2,False)==0
assert get_digit(7832983,10,-1,False)==0
assert get_digit(7832983,10,0,False)==3
assert get_digit(7832983,10,1,False)==8
assert get_digit(7832983,10,2,False)==9
assert get_digit(7832983,10,3,False)==2

assert number_to_list_of_digits(983728327,10,most_signicant_digit_first=True)==[9, 8, 3, 7, 2, 8, 3, 2, 7]
assert number_to_list_of_digits(983728327,10,most_signicant_digit_first=False)==[7, 2, 3, 8, 2, 7, 3, 8, 9]
#print(number_to_list_of_digits(983728327,10,most_signicant_digit_first=True))

#print(number_to_list_of_digits(12312,10,10))

from timeit import timeit
number=1000012124332132355747445764523432432432332432
base=21
#print(timeit(lambda:number_to_list_of_digits(number,base)))

from math import log
#print(number_to_list_of_digits(24343,10))
t=time()
for base in range(2,20):
    for n in range(2,10000):
        for zftl in range(3):
            l=number_to_list_of_digits(n,base,zftl,most_signicant_digit_first=True)
            assert len(l)>=zftl
            for p in range(len(l)):
                assert l[-1-p]==get_digit(n,base,p,False)
                #assert l[p]==get_digit(n,base,p,True)
print(time()-t)





#sa=32149876984321769832164983264783967500223892430239832984983298329386464564564354353476675675675762076897392768591432749810538097410890001438932747621
#base=311
#pod=31
#print("vastus:",get_digit(sa,base,pod,False))
#print("timeit:",timeit(lambda:get_digit(sa,base,pod,False)))
#print("timeit:",timeit(lambda:get_digit2 (sa,base,pod)))
#print("timeit:",timeit(lambda:get_digit3 (sa,base,pod)))



t=time()
for base in range(2,4000):
    assert number_to_list_of_digits(0,base)==[]
    for n in range(1,base):
        assert number_to_list_of_digits(n,base)==[n]
print(time()-t)
t=time()
for n in range(2,100):
    assert number_to_list_of_digits(n,n,most_signicant_digit_first=True)==[1,0]
    assert number_to_list_of_digits(n,n,most_signicant_digit_first=False)==[0,1]
print(time()-t)
t=time()
for base in range(2,100):
    for n in range(0,20000):
        #print(n,base,number_to_list_of_digits(n,base,most_signicant_digit_first=True))
        assert n==list_of_digits_to_number(number_to_list_of_digits(n,base,most_signicant_digit_first=True),base,most_signicant_digit_first=True)
        assert n==list_of_digits_to_number(number_to_list_of_digits(n,base,most_signicant_digit_first=False),base,most_signicant_digit_first=False)
for base in range(-50,-1):
    for n in range(0,200):
        assert n==list_of_digits_to_number(number_to_list_of_digits(n,base,most_signicant_digit_first=True),base,most_signicant_digit_first=True)
        assert n==list_of_digits_to_number(number_to_list_of_digits(n,base,most_signicant_digit_first=False),base,most_signicant_digit_first=False)
print(time()-t)