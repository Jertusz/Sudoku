from random import shuffle, randint
from time import sleep
import copy


class Node:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = 0 
        

    def get_pos(self):
        return [self.row, self.col]


    def is_filled(self):
        return self.value != 0


    def set_value(self, number):
        self.value = number


    def get_value(self):
        return self.value


# class Cube:
# 
#     def __init__(self, number):
#         self.number = number
#         self.nodes = self.generate_nodes()
# 
# 
#     def get_pos(self):
#         return self.number 
# 
# 
#     def get_nodes(self):
#         return self.nodes
# 
# 
#     def generate_nodes(self):
#         col = 0
#         nodes = []
#         for i in range(9):
#             row = i%3
#             if col == 3:
#                 col = 0
#             nodes.append(Node(row, col))
#             col += 1
#         return nodes


class Grid:

    def __init__(self):
        self.size = 9
        self.nodes = self.generate_nodes()
        self.num_list = [1,2,3,4,5,6,7,8,9]
        self.counter = 0


    def get_nodes(self):
        return self.nodes


    def set_nodes(self, nodes):
        self.nodes = nodes


    def generate_nodes(self):
        nodes = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(Node(i, j))
            nodes.append(row)
        return nodes


    def get_counter(self):
        return self.counter


    def set_counter(self, val):
        self.counter = val


    def print_grid(self):   # for debug purposes only
        for row in self.get_nodes():
            for node in row:
                print(node.get_value(), end="\t")
            print("\n")
            print("\n")


    def check_grid(self):
        nodes = self.get_nodes()
        for row in nodes:
            for col in range(9):
                if not row[col].is_filled():
                    return False

        return True


    def get_row_values(self, row):
        vals = []
        for node in self.get_nodes()[row]:
            vals.append(node.get_value())

        return vals


    def get_col_values(self, col):
        vals = []
        for i in range(9):
            node = self.get_nodes()[i][col] 
            vals.append(node.get_value())

        return vals


    def get_square(self, end_col, end_row):
        start_col = end_col - 3
        start_row = end_row - 3
        square = []
        for i in range(start_row, end_row):
            square.append(self.get_nodes()[i][start_col:end_col])
        return square


    def solve(self):
        for i in range(0, 81):
            row = i//9
            col = i%9
            if self.get_nodes()[row][col].get_value() == 0:
                for value in range(1, 10):
                    if value not in self.get_row_values(row):
                        if value not in self.get_col_values(col):
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = self.get_square(3, 3)
                                elif col < 6:
                                    square = self.get_square(6, 3)
                                else:
                                    square = self.get_square(9, 3)
                            elif row < 6:
                                if col < 3:
                                    square = self.get_square(3, 6)
                                elif col < 6:
                                    square = self.get_square(6, 6)
                                else:
                                    square = self.get_square(9, 6)
                            else:
                                if col < 3:
                                    square = self.get_square(3, 9)
                                elif col < 6:
                                    square = self.get_square(6, 9)
                                else:
                                    square = self.get_square(9, 9)
                            square_vals = []
                            for rows in square:
                                for node in rows:
                                    square_vals.append(node.get_value())
                            if value not in square_vals:
                                self.get_nodes()[row][col].set_value(value)
                                if self.check_grid():
                                    self.set_counter(self.get_counter()+1)
                                    break
                                else:
                                    if self.solve():
                                        return True

                break
        self.get_nodes()[row][col].set_value(0)


    def fill(self):
        for i in range(0, 81):
            row = i//9
            col = i%9
            if not self.get_nodes()[row][col].is_filled():
                shuffle(self.num_list)
                for value in self.num_list:
                    if value not in self.get_row_values(row) and value not in self.get_col_values(col):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = self.get_square(3, 3)
                            elif col < 6:
                                square = self.get_square(6, 3)
                            else:
                                square = self.get_square(9, 3)
                        elif row < 6:
                            if col < 3:
                                square = self.get_square(3, 6)
                            elif col < 6:
                                square = self.get_square(6, 6)
                            else:
                                square = self.get_square(9, 6)
                        else:
                            if col < 3:
                                square = self.get_square(3, 9)
                            elif col < 6:
                                square = self.get_square(6, 9)
                            else:
                                square = self.get_square(9, 9)
                        square_vals = []
                        for rows in square:
                            for node in rows:
                                square_vals.append(node.get_value())
                        if value not in square_vals:
                            self.get_nodes()[row][col].set_value(value)
                            if self.check_grid():
                                return True

                            else:
                                if self.fill():
                                    return True
                                else:
                                    self.get_nodes()[row][col].set_value(0)

                break

def main():
    g = Grid()
    corr = False
    tried = []

    while not corr:
        removed = 0
        attempts = 0
        g.set_nodes(g.generate_nodes())
        g.fill()
        nodes = g.get_nodes()
        print(len(tried))
        vals = []
        g.set_counter(0)
        for r in g.get_nodes():
            rx = []
            for n in r:
                rx.append(n.get_value)
            vals.append(rx)
        if vals in tried:
            continue
        else:
            tried.append(vals)
            while attempts < 5:
                print(f'attempt: {attempts}')
                while removed < 60:
                    row = randint(0,8)
                    col = randint(0,8)

                    backup = g.get_nodes()[row][col].get_value()
                    if backup != 0:
                        g.get_nodes()[row][col].set_value(0)
                        removed += 1
                    

                print("digits removed, solving")
                g.solve()
                if g.get_counter() != 1:
                    attempts += 1
                    g.set_nodes(nodes)
                else:
                    corr = True
                    break

    g.print_grid()


main()


