"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

import time
import sys


def num_to_letter(num):
    # special cases
    if num in special_dict:
        return special_dict[num]
    num_string = str(num)
    num_digits = len(num_string)
    letter = ""
    # if it is one digit:
    if num_digits == 1:
        num_string = "0" + num_string
    # three digits
    if num_digits == 3:
        letter += "%s hundred" % (ones_dict[int(num_string[0])])
        # reduce to the tens digit
        num_string = num_string[-2:]
        # assert there are only two digits left
        assert len(num_string) == 2
        if num_string == '00':
            return letter
        else:
            letter += " and "
    # tens digit
    tens_digit = num_string[-2]
    if tens_digit == '0':
        letter += ones_dict[int(num_string[-1])]
    elif tens_digit == '1':
        letter += ones_dict[int(num_string[-2:])]
    else:
        letter += "%s" % (tens_dict[int(num_string[-2])])
        if num_string[-1] != '0':
            letter += "-%s" %(ones_dict[int(num_string[-1])])
    return letter


def remove_spaces_and_dashes(string):
    string_copy = string.replace(" ", "")
    string_copy = string_copy.replace("-", "")
    return string_copy

if __name__ == '__main__':
    # dictionary
    special_dict = {0: "zero",
                    1000: "one thousand"}
    ones_dict = {0: "",
                 1: "one",
                 2: "two",
                 3: "three",
                 4: "four",
                 5: "five",
                 6: "six",
                 7: "seven",
                 8: "eight",
                 9: "nine",
                 10: "ten",
                 11: "eleven",
                 12: "twelve",
                 13: "thirteen",
                 14: "fourteen",
                 15: "fifteen",
                 16: "sixteen",
                 17: "seventeen",
                 18: "eighteen",
                 19: "nineteen"}
    tens_dict = {0: "",
                 2: "twenty",
                 3: "thirty",
                 4: "forty",
                 5: "fifty",
                 6: "sixty",
                 7: "seventy",
                 8: "eighty",
                 9: "ninety"}
    # input
    lower_limit = 1
    upper_limit = 1000
    # initialize running time
    start = time.time()
    # number of letters used in total
    num_letters = 0
    for i in range(lower_limit, upper_limit + 1):
        # abort if taking too long
        if (time.time() - start > 30):
            raise Exception("Timeout: Running of script aborted.")
        # print i, num_to_letter(i)
        num_letters += len(remove_spaces_and_dashes(num_to_letter(i)))
    # finalize running time
    stop = time.time()
    # print results
    print "Number of Letters from %s to %s: \t %s" % (lower_limit, upper_limit,
                                                      num_letters)
    print "Running Time:                    \t %.2f sec" % (stop - start)
