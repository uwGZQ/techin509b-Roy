from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    
    # Input validation
    if not (0 <= x < len(input_board) and 0 <= y < len(input_board[0])):
        raise ValueError("Invalid x or y coordinates.")
    if not (len(old) == 1 and len(new) == 1):
        raise ValueError("Old and new values should be single characters.")

    queue = [(x, y)]
    visited = set()

    mutable_board = [list(row) for row in input_board]

    def is_valid(x, y):
        return 0 <= x < len(input_board) and 0 <= y < len(input_board[0])

    while queue:
        x, y = queue.pop(0)  
        
        if (x, y) in visited or mutable_board[x][y] != old:
            continue

        mutable_board[x][y] = new

        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                queue.append((new_x, new_y))

    return [''.join(row) for row in mutable_board]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)