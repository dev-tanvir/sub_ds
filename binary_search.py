def binary_search(l, x):
    left, right = 0, len(l)-1

    while left <= right:
        mid = (left + right) // 2

        if l[mid] == x:
            return mid


        if l[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    l = [1,2,3,5,6,7,8,9]

    for x in range(1, 11):
        position = binary_search(l, x)
        print(l)
        print("========================")
        print(x)
        print("------------------------")
        
        if position == -1:
            if x in l:
                print(x, "is in list, but function returned -1")
            else:
                print(x, "not in list")
        else:
            if l[position] == x:
                print(x, "found in correct position", "and position in list is", position)
            else:
                print("binary search returned ", position, "for", x, "which is incorrect")
    print("program terminated")    
