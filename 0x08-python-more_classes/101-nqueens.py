import sys

"""ths model is for """


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in the given row and column of the board.

    Args:
        board (list[list[int]]): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """

    for i in range(col):
        if board[row][i] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    """
    Print the current solution (board) in a readable format.

    Args:
        board (list[list[int]]): The chessboard.
    """
    for row in board:
        print(" ".join(map(str, row)))

def solve_nqueens(n):
    """
    Solve the N-Queens problem and return all possible solutions.

    Args:
        n (int): The size of the board.

    Returns:
        list[list[list[int]]]: List of all possible solutions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

def solve_nqueens_util(board, col, n, solutions):
    """
    Utility function to solve the N-Queens problem recursively.

    Args:
        board (list[list[int]]): The chessboard.
        col (int): Current column.
        n (int): The size of the board.
        solutions (list[list[list[int]]]): List to store solutions.
    """
    if col == n:

        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):

            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)

            board[i][col] = 0

def main():
    """
    Main function to handle command line arguments and execute the program.
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)


    solutions = solve_nqueens(n)


    for solution in solutions:
        print_solution(solution)
        print()

if __name__ == "__main__":
    main()
