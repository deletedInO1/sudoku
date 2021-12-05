import time

from backtracking import Backtracking

first_board = [
    [0, 6, 0, 5, 0, 8, 7, 0, 3],
    [9, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [5, 0, 8, 0, 0, 3, 0, 0, 9],
    [0, 7, 3, 0, 0, 1, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 1, 0, 0, 0, 0, 3, 2, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 6, 0, 5, 0, 0]
]

def check_row(board, x, y):
    for i in range(9):
        if board[y][x] == board[y][i] and x != i:
            return False
    return True

def check_column(board, x, y):
    for i in range(9):
        if board[y][x] == board[i][x] and i != y:
            return False
    return True

def check_box(board, x, y):
    box_x = x // 3
    box_y = y // 3
    for i in range(3):
        for j in range(3):
            i2 = i + 3*box_x
            j2 = j + 3*box_y
            if x == i2 and y == j2:
                continue
            if board[y][x] == board[j2][i2]:
                return False
    return True

class SudokuSolver(Backtracking):

    def __init__(self):
        super(SudokuSolver, self).__init__()
        self.get_row = lambda state, y: state[y]
        self.get_column = lambda state, x: [state[y][x] for y in range(len(state))]

    def get_possible_states(self, state, pos):
        l = []
        x = pos % 9
        y = pos // 9
        if state[y][x] != 0:
            return [state]
        forbidden = self.get_row(state, y) + self.get_column(state, x) + self.get_box(state, x, y)
        opportunities = list(range(1, 10))
        for f in forbidden:
            if f in opportunities:
                opportunities.remove(f)
        for o in opportunities:
            c = self.copy(state)
            c[y][x] = o
            l.append(c)

        return l

    def get_box(self, state, x, y):
        bx = x // 3
        by = y // 3
        box = []
        for i in range(3):
            for j in range(3):
                box.append(state[by*3+j][bx*3+i])
        return box


    def copy(self, state):
        new = []
        for row in state:
            new_r = []
            for v in row:
                new_r.append(v)
            new.append(new_r)
        return new


    def end(self, pos):
        return pos >= 81


if __name__ == '__main__':
    #b = solve(first_board[:], 0, 0)
    #exit()
    solution = [
        [1, 6, 2, 5, 4, 8, 7, 9, 3],
        [9, 8, 5, 7, 3, 2, 4, 6, 1],
        [3, 4, 7, 9, 1, 6, 2, 8, 5],
        [5, 2, 8, 6, 7, 3, 1, 4, 9],
        [6, 7, 3, 4, 9, 1, 8, 5, 2],
        [4, 9, 1, 2, 8, 5, 6, 3, 7],
        [7, 1, 6, 8, 5, 9, 3, 2, 4],
        [8, 5, 4, 3, 2, 7, 9, 1, 6],
        [2, 3, 9, 1, 6, 4, 5, 7, 8],
    ]
    solver = SudokuSolver()
    lel = [[0 for i in range(9)] for j in range(9)]
    b = solver.solve(lel)
    # count = 0
    # t_sum = 0
    # for i in range(1000):
    #     t1 = time.time()
    #     b = solver.solve(first_board)
    #     t2 = time.time()
    #     count += 1
    #     t = t2-t1
    #     t_sum += t
    # print(t_sum / count)
    for i in range(9):
        for j in range(9):
            if not check_row(solution, i, j) or not check_column(solution, i, j) or not check_box(solution, i, j):
                print("!")
    #print(b)
    for i in range(9):
        for j in range(9):
            if solution[i][j] != b[i][j]:
                print('!')
    for row in b:
        print(row)
