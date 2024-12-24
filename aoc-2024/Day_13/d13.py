import math
from typing import List, Tuple, Optional

# Utility: Extended Euclidean Algorithm to solve ax + by = gcd(a, b)
def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

# Part 1: Calculate minimum tokens using a brute-force approach
def calculate_minimum_tokens(Ax: int, Ay: int, Bx: int, By: int, Px: int, Py: int) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    min_cost = math.inf
    best_na, best_nb = None, None

    for nA in range(101):  # Iterate over possible values of nA
        remaining_x = Px - nA * Ax
        remaining_y = Py - nA * Ay

        # Check if remaining_x and remaining_y can be fulfilled by B button presses
        if remaining_x % Bx == 0 and remaining_y % By == 0:
            nB_x = remaining_x // Bx
            nB_y = remaining_y // By

            if nB_x == nB_y and nB_x >= 0:  # Ensure valid nB
                nB = nB_x
                cost = 3 * nA + 1 * nB
                if cost < min_cost:
                    min_cost, best_na, best_nb = cost, nA, nB

    return min_cost if min_cost < math.inf else None, best_na, best_nb

# Part 2: Solve for large prize coordinates using Diophantine equations

def determinant(matrix: List[List[int]]) -> int:
    """Calculate the determinant of a 2x2 matrix."""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def cramer_solve(Ax: int, Ay: int, Bx: int, By: int, Px: int, Py: int) -> Optional[Tuple[int, int]]:
    """Solve the linear system using Cramer's Rule."""
    # The determinant of the coefficient matrix
    det_coeff = determinant([[Ax, Bx], [Ay, By]])
    if det_coeff == 0:
        return None  # No unique solution

    # Determinants for n_A and n_B
    det_nA = determinant([[Px, Bx], [Py, By]])
    det_nB = determinant([[Ax, Px], [Ay, Py]])

    # Solve for n_A and n_B
    nA = det_nA / det_coeff
    nB = det_nB / det_coeff

    if nA.is_integer() and nB.is_integer() and nA >= 0 and nB >= 0:
        return int(nA), int(nB)
    return None

def find_min_cost_cramer(Ax: int, Ay: int, Bx: int, By: int, Px: int, Py: int) -> Optional[int]:
    """Calculate minimum tokens using Cramer's Rule."""
    solution = cramer_solve(Ax, Ay, Bx, By, Px, Py)
    if solution is None:
        return None
    nA, nB = solution
    return 3 * nA + 1 * nB

# File parser to process machines and prize data
def process_file(filename: str, offset: int = 0) -> List[Tuple[int, int, int, int, int, int]]:
    machines = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in range(0, len(lines), 3):
            Ax, Ay = map(int, lines[i].split(": ")[1].replace("X+", "").replace("Y+", "").split(", "))
            Bx, By = map(int, lines[i + 1].split(": ")[1].replace("X+", "").replace("Y+", "").split(", "))
            Px, Py = map(int, lines[i + 2].split(": ")[1].replace("X=", "").replace("Y=", "").split(", "))
            machines.append((Ax, Ay, Bx, By, Px + offset, Py + offset))
    return machines

# Main function to compute results for both parts
def main(input_file: str):
    machines = process_file(input_file)

    # Part 1: Solve using brute-force approach
    print("Part 1: Brute-force solution")
    total_cost_part1 = 0
    prizes_won_part1 = 0

    for idx, machine in enumerate(machines):
        min_cost, best_na, best_nb = calculate_minimum_tokens(*machine)
        if min_cost is not None:
            total_cost_part1 += min_cost
            prizes_won_part1 += 1
            print(f"Machine {idx + 1}: Minimum Tokens = {min_cost}, Button A = {best_na}, Button B = {best_nb}")
        else:
            print(f"Machine {idx + 1}: No solution")

    print(f"Total Prizes Won (Part 1): {prizes_won_part1}")
    print(f"Total Tokens Spent (Part 1): {total_cost_part1}\n")

    # Part 2: Solve for large coordinates
    print("Part 2: Diophantine solution")
    # Part 2: Solve for large coordinates using Cramer's Rule
    print("Part 2: Using Cramer's Rule")
    machines_offset = process_file(input_file, offset=10**13)
    total_cost_part2 = 0
    prizes_won_part2 = 0

    for idx, machine in enumerate(machines_offset):
        min_cost = find_min_cost_cramer(*machine)
        if min_cost is not None:
            total_cost_part2 += min_cost
            prizes_won_part2 += 1

    print(f"Total Prizes Won (Part 2): {prizes_won_part2}")
    print(f"Total Tokens Spent (Part 2): {total_cost_part2}")

# Entry point
if __name__ == "__main__":
    input_file = "input.txt"  # Change this to "example.txt" for testing
    main(input_file)