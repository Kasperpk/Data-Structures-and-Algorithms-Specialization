def covering_by_segments(segments):
    points = []
    # Sort segments by right endpoint
    segments_sorted = sorted(segments, key=lambda x: x[1])

    while segments_sorted:
        # Pick the right endpoint of the first segment
        point = segments_sorted[0][1]
        points.append(point)

        # Remove all segments that are covered by this point
        # A segment [l,r] is covered by point p if l <= p <= r
        segments_sorted = [seg for seg in segments_sorted if not (seg[0] <= point <= seg[1])]

    return points


if __name__ == "__main__":
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    result = covering_by_segments(segments)
    print(len(result))
    for point in result:
        print(point)