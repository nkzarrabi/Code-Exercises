from typing import List, Dict 

def isValid(board: Dict[complex, str], dirs: Dict[str, List[complex]]) -> bool:
    def dfs(board, dirs, visited, r, c, i):
        if i == r + 1j * c: return True
        visited[i] = 1
        for di in dirs[board[i]]:
            z = i + di
            if board[z] == '.': continue   
            if z in board and not visited.get(z, 0) and -di in dirs[board[z]]:
                if dfs(board, dirs, visited, r, c, z): return True
        return False
    r, c = max(int(z.real) for z in board.keys()), max(int(z.imag) for z in board.keys())
    visited = {}
    return dfs(board, dirs, visited, r, c, 0)



pipes = ['S7-J', '.|.|', '.L-7', '...L']
board = {i + 1j * k: x for i, l in enumerate(pipes) for k, x in enumerate(l)}
dirs = {
        "|": [1, -1],
        "-": [1j, -1j],
        "J": [-1, -1j],
        "F": [1, 1j],
        "S": [1, 1j],
        "7": [1, -1j],
        "L": [-1, 1j],
        #"+": [1, -1, 1j, -1j],
        #'.': [0,0j],
    }


print(pipes, isValid(board, dirs))
