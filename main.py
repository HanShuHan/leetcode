def fibonacci(n: int):
    if n < 0:
        raise ValueError('Cannot be negative')
    if n == 0 or n == 1:
        return 1

    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, (a + b)
    return b


def recursive_fibonacci(n: int):
    if n < 0:
        raise ValueError('Cannot be negative')
    if n == 0 or n == 1:
        return 1

    return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)


if __name__ == '__main__':
    # Start from here
    result = fibonacci(1000)
    print(result)
