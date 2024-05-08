#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(roman_string)):
        current_val = roman_dict[roman_string[i]]
        if i + 1 < len(roman_string):
            next_val = roman_dict[roman_string[i + 1]]
            if current_val < next_val:
                result -= current_val
                continue
            else:
                result += current_val
                continue
        else:
            result += current_val
    return result
