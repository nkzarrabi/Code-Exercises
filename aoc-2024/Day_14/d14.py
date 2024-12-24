from typing import List, Tuple
from re import findall
from statistics import variance

def parse_input(file_name: str) -> List[Tuple[int, int, int, int]]:
    """Parse robot data from the input file."""
    with open(file_name, 'r') as file:
        robots = [
            tuple(map(int, findall(r"-?\d+", line.strip())))
            for line in file if line.strip()
        ]
    return robots

def simulate_positions(robots: List[Tuple[int, int, int, int]], t: int, width: int, height: int) -> List[Tuple[int, int]]:
    """Simulate robot positions at time t with wrapping."""
    return [
        ((sx + t * vx) % width, (sy + t * vy) % height)
        for sx, sy, vx, vy in robots
    ]

def calculate_best_variances(robots: List[Tuple[int, int, int, int]], width: int, height: int) -> Tuple[int, int]:
    """Calculate the best times for x and y clustering based on variance."""
    bx, bxvar = 0, float('inf')
    by, byvar = 0, float('inf')
    
    for t in range(max(width, height)):  # Only iterate up to the max dimension
        positions = simulate_positions(robots, t, width, height)
        xs, ys = zip(*positions)
        
        # Check variance in x and y
        if (xvar := variance(xs)) < bxvar:
            bx, bxvar = t, xvar
        if (yvar := variance(ys)) < byvar:
            by, byvar = t, yvar

    return bx, by

def find_christmas_tree_with_crt(file_name: str, width: int, height: int) -> int:
    """Use CRT to find the fewest seconds for robots to form the Christmas tree pattern."""
    robots = parse_input(file_name)
    bx, by = calculate_best_variances(robots, width, height)

    # Apply CRT to solve for t
    w_inverse_mod_h = pow(width, -1, height)  # Modular inverse of W mod H
    k = ((by - bx) * w_inverse_mod_h) % height
    t = bx + k * width

    # Debug output
    print(f"bx = {bx}, by = {by}, W^-1 mod H = {w_inverse_mod_h}, k = {k}")
    return t

def solve_both_parts(file_name: str, width: int, height: int, seconds: int) -> None:
    """Solve both Part 1 and Part 2."""
    print("Solving Part 1:")
    robots = parse_input(file_name)
    positions = simulate_positions(robots, seconds, width, height)
    
    # Count robots in each quadrant
    mid_x, mid_y = width // 2, height // 2
    q1 = q2 = q3 = q4 = 0
    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x >= mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y >= mid_y:
            q3 += 1
        elif x >= mid_x and y >= mid_y:
            q4 += 1
    safety_factor = q1 * q2 * q3 * q4
    print(f"Safety factor (Part 1): {safety_factor}\n")

    print("Solving Part 2:")
    time_to_christmas_tree = find_christmas_tree_with_crt(file_name, width, height)
    print(f"Fewest seconds to form the Christmas tree (Part 2): {time_to_christmas_tree}")

# Example usage
if __name__ == "__main__":
    file_name = "input.txt"  # Replace with your actual input file
    width, height, seconds = 101, 103, 100
    solve_both_parts(file_name, width, height, seconds)