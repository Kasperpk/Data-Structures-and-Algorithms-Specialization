import heapq
def parallel_processing(n,m, jobs):
    
    heap = []
    for i in range(0,n):
        heap.append((0,i))
    heapq.heapify(heap)

    output = []

    for t in jobs:
        next_available_thread = heapq.heappop(heap)

        output.append((next_available_thread[1], next_available_thread[0]))

        new_free_time = next_available_thread[0] + t

        heapq.heappush(heap,(new_free_time, next_available_thread[1]))

    return output

if __name__ == "__main__":
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == m

    result = parallel_processing(n, m, jobs)

    for thread_id, start_time in result:
        print(thread_id, start_time)