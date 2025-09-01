def largest_concatenate(n, integers):
    '''
    :param n: number of lists
    :param integers: list of lists of integers
    :return: concatenation of digits to form the largest possible number
    '''
    # Flatten and extract all digits
    all_digits = []
    for sublist in integers:
        for num in sublist:
            # Convert number to string and extend each digit
            all_digits.extend(list(str(num)))

    # Sort ALL digits in descending order (only once, after collecting all)
    all_digits.sort(reverse=True)

    # Join and return
    return ''.join(all_digits)


if __name__ == "__main__":
    n = int(input())
    integers = [list(map(int, input().split())) for _ in range(n)]
    result = largest_concatenate(n, integers)
    print(result)