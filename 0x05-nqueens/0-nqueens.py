#!/usr/bin/python3
"""Solve N- Queens problem using backtracking algorithm for any N >= 4"""


def checker(sol, row, col):
    """Check if the position is safe to place a queen at.
    Parameters:
        sol (list): list of current positions occupied by the queens.
        row (int): row postion of the new queen to add.
        col (int): column postion of the new queen to add.
    """
    for pos in sol:
        # check horizontals and verticals
        if row == pos[0] or col == pos[1]:
            return False
        # check left and right diagnoals
        if abs(row - pos[0]) == abs(col - pos[1]):
            return False
    return True


def solver(sol, n, col):
    """Solve N-Quens problem for a given N
    Parameters:
        sol (list): list of tuples with the queens positions on the board
        n (int): The size of the chess board
        col (int): col to start with
    """
    if col == n:
        print(sol)
        return

    for row in range(n):
        if checker(sol, row, col):
            # add queen position and try next queen
            sol.append([row, col])
            solver(sol, n, col + 1)
            # remove the last element
            sol.pop()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        for i in range(n):
            sol = [[i, 0]]
            solver(sol, n, 1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
