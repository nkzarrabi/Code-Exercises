'''

Day 1: Historian Hysteria 

As each location is checked, they will mark it on their list with a star.
They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, 
you need to help them get fifty stars on their list before Santa takes off on December 25th.


Throughout the Chief's office, 
the historically significant locations are listed not by name but by a unique number called the location ID. 
To make sure they don't miss anything, The Historians split into two groups,
 each searching the office and trying to create their own complete list of location IDs.


'''

# Part 1 

# The Historians have been given a list of location IDs.

# Read the list of location IDs from the file example1.txt 

# We must read the first number of each row and place it in the left list and the second number in the right list.

# Read the file


#file = open("example1.txt", "r")
file = open("day1.txt", "r")
lines = file.readlines()
file.close()

# Create two lists to store the location IDs

left, right = [], []

# Split the location IDs and place them in the left and right lists

for line in lines:
    location = line.split()
    left.append(location[0])
    right.append(location[1])



# Sort the lists from smallest to largest

left.sort()
right.sort()

# Print the left and right lists

print("Left List: ", left)
print("Right List: ", right)

# Take the difference of each number in the two lists 

# Create a list to store the differences

differences = []

# Calculate the differences

for i in range(len(left)):
    # Forgot the abs function
    difference = abs(int(right[i]) - int(left[i]))
    differences.append(difference)

# Print the differences

print("Differences: ", differences)

answer = sum(differences)
print("Answer: ", answer)   


# Part 2 

"""
The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting,
 but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! 
 Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
Calculate a total similarity score by adding up each number in the left list after 
multiplying it by the number of times that number appears in the right list.

"""

# Count how many times each number in the left list appears in the right list

# Create a dictionary to store the counts

counts = {}

# Count the number of times each number in the left list appears in the right list

for number in left:
    count = right.count(number)
    counts[number] = count

# Print the counts

print("Counts: ", counts)

# Calculate the total similarity score

total = 0

for number in left:
    total += int(number) * counts[number]

# Print the total similarity score

print("Total Similarity Score: ", total)

