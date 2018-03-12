def fibonacci(n):
    """
    seeing the calling structure of recursion
    in fibonacci
    :param n:int
    :return:
    """
    print("Trying to find fibonacci of",n)
    if n in [1,2]:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(5))