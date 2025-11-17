
#Takes in a n x n 2D array and checks if it is a magic square
def check_magic(arr):
    n = len(arr)
    #Check all
    lst = []
    for item in arr:
        lst.extend(item)
    if len(set(lst)) != n**2:
        return False
    count = sum(arr[0])
    #Check row
    for i in range(n):
        count_1 = sum(arr[i])
        if count_1 != count:
            return False
    #Check column
    for j in range(n):
        count_2 = 0
        for item in arr:
            count_2 += item[j]
        if count_2 != count:
            return False
    #Check diagonal
    count_3 = 0
    for k in range(n):
        count_3 += arr[k][k]
    if count_3 != count:
        return False
    return True
#Make magic square of size n where n is odd
def make_magic(n:int):
    if not bool(n%2):
        return None
    arr = [[0 for i in range(n)] for j in range(n)]
    arr[0][n//2] = 1
    count = 2
    a,b = 0,n//2
    while count <= n**2:
        a -= 1
        b += 1
        a %= n
        b %= n
        if arr[a][b] != 0:
            a += 1
            b -= 1
            a += 1
            a %= n
            b %= n 
        arr[a][b] = count
        count += 1
    return arr
for i in range(1,8,2):
    for item in make_magic(i):
        print(item)
    print('=======')
