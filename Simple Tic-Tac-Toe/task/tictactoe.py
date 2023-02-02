# write your code here
def get_matrix_from_line(line):
    return [list(line[3 * i: 3 * (i + 1)]) for i in range(3)]


def get_nb_token_in_a_list(token, row):
    return sum(x == token for x in row)


class Grid:
    def __init__(self):
        line = '_' * 9
        matrix = get_matrix_from_line(line)
        self.matrix = matrix

    def show_matrix(self):
        matrix = self.matrix
        print("---------")
        for i in range(3):
            print('|', end=" ")
            for j in range(3):
                print(matrix[i][j], end=" ")
            print('|')
        print("---------")

    def nb_of_winner_rows(self, token):
        matrix = self.matrix
        return sum(get_nb_token_in_a_list(token, matrix[i]) == 3 for i in range(3))

    def nb_of_winner_columns(self, token):
        matrix = self.matrix
        return sum(get_nb_token_in_a_list(token, [matrix[j][i] for j in range(3)]) == 3 for i in range(3))

    def nb_of_winner_diagonals(self, token):
        matrix = self.matrix
        main_diag = [matrix[i][i] for i in range(3)]
        reverse_diag = [matrix[i][2 - i] for i in range(3)]
        main_diag_result = sum(get_nb_token_in_a_list(token, main_diag) == 3 for _ in range(3))
        reverse_diag_result = sum(get_nb_token_in_a_list(token, reverse_diag) == 3 for _ in range(3))
        return main_diag_result + reverse_diag_result

    def nb_of_winner(self, token):
        return self.nb_of_winner_diagonals(token) + self.nb_of_winner_rows(token) + self.nb_of_winner_columns(token)

    def nb_of_cells(self, token):
        matrix = self.matrix
        return sum(sum(elt == token for elt in row) for row in matrix)

    def nb_of_empty_cells(self):
        return self.nb_of_cells('_')

    def get_state(self):
        matrix = self.matrix
        X_winner = self.nb_of_winner('X')
        O_winner = self.nb_of_winner('O')
        if abs(self.nb_of_cells('X') - self.nb_of_cells('O')) > 1 or (X_winner > 0 and O_winner > 0):
            print('Impossible')
        elif X_winner == 0 and O_winner == 0 and self.nb_of_cells('_') > 0:
            print('Game not finished')
        elif X_winner == 0 and O_winner == 0 and self.nb_of_cells('_') == 0:
            print(matrix)
            print(self.nb_of_winner('_'))
            print('Draw')
        elif X_winner > 0:
            print('X wins')
        elif O_winner:
            print('O wins')

    def make_move(self, token):
        matrix = self.matrix
        while True:
            move_input = input()
            if ' ' not in move_input:
                print("You should enter numbers!")
            elif not all(word.isdigit() for word in move_input.split()):
                print("You should enter numbers!")
            else:
                x, y = map(int, move_input.split())
                if x not in range(1, 4) or y not in range(1, 4):
                    print("Coordinates should be from 1 to 3!")
                elif matrix[x - 1][y - 1] != '_':
                    print("This cell is occupied!")
                else:
                    matrix[x - 1][y - 1] = token
                    break

    def game_is_finished(self):
        return self.nb_of_winner('X') > 0 or self.nb_of_winner('O') > 0 or (
                self.nb_of_winner('X') == 0 and self.nb_of_winner('X') == 0 and self.nb_of_cells('_') == 0)

    def play(self):
        self.show_matrix()
        while not self.game_is_finished():
            self.make_move(user_token)
            self.show_matrix()
        if self.nb_of_winner('X') > 0:
            print('X wins')
        elif self.nb_of_winner('O') > 0:
            print('O wins')
        elif self.nb_of_winner('X') == 0 and self.nb_of_winner('X') == 0 and self.nb_of_cells('_') == 0:
            print('Draw')


grid = Grid()
user_token = 'X'
grid.play()
