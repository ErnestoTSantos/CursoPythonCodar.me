def reverse_list(list_items):
    numItems = len(list_items) - 1

    i = numItems

    reverse_elements = []

    while i > -1:
        reverse_elements.append(list_items[i])
        i -= 1

    return(reverse_elements)


elements = ["a", 5, "Texto", [4.5], {1}, 8]

elements_reverse = reverse_list(elements)
print(elements_reverse)
