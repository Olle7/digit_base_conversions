def first_numbers_in_base(n,base,zerofill_to_length=0):
    if zerofill_to_length==0:
        if n<2:
            if n:
                return [[0]]
            return []
        numbers=[[0],[1]]
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
            numbers.append(num.copy())  # replace tuple(num) with num.copy() if you want resutl to contain lists instead of tuples.
        return numbers
    else:
        if base==0 or n==0:
            return []
        number=[0]*zerofill_to_length
        numbers=[number.copy()]
        base=base-1
        n2=0
        n-=1
        while n2<n:
            for i in range(zerofill_to_length-1,-1,-1):
                if number[i]==base:
                    number[i]=0
                else:
                    number[i]+=1
                    numbers.append(number.copy())
                    break
            else:
                number=[1]+number
                zerofill_to_length+=1
                numbers.append(number.copy())
            n2+=1
        return numbers

from math import log
def number_to_base1(n,base):
    number=[]
    for digit in range(int(log(n+0.500001,base)),-1,-1):
        number.append(n//base**digit%base)
    while number and number[0]==0:
        number.pop(0)
    return number

def get_digit(number,base,position_of_the_digit):
    m=base**(position_of_the_digit-1)
    return (number%(m*base))//m

print(get_digit(1238,10,2))


def number_to_base(n,base,zerofill_to_length=0):
    digits = []
    if int(n)==n:
        if n:
            digits=[n%base]
        while n:
            n//=base
            digits=[n%base]+digits
    else:
        m_next=1
        m=1
        min_number_of_digits=0
        while m_next<=n:
            min_number_of_digits+=1
            m=m_next
            m_next*=base
        while n:
            min_number_of_digits-=1
            #print(n,m_next,end="")
            digit=n//m
            digits.append(digit)
            n=(n-digit*m)*base
        if 0<min_number_of_digits:
            digits=digits+[0]*(min_number_of_digits)
    if len(digits)<zerofill_to_length:
        digits=[0]*(len(digits)-zerofill_to_length)
    return digits


print(number_to_base(24343,10))

def digits_to_number(digits,base,check_digit_value=False):
    n=0
    m=1
    if digits:
        n=digits[len(digits)-1]
    for i_digit in range(len(digits)-2,-1,-1):
        if check_digit_value and (digits[i_digit]!=int(digits[i_digit]) or digits[i_digit]>=base):
            raise ValueError()
        m*=base
        n+=m*digits[i_digit]
    return n

#from  timeit import timeit
from time import time
#print (timeit("number_to_base(1238932014353121535253298342234141243321069060508233453464523424324432324432327645745764576432435476473534545455436525,235)",globals={"number_to_base":number_to_base},number=1))
#print(timeit("number_to_base2(1238932014353121535253298342234141243321069060508233453464523424324432324432327645745764576432435476473534545455436525,235)",globals={"number_to_base2":number_to_base2},number=1))
#number_to_base2(123893201435312153525329834223414124332106906050823,2)

#print(number_to_base2(123893201435312153525329835,10))
print(number_to_base(0,1))

t=time()
for base in range(2,100):
    for n in range(0,20000):
        assert n==digits_to_number(number_to_base(n,base),base)
for base in range(-50,-1):
    for n in range(0,200):
        assert n==digits_to_number(number_to_base(n,base),base)
print(time()-t)
#print(first_numbers_in_base(21,4,zerofill_to_length=0))