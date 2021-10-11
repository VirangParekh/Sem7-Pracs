import copy


class EightPuzzle(object):

    def __init__(self, s):
        s = [int(x) for x in s.split()]
        self.state = []
        for i in range(3):
            row = list()
            for j in range(3):
                row.append(s[3*i + j])
            self.state.append(row)

    def __str__(self):
        s = ''
        for i in range(3):
            for j in range(3):
                s += str(self.state[i][j]) + ' '
        return s

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not __eq__(self, other)

    def __hash__(self):
        uid = 0
        mult = 1
        for i in range(3):
            for j in range(3):
                uid += self.state[i][j] * mult
                mult *= 10
        return uid

    def manhattan_distance(self, goal):
        total = 0
        for i in range(3):
            for j in range(3):
                tile = self.state[i][j]
                for m in range(3):
                    for n in range(3):
                        if tile == goal.state[m][n]:
                            total += abs(i - m) + abs(j - n)
        return total

    def neighbours(self):
        row_zero, col_zero = 0, 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    row_zero = i
                    col_zero = j

        n = []
        if row_zero > 0:
            r = copy.deepcopy(self)
            r.state[row_zero][col_zero] = r.state[row_zero - 1][col_zero]
            r.state[row_zero - 1][col_zero] = 0
            n.append(r)
        if row_zero < 2:
            r = copy.deepcopy(self)
            r.state[row_zero][col_zero] = r.state[row_zero + 1][col_zero]
            r.state[row_zero + 1][col_zero] = 0
            n.append(r)
        if col_zero > 0:
            r = copy.deepcopy(self)
            r.state[row_zero][col_zero] = r.state[row_zero][col_zero - 1]
            r.state[row_zero][col_zero - 1] = 0
            n.append(r)
        if col_zero < 2:
            r = copy.deepcopy(self)
            r.state[row_zero][col_zero] = r.state[row_zero][col_zero + 1]
            r.state[row_zero][col_zero + 1] = 0
            n.append(r)
        return n

    def transition_sequence(self, current, parent):
        s = ''
        if current in parent.keys():
            s = self.transition_sequence(parent[current], parent)
            s += '\n' + str(current)
        else:
            s = str(current)
        return s

    def hill_climbing(self, goal):
        min_node = None
        min_cost = None
        for n in self.neighbours():
            if not min_node or min_cost > n.manhattan_distance(goal):
                min_node = n
                min_cost = n.manhattan_distance(goal)
        if min_cost < self.manhattan_distance(goal):
            return min_node.hill_climbing(goal)
        else:
            return str(self), self.manhattan_distance(goal)


initial = input("Enter the initial state: ")
goal = input("Enter the goal state: ")
initial = EightPuzzle(initial)
goal = EightPuzzle(goal)
print(initial.hill_climbing(goal))
