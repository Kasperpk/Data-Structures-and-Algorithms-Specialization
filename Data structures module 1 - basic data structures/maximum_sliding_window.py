def max_sliding_window(n, integers, m):
    from collections import deque

    if not integers or m == 0:
        return []

    result = []
    dq = deque()

    for i in range(n):
        # Remove elements not in the current window
        if dq and dq[0] < i - m + 1:
            dq.popleft()

        # Remove elements smaller than the current element from the deque
        while dq and integers[dq[-1]] < integers[i]:
            dq.pop()

        dq.append(i)

        # The first index where we have a full window
        if i >= m - 1:
            result.append(integers[dq[0]])

    return result

if __name__ == "__main__":
    n = int(input().strip())
    integers = list(map(int, input().strip().split()))
    m = int(input().strip())
    result = max_sliding_window(n, integers, m)
    print(" ".join(map(str, result)))