def distinct_summands(n):

    numbers_used = []
    current_amount = n
    if current_amount < 1:
        return
    while current_amount != 0:
        for i in range(1,n):
            if current_amount - i > i:
                numbers_used.append(i)
                current_amount = current_amount - i
            elif current_amount - i == 0:
                numbers_used.append(i)
                current_amount = current_amount - i
    return numbers_used


if __name__ == "__main__":
    n = int(input())  # positive integer
    result = distinct_summands(n)
    print(len(result))
    for res in result:
        print(res)