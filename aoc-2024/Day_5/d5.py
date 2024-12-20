from collections import defaultdict, deque

def parse_input_from_file(filename):
    """
    Reads the input from a file and splits it into ordering rules and updates.
    """
    with open(filename, 'r') as file:
        sections = file.read().strip().split("\n\n")
    # Parse ordering rules
    ordering_rules = [tuple(map(int, line.split("|"))) for line in sections[0].strip().split("\n")]
    # Parse updates
    updates = [list(map(int, line.split(","))) for line in sections[1].strip().split("\n")]
    return ordering_rules, updates

def is_valid_update(update, ordering_rules):
    """
    Checks if an update follows the given ordering rules.
    """
    for x, y in ordering_rules:
        if x in update and y in update:
            # Ensure x comes before y in the update
            if update.index(x) > update.index(y):
                return False
    return True

def calculate_middle_sum(ordering_rules, updates):
    """
    Calculates the sum of the middle page numbers of all valid updates.
    """
    valid_updates = []
    for update in updates:
        if is_valid_update(update, ordering_rules):
            valid_updates.append(update)
    
    middle_sum = 0
    for update in valid_updates:
        # Find the middle index of the update
        middle_index = len(update) // 2
        # Add the middle page number to the sum
        middle_sum += update[middle_index]
    return middle_sum

def reorder_update(update, ordering_rules):
    """
    Reorders an update to satisfy the ordering rules using topological sorting.
    """
    # Build a graph of dependencies
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set(update)

    for x, y in ordering_rules:
        if x in nodes and y in nodes:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def calculate_reordered_middle_sum(ordering_rules, updates):
    """
    Calculates the sum of middle page numbers for reordered invalid updates.
    """
    invalid_updates = []
    for update in updates:
        if not is_valid_update(update, ordering_rules):
            invalid_updates.append(update)
    
    middle_sum = 0
    for update in invalid_updates:
        reordered = reorder_update(update, ordering_rules)
        middle_index = len(reordered) // 2
        middle_sum += reordered[middle_index]
    return middle_sum

# Main execution for Part 1
if __name__ == "__main__":
    # File name containing input data
    filename = "input.txt"  # Replace with the actual file name if different
    
    # Parse the input file
    ordering_rules, updates = parse_input_from_file(filename)
    
    # Calculate the sum of the middle page numbers for valid updates (Part 1)
    part1_result = calculate_middle_sum(ordering_rules, updates)
    print("Part 1: Sum of middle page numbers:", part1_result)
    
    # Calculate the sum of the middle page numbers for reordered invalid updates (Part 2)
    part2_result = calculate_reordered_middle_sum(ordering_rules, updates)
    print("Part 2: Sum of middle page numbers after reordering:", part2_result)