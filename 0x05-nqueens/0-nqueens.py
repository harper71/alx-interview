#!/usr/bin/python3
import sys
""" Nqueen problem """
def print_usage_and_exit():
    """prints exist"""
    print("Usage: nqueens N")
    sys.exit(1)

def is_integer(s):
    """check if the list is integer"""
    try:
        int(s)
        return True
    except ValueError:
        return False

def solve_nqueens(N):
    """the n queen solution"""
    def can_place(queens, row, col):
        """places the number"""
        for i in range(row):
            if queens[i] == col or \
               queens[i] - i == col - row or \
               queens[i] + i == col + row:
                return False
        return True

    def place_queen(queens, row):
        """places the queen"""
        if row == N:
            solutions.append(queens[:])
            return
        for col in range(N):
            if can_place(queens, row, col):
                queens[row] = col
                place_queen(queens, row + 1)
    
    solutions = []
    queens = [-1] * N
    place_queen(queens, 0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    arg = sys.argv[1]

    if not is_integer(arg):
        print("N must be a number")
        sys.exit(1)

    N = int(arg)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

if __name__ == "__main__":
    main()
