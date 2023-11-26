SAMPLE = [2, 3, 8, 0, 0, 8, 3, 2]


def recurring_character_nesting(original):
    """Get first recurring character using nested loops. Return first recurring character"""
    recurring_distance = len(original) - 1
    recurring_character = None
    for sample_index in range(len(original)):
        for check_index in range(sample_index + 1, len(original)):
            if original[sample_index] == original[check_index]:
                if check_index - sample_index < recurring_distance:
                    recurring_distance = check_index - sample_index
                    recurring_character = original[sample_index]

    if recurring_distance == len(original) - 1:
        if original[0] == original[-1]:
            recurring_character = original[0]
        else:
            return None
    return recurring_character


def recurring_character_hash(original):
    """Get first recurring character using hash. Return first recurring character."""
    recurring_hash = {}
    for char in original:
        if char in recurring_hash:
            return char
        else:
            recurring_hash[char] = char
    return None


print(f"SAMPLE: {SAMPLE}")
print(f"Recurring character(Nesting): {recurring_character_nesting(SAMPLE)}")
print(f"Recurring character(Hash): {recurring_character_hash(SAMPLE)}")
