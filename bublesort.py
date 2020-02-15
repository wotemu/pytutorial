# prints bublesort
""" def bs(a):
    b = len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y], a[y+1] = a[y+1], a[y]
                return a


a = [32, 5, 3, 6, 7, 54, 87]
bs(a)
 """

# prints star

"""
def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))


pyfunc(9)
 """

# fiabonacci series
""" a = int(input('Enter the terms: '))
f = 0
s = 1
if a <= 0:
    print('The series is: ', f)
else:
    print(f, s, end=" ")
    for x in range(2, a):
        next = f+s
        print(next, end=' ')
        f = s
        s = next
 """

# prime or not
""" a = int(input('Enter a number: '))
if a > 1:
    for x in range(2, a):
        if a % x == 0:
            print('Not prime')
            break
    else:
        print('Prime')
else:
    print('Not prime') """

# palindrome
""" a = input('Enter a sequence: ')
b = a[::-1]
if a == b:
    print('palindrome')
else:
    print('Not palindrome') """

# count capital letters
