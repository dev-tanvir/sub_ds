#test with pytest!!
def factorial(n):
    if n < 0:
        return None
    elif n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(4))
    print(factorial(3))
    print(factorial(2))
    print(factorial(1))
    print(factorial(-1))
    print(factorial(0))
