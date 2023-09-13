def first_recurring_character_nested(sample_array):
    """Finds the first recurring character based on the sample provided using nested loops."""
    does_exist = False
    first_recurring = sample[0]
    recurring_distance = len(sample) - 1
    for sample_index in range(len(sample)):
        for check_index in range(sample_index + 1, len(sample)):
            if sample[sample_index] == sample[check_index] and recurring_distance > check_index - sample_index:
                recurring_distance = check_index - sample_index
                first_recurring = sample[sample_index]
                does_exist = True
    if recurring_distance == len(sample) - 1:
        if does_exist:
            print(f"First recurring character (nested): {first_recurring}")
        else:
            print("No recurring characters.")
    else:
        print(f"First recurring character (nested): {first_recurring}")


def first_recurring_character_hash(sample_array):
    """Finds the first recurring character based on the sample provided using hash tables."""
    sample_hash = {}
    for character_index in range(len(sample)):
        if sample[character_index] not in sample_hash.keys():
            sample_hash[sample[character_index]] = sample[character_index]
        else:
            print(f"First recurring character (hash): {sample_hash[sample[character_index]]}")
            return True


sample = [2, 5, 5, 1, 3, 1, 2, 4]
first_recurring_character_nested(sample)
first_recurring_character_hash(sample)
