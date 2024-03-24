# If the numbers 1-5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# if all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# Note: do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


def number_to_words(n):
    # Define the words for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def word_for_number(n):
        if n < 10:
            return ones[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        elif 20 <= n < 100:
            return tens[n // 10] + (ones[n % 10] if n % 10 != 0 else '')
        elif 100 <= n < 1000:
            return ones[n // 100] + "hundred" + (("and" + word_for_number(n % 100)) if n % 100 != 0 else '')
        elif 1000 <= n < 10000:
            return ones[n // 1000] + "thousand" + (word_for_number(n % 1000) if n % 1000 != 0 else '')
        else:
            return "Number out of range"

    return word_for_number(n)

# Count letters for numbers from 1 to 1000
total_letters = sum(len(number_to_words(i).replace(" ", "")) for i in range(1, 1001))
print(total_letters)
