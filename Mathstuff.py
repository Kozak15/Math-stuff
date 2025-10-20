#Some random math stuff in Python
#Imma upload number base conversion and bal 3 string in the future
import math
# Numerical integration using the Riemann sum method
def integral(a,b):
    count = 0
    dx = 0.00001
    while b > a:
        count += f(b)
        b -= dx
    return count * dx

#Example function to integrate
def f(x):
    return math.sin(x) ** 3
round(integral(0,math.pi),3)

#Recursive function to compute the nth root of a number N using the Newton-Raphson method
def nth_root(N, n, tol=1e-6, X_now=None):
    if X_now is None:
        X_now = N if N != 0 else 1
    X_next = ((n - 1) * X_now + N / (X_now ** (n - 1))) / n

    if abs(X_next - X_now) < tol:
        return X_next
    else:
        return nth_root(N, n, tol, X_next)

#Arctangent function using Taylor series expansion, summing n terms. Improves accuracy with higher n.
def arctan(x,n):
    count = 0
    for i in range(1,n+1):
        term = ((-1)**(i-1) * (x**(2*i -1))) / (2*i - 1)
        count += term
    return count
def pi(n):#Most accurate I could find that was short
    return 16 * arctan(1/5 ,n) - 4 * arctan(1/239 ,n)

#Horner's method for polynomial evaluation
def poly_eval(tup,x):
    if len(tup) == 0:
        return 0
    if len(tup) == 1:
        return tup[0]
    return tup[0] + (x*(poly_eval(tup[1:],x)))
#Polynomial multiplication
def multiply_poly(p1 , p2):
    if p1 == () or p2 == ():
        return ()
    else:
        ans = [0] * (len(p1) + len(p2) - 1)
        for i in range(len(p1)):
                       for j in range(len(p2)):
                                      ans[i + j] += p1[i] * p2[j]
        return tuple(ans)
#Polynomial addition and subtraction
def add_poly(p1, p2):
    ans = []
    for i in range(max(len(p1), len(p2))):
        if i < len(p1):
            x = p1[i]
        else:
            x = 0
        if i < len(p2):
            y = p2[i]
        else:
            y = 0
        ans.append(x+y)
    while len(ans) > 0 and ans[-1] == 0:
        ans.pop()
    
    return tuple(ans)
def subtract_poly(p1, p2):
    ans = []
    for i in range(max(len(p1), len(p2))):
        if i < len(p1):
            x = p1[i]
        else:
            x = 0
        if i < len(p2):
            y = p2[i]
        else:
            y = 0
        ans.append(x-y)
    while len(ans) > 0 and ans[-1] == 0:
        ans.pop()
    return tuple(ans)
#Polynomial long division using numpy for convenience
import numpy#I know it's cheating but i'm lazy
def divide_poly(p1,p2):
    if len(p1) < len(p2):
        return ((),p1)
    if p2 == ():
        return "Error: Divide by zero"
    qx, rx = numpy.polynomial.polynomial.polydiv(p1, p2)
    lst_1,lst_2 = [],[]
    for item in qx:
        lst_1.append(int(item))
    for item in rx:
        lst_2.append(int(item))
    if lst_2 == [0]:
        lst_2 = []

    return (tuple(lst_1),tuple(lst_2))

#Collatz conjecture
#Collatz operator
def collatz(n):
       if n % 2 == 0:
         return n // 2
       else:
         return 3 * n + 1
#Stopping time function
def stopping_time(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
#Maximum number reached in the sequence
def max_num_reached(n):
    max_num_reached = n
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        max_num_reached = max(n , max_num_reached)
    return max_num_reached
#Number with the maximum stopping time for numbers up to n
def max_stopping_time(n):
    max_steps = 0
    new_n = 1
    for x in range(1, n + 1):
        steps = stopping_time(x)
        if steps > max_steps:
            max_steps=steps
            new_n = x
    return [new_n, max_steps]
#Maximum number reached in the sequence for numbers up to n
def max_max_num_reached(n):
    max_reached = 0
    new_n = 1
    for x in range(1, n + 1):
        max_num = max_num_reached(x)
        if max_num > max_reached:
            max_reached = max_num
            new_n = x
    return [new_n, max_reached]

