def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


def main():
    print("Enter a list of numbers separated by spaces: ")
    unsorted_list = list(map(int, input().split()))    
    if not unsorted_list:
        print("The list is empty.")
    sorted_list = bubble_sort(unsorted_list)
    print("Sorted list is:", sorted_list)
        

if __name__ == "__main__":
    main()        

#this is a comment
    
