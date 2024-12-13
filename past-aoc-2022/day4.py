text = {4: open('input4.txt').read().splitlines(), 44: open('example4.txt').read().splitlines()}

print(text[44])  
input = text[4]

l = input
print(l)
# Now split at commas
def count_fully_contained_pairs(assignments):
    overlaps = 0
    for line in assignments:
        # Extracting range values as integers
        first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        # Checking if one range fully contains the other
        # For the first range to fully contain the second, the start of the first must be <= the start of the second
        # and the end of the first must be >= the end of the second, or vice versa.
        if (first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]) or \
           (second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]):
            overlaps += 1
    return overlaps

# Example list of assignment pairs as provided
assignments_example = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]

# Calculate the number of assignment pairs where one range fully contains the other
count_fully_contained_pairs(assignments_example)

print(count_fully_contained_pairs(l))

# Part 2
def count_overlapping_pairs(assignments):
    overlaps = 0
    for line in assignments:
        # Extracting range values as integers
        first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in line.split(",")]
        # Checking for any overlap between the ranges
        # An overlap occurs if the start of one range is less than or equal to the end of the other range and vice versa.
        if (first_pair[1] >= second_pair[0] and first_pair[0] <= second_pair[1]):
            overlaps += 1
    return overlaps



print(count_overlapping_pairs(input))