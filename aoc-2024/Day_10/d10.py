from collections import deque

def parse_input(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]

def find_trailheads(grid):
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_move(grid, current, next_pos):
    rows, cols = len(grid), len(grid[0])
    r, c = next_pos
    cr, cc = current
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] == grid[cr][cc] + 1

# BFS for Part 1 (Count reachable 9s)
def bfs_count_reachable_nines(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set()
    reached_nines = set()
    
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if grid[r][c] == 9:
            reached_nines.add((r, c))
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, down, left, right
            nr, nc = r + dr, c + dc
            if is_valid_move(grid, (r, c), (nr, nc)) and (nr, nc) not in visited:
                queue.append((nr, nc))
    
    return len(reached_nines)

# DFS for Part 2 (Count distinct trails)
def dfs_count_trails(grid, current, visited):
    rows, cols = len(grid), len(grid[0])
    r, c = current

    # If we've reached a 9, this is a valid trail endpoint
    if grid[r][c] == 9:
        return 1

    visited.add((r, c))
    total_trails = 0

    # Try moving in all four directions (up, down, left, right)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
            total_trails += dfs_count_trails(grid, (nr, nc), visited.copy())

    return total_trails

# Calculate scores for both parts
def calculate_scores(grid):
    trailheads = find_trailheads(grid)
    total_score_part1 = 0
    total_rating_part2 = 0

    for trailhead in trailheads:
        # Part 1: Count reachable 9s
        total_score_part1 += bfs_count_reachable_nines(grid, trailhead)
        # Part 2: Count distinct trails
        total_rating_part2 += dfs_count_trails(grid, trailhead, set())

    return total_score_part1, total_rating_part2

# Main execution
if __name__ == "__main__":
    input_file = "input.txt"
    grid = parse_input(input_file)
    part1_score, part2_rating = calculate_scores(grid)
    print("Part 1 (Sum of Scores):", part1_score)
    print("Part 2 (Sum of Ratings):", part2_rating)