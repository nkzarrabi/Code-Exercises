'''

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?


'''

def count_xmas(grid):
    # Grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Define directions: right, left, down, up, diagonal down-right, diagonal up-right, diagonal down-left, diagonal up-left
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, 1),  # Diagonal up-right
        (1, -1),  # Diagonal down-left
        (-1, -1)  # Diagonal up-left
    ]
    target = "XMAS"
    target_len = len(target)
    count = 0

    # Traverse each cell
    for r in range(rows):
        for c in range(cols):
            # Check all directions
            for dr, dc in directions:
                match = True
                for i in range(target_len):
                    nr, nc = r + dr * i, c + dc * i  # Next row and column
                    # Check bounds and character match
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != target[i]:
                        match = False
                        break
                if match:
                    count += 1
    return count

def main():
    # File name
    f = 'input.txt'
    
    try:
        # Read the file and strip whitespace from each line
        with open(f, 'r') as file:
            grid = [line.strip() for line in file.readlines() if line.strip()]
        
        # Verify grid dimensions (should be rectangular)
        if not all(len(row) == len(grid[0]) for row in grid):
            raise ValueError("Grid rows are not of consistent length!")
        
        # Log the grid for debugging
        print("Grid:")
        for row in grid:
            print(row)
        
        # Count occurrences of XMAS
        result = count_xmas(grid)
        print("Total occurrences of XMAS:", result)
    
    except FileNotFoundError:
        print(f"Error: File '{f}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


## Part 2 
def count_x_mas(grid):
    # Grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Define MAS strings (forward and backward)
    mas_variants = {"MAS", "SAM"}
    count = 0

    # Traverse the grid, leaving space for a 3x3 region
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check diagonals for the X-MAS pattern
            left_diag = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
            right_diag = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]
            
            # Check if the center is "A" and both diagonals are valid "MAS"
            if grid[r][c] == "A" and left_diag in mas_variants and right_diag in mas_variants:
                count += 1

    return count


def main2():
    # File name
    #f = 'example.txt'
    f = 'input.txt'
    try:
        # Read the file and strip whitespace from each line
        with open(f, 'r') as file:
            grid = [line.strip() for line in file.readlines() if line.strip()]
        
        # Verify grid dimensions (should be rectangular)
        if not all(len(row) == len(grid[0]) for row in grid):
            raise ValueError("Grid rows are not of consistent length!")
        
        # Log the grid for debugging
        print("Grid:")
        for row in grid:
            print(row)
        
        # Count occurrences of X-MAS
        result = count_x_mas(grid)
        print("Total occurrences of X-MAS:", result)
    
    except FileNotFoundError:
        print(f"Error: File '{f}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
    main2()