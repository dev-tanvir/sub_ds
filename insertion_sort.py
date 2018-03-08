import time


def insertion_sort(L):
    n = len(L)

    for i in range(1, n):
        item = L[i]
        j = i-1

        while j >= 0 and L[j] > item:
            L[j+1] = L[j]
            j = j-1

        L[j+1] = item


if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print("before: ", L)
    start_program_time = time.time()
    insertion_sort(L)
    program_end_time = time.time() - start_program_time
    print("time taken:", program_end_time, "seconds")
    print("After: ", L)