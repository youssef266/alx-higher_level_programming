#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        sum_val = 0
        number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(roman_string)):

            if i == len(roman_string) - 1:
                sum_val += number[roman_string[i]]

            elif number[roman_string[i + 1]] <= number[roman_string[i]]:
                sum_val += number[roman_string[i]]

            else:
                sum_val -= number[roman_string[i]]

        return (sum_val)
    else:
        return (0)
