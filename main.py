class Node:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.filled = 0 
        

    def get_pos(self):
        return [self.row, self.col]


    def is_filled(self):
        return self.filled != 0


    def fill(self, number):
        self.filled = number


    def get_number(self):
        return self.filled


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


    def get_nodes(self):
        return self.nodes


    def generate_nodes(self):
        nodes = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(Node(i, j))
            nodes.append(row)
        return nodes


    def print_grid(self):   # for debug purposes only
        for row in self.get_nodes():
            for node in row:
                print(node.get_number(), end="\t")
            print("\n")
            print("\n")



g = Grid()
g.print_grid()
