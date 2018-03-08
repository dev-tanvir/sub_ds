import time


def selection_sort(L):
    n = len(L)

    for i in range(0, n-1):
        index_min = i

        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j

        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]


if __name__ == "__main__":
    L = [6,1, 4, 9, 2]
    print("before: ", L)
    start_program_time = time.time()
    selection_sort(L)
    program_end_time = time.time() - start_program_time
    print("time taken:", program_end_time, "seconds")
    print("After: ", L)