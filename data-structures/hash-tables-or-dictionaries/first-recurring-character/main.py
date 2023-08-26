def first_recurring_character_nested(query_array):
    """Returns the first recurring character based on the query array provided."""
    short_index = 20000
    for check_index in range(len(query_array)):
        temp = query_array[check_index]

        for loop_index in range(check_index + 1, len(query_array)):
            if temp == query_array[loop_index]:
                if loop_index < short_index:
                    short_index = loop_index
                    first_recurring = query_array[loop_index]

    return first_recurring


def first_recurring_character_hash(query_array):
    """Returns the first recurring character based on the query array provided."""
    query_map = {}
    for index in range(len(query_array)):
        if query_array[index] in query_map:
            return query_array[index]
        else:
            query_map[query_array[index]] = index


print(first_recurring_character_nested([2, 5, 5, 1, 3, 1, 2, 4]))
print(first_recurring_character_hash([2, 5, 5, 1, 3, 1, 2, 4]))
