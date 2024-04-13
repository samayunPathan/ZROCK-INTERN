def find_index(lst, element):
    return lst.index(element)
    
my_list = [1, 2, 3, 4, 5]
index = find_index(my_list, 3)
if index:
    print(f"Element found at index: {index}")
else:
    print("Element not found.")
