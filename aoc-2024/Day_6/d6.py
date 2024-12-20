def simulate_guard_path(filename, part=1):
    # Read the map from the file
    with open(filename, 'r') as f:
        lab_map = [line.strip() for line in f.readlines() if line.strip()]
    
    # Directions mapping: 0=up, 1=right, 2=down, 3=left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = {"^": 0, ">": 1, "v": 2, "<": 3}
    turn_right = {0: 1, 1: 2, 2: 3, 3: 0}

    # Parse the map dimensions and find guard position
    rows, cols = len(lab_map), len(lab_map[0])
    obstacles = set()
    guard_position = None
    guard_direction = None

    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] == "#":
                obstacles.add((r, c))
            elif lab_map[r][c] in "^>v<":
                guard_position = (r, c)
                guard_direction = direction_index[lab_map[r][c]]

    if not guard_position or guard_direction is None:
        raise ValueError("Guard starting position not found in the map.")

    if part == 1:
        # Part One: Count distinct positions visited
        visited = set()
        visited.add(guard_position)

        while True:
            r, c = guard_position
            dr, dc = directions[guard_direction]
            next_position = (r + dr, c + dc)

            # Check if the guard will leave the map
            if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
                break

            # Check if there's an obstacle ahead
            if next_position in obstacles:
                # Turn right
                guard_direction = turn_right[guard_direction]
            else:
                # Move forward
                guard_position = next_position
                visited.add(guard_position)

        return len(visited)

    elif part == 2:
        # Part Two: Count obstruction positions that create loops
        def simulate_with_obstruction(obstruction):
            visited_states = set()
            position, direction = guard_position, guard_direction

            while True:
                state = (position, direction)
                if state in visited_states:
                    return True  # Loop detected
                visited_states.add(state)
                
                r, c = position
                dr, dc = directions[direction]
                next_position = (r + dr, c + dc)

                # Check if the guard will leave the map
                if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
                    return False
                
                # Check if the next position is blocked
                if next_position in obstacles or next_position == obstruction:
                    direction = turn_right[direction]
                else:
                    position = next_position

        # Precompute reachable positions
        visited_part1 = set()
        queue = [guard_position]
        while queue:
            pos = queue.pop()
            if pos in visited_part1 or pos in obstacles:
                continue
            visited_part1.add(pos)
            for dr, dc in directions:
                next_pos = (pos[0] + dr, pos[1] + dc)
                if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols:
                    queue.append(next_pos)

        # Count valid obstruction positions
        valid_obstructions = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in obstacles and (r, c) != guard_position and (r, c) in visited_part1:
                    if simulate_with_obstruction((r, c)):
                        valid_obstructions += 1

        return valid_obstructions


# Example Usage
filename = "input.txt"

# Part One: Distinct positions visited
result_part1 = simulate_guard_path(filename, part=1)
print(f"Distinct positions visited: {result_part1}")

# Part Two: Valid obstruction positions
result_part2 = simulate_guard_path(filename, part=2)
print(f"Valid obstruction positions: {result_part2}")