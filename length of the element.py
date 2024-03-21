def sort_list_by_length(lst):
    return sorted(lst, key=len)
input_list = ["apple", "banana", "orange"]
sorted_list = sort_list_by_length(input_list)
print("Sorted list by length:", sorted_list)

