import os

def read_input_file():
    # Check for 'example.txt' first, fallback to 'input.txt'
    flag = False
    filename = "example.txt" if flag else "input.txt"
    
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n")
    
    # Parse input
    towel_patterns = lines[0].split(", ")
    designs = lines[2:]  # Skip the blank line and the towel patterns line
    return towel_patterns, designs

def count_design_arrangements(towel_patterns, designs):
    # Convert towel patterns into a set for fast lookup
    towel_set = set(towel_patterns)
    
    def count_ways_to_form(design):
        # Use memoization to store results for substrings
        memo = {}
        
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == "":
                return 1  # 1 way to form an empty string
            total_ways = 0
            for i in range(1, len(remaining) + 1):
                if remaining[:i] in towel_set:
                    total_ways += dfs(remaining[i:])  # Explore the remaining substring
            memo[remaining] = total_ways
            return total_ways
        
        return dfs(design)
    
    # Count the total ways for all designs
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form(design)
    
    return total_ways

# Main execution
if __name__ == "__main__":
    towel_patterns, designs = read_input_file()
    result = count_design_arrangements(towel_patterns, designs)
    print(f"Total number of ways to arrange designs: {result}")