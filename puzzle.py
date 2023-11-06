"""
Lab 8 task 2
Puzzle game
repository: https://github.com/Danylo-Ik/Ikonnikov_Danyil_lab8_task2
"""
def validate_board(board: list) -> bool:
    """
    list(str) -> bool
    >>> board = [\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
]
    >>> validate_board(board)
    False
    """
    lines = []
    rows = []
    #Check for repeats in lines
    for i in board:
        lines.append([char for char in i])
    for line in lines:
        for el in line:
            if el.isdigit() and line.count(el) > 1 or 0 < int(el) < 10:
                return False
    #Check for repeats in rows
    for i in range(len(lines[0])):
        row = []
        for line in lines:
            row.append(line[i])
        rows.append(row)
    for row in rows:
        for el in row:
            if el.isdigit() and row.count(el) > 1 or 0 < int(el) < 10:
                return False
    

board = [ "**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]
print(validate_board(board))

