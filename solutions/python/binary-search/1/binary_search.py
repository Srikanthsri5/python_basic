def find(search_list, value):
    # Store original indices
    indexed_list = list(enumerate(search_list))
    # Sort based on values, but keep original indices
    indexed_list.sort(key=lambda x: x[1])

    low = 0
    high = len(indexed_list) - 1

    print('test')
    while low <= high:
        mid = (low + high) // 2
        mid_value = indexed_list[mid][1]

        if mid_value == value:
            return indexed_list[mid][0]  # Return original index
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("value not in array")
