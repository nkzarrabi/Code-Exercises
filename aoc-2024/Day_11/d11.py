from collections import Counter

def simulate_stone_blinks_optimized(input_file, blinks):
    with open(input_file, 'r') as file:
        # Read the initial stone arrangement from the file
        stones = list(map(int, file.readline().strip().split()))
    
    # Use a Counter to track the number of stones with each value
    stone_counts = Counter(stones)
    
    for _ in range(blinks):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count
        stone_counts = new_counts
    
    # Return the total number of stones
    return sum(stone_counts.values())

# Example usage
input_file = 'input.txt'  # File containing the initial stone arrangement
blinks = 75  # Number of blinks
result = simulate_stone_blinks_optimized(input_file, blinks)
print(f"Number of stones after {blinks} blinks: {result}")