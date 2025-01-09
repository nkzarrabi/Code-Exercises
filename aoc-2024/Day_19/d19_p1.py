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

def count_possible_designs(towel_patterns, designs):
    # Convert towel patterns into a set for fast lookup
    towel_set = set(towel_patterns)
    
    def can_form_design(design):
        # Use memoization to avoid recalculating for the same design
        memo = {}
        
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == "":
                return True
            for i in range(1, len(remaining) + 1):
                if remaining[:i] in towel_set and dfs(remaining[i:]):
                    memo[remaining] = True
                    return True
            memo[remaining] = False
            return False
        
        return dfs(design)
    
    # Count designs that can be formed
    possible_count = 0
    for design in designs:
        if can_form_design(design):
            possible_count += 1
    
    return possible_count

# Main execution
if __name__ == "__main__":
    towel_patterns, designs = read_input_file()
    result = count_possible_designs(towel_patterns, designs)
    print(f"Number of possible designs: {result}")