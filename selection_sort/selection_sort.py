def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



def main():
    print("Enter a list of numbers separated by spaces: ")  
    unsorted_list = list(map(int, input().split()))
    if not unsorted_list:
        print("The list is empty.")
    sorted_list = selection_sort(unsorted_list)
    print("Sorted list is:", sorted_list)


if __name__ == "__main__":
    main()

#this is a comment

    # TODO: Implement selection sort
    pass
