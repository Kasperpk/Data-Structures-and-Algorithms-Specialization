def fibonacci(n):

    if n <= 1:
        return n

    numbers = [0] * (n+1)
    numbers[0] = 0
    numbers[1] = 1

    for i in range(2,n+1):
        numbers[i] = fibonacci(i-1) + fibonacci(i-2)

    return numbers[n]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    n = int(input())
    result = fibonacci(n)
    print(result)
