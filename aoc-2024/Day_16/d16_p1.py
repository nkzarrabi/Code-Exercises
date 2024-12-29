import heapq

def parse_maze(maze):
    start = None
    end = None
    grid = []
    for y, line in enumerate(maze.strip().split("\n")):
        row = list(line)
        grid.append(row)
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return grid, start, end

def lowest_score(maze):
    # Parse the maze
    grid, start, end = parse_maze(maze)
    
    # Directions: 0=East, 1=South, 2=West, 3=North
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue for BFS
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0))  # (score, x, y, direction)
    
    # Visited set to track the minimum score for a given state (x, y, direction)
    visited = {}
    
    while pq:
        score, x, y, direction = heapq.heappop(pq)
        
        # If reached the end, return the score
        if (x, y) == end:
            return score
        
        # If this state has been visited with a lower score, skip it
        if (x, y, direction) in visited and visited[(x, y, direction)] <= score:
            continue
        visited[(x, y, direction)] = score
        
        # Explore moves
        # 1. Move forward
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] != '#':
            heapq.heappush(pq, (score + 1, nx, ny, direction))
        
        # 2. Turn clockwise
        heapq.heappush(pq, (score + 1000, x, y, (direction + 1) % 4))
        
        # 3. Turn counterclockwise
        heapq.heappush(pq, (score + 1000, x, y, (direction - 1) % 4))

# Example usage
test = 0


if test:
    file_name = "example.txt"
else:
    file_name = "input.txt"

maze = open(file_name).read()

print(lowest_score(maze))