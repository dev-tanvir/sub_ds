#not checking every element :P

def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            print(i)
            return i
        i += 1

    print("Nope! not in list!!!")
    return -1

M =[ 1, 2, 4, 56, -87, 9.5, 4, [],'a']
x= -1
y=4

linear_search(M, x)
