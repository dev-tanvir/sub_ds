
def linear_search(L, x):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            print(i)
            return i
        i += 1
    print("not in list! :-( ")
    return -1

L = [1,3,5,6,7,88,90,-45,678]
x=90
linear_search(L, 678)

