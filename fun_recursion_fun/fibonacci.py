def fibonacci(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))