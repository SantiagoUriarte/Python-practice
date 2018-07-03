class OthelloGameState:
    def __init__(self, starting_player: str, win_condition: str, columns, rows):
        '''
        Constant Variables
        '''

        self.WHITE = "White"
        self.BLACK = "Black"
        self.NONE = "."
        self.WIN_CONDITION = win_condition
        self.COLUMNS = columns
        self.ROWS = rows

        '''
        Changing Variables
        '''
        self.current_player = starting_player
        self.game_over = False



    '''
    Public methods
    '''

    def new_game(self):
        # Creates new game
        self.game_board = self._create_board()
        self.set_score()
    
    def set_score(self):
        '''
        Reads board columns and sets the score for both players
        '''
        self.white_score = 0
        self.black_score = 0

        for column in self.game_board:
            for piece in column:
                if piece == self.WHITE:
                    self.white_score += 1
                if piece == self.BLACK:
                    self.black_score += 1


    def find_available_moves(self) -> tuple:
        '''
        Finds available moves and stores them in a dictionary with format placed_piece: [pieces to flip]
        '''
        available_moves = []
        pieces_to_flip = []


        for column_index in range(len(self.game_board)):
            for piece_index in range(len(self.game_board[0])):
                if self.game_board[column_index][piece_index] == self.NONE:
                    horizontal_moves = (self._check_horizontal(column_index, piece_index))
                    vertical_moves = (self._check_vertical(column_index, piece_index))
                    diagonal_positive_moves = (self._check_diagonal_positive(column_index, piece_index))
                    diagonal_negative_moves = (self._check_diagonal_negative(column_index, piece_index))

                    #If pieces flipped, move is valid
                    if len(horizontal_moves) > 0 or len(vertical_moves) > 0 or len(diagonal_positive_moves) > 0 or len(diagonal_negative_moves) > 0:
                        available_moves.append([piece_index, column_index])
                        pieces_to_add = []
                        for moves in horizontal_moves:
                            pieces_to_add.append(moves)

                        for moves in vertical_moves:
                            pieces_to_add.append(moves)

                        for moves in diagonal_positive_moves:
                            pieces_to_add.append(moves)

                        for moves in diagonal_negative_moves:
                            pieces_to_add.append(moves)

                        pieces_to_flip.append(pieces_to_add)

        return (available_moves, pieces_to_flip)


    def place_piece(self, column, row, color):
        self.game_board[row][column] = color

    def flip_pieces(self, pieces_to_flip: list, color: str):
        for piece_location in pieces_to_flip:
            self.place_piece(piece_location[0], piece_location[1], color )

    def change_player(self):
        self.current_player = self._get_opposite_player()

    def get_winner(self)->str:
        self.set_score()

        if self.WIN_CONDITION == ">":
            if self.white_score == self.black_score:
                return "NONE"
            elif self.black_score > self.white_score:
                return "Black"
            else:
                return "White"

        if self.WIN_CONDITION == "<":
            if self.white_score == self.black_score:
                return "NONE"
            elif self.black_score < self.white_score:
                return "Black"
            else:
                return "White"

    '''
    Private methods
    '''

    def _create_board(self):
        '''
        Creates new board from initial input
        '''
        board = []

        for row in range(self.ROWS):

            row_list = []

            for column in range(int(self.COLUMNS)):
                row_list.append(".")

            board.append(row_list)

        return board
        


    def _get_opposite_player(self) -> str:
        '''
        Finds opposite player
        '''
        if self.current_player == self.BLACK:
            return self.WHITE

        if self.current_player == self.WHITE:
            return self.BLACK

    def _check_horizontal(self, column: int, row: int) -> list:
        '''
        Checks horizontally from placed piece for pieces to flip
        '''
        pieces_to_flip = []
        pieces_to_add = []

        #Checks right side of piece
        for piece_index in range(row + 1, len(self.game_board[0])):
            if self.game_board[column][piece_index] == self.NONE:
                break

            if self.game_board[column][piece_index] == self.current_player:
                for piece in pieces_to_add:
                    pieces_to_flip.append(piece[::-1])

                break

            if self.game_board[column][piece_index] == self._get_opposite_player():
                pieces_to_add.append([column, piece_index])

        #Checks left side of piece
        pieces_to_add = []
        for piece_index in range(row - 1, -1, -1):
            if self.game_board[column][piece_index] == self.NONE:
                break

            if self.game_board[column][piece_index] == self.current_player:
                for piece in pieces_to_add:
                    pieces_to_flip.append(piece[::-1])

                break

            if self.game_board[column][piece_index] == self._get_opposite_player():
                pieces_to_add.append([column, piece_index])

        return pieces_to_flip[::-1]

    def _check_vertical(self, column: int, row: int) -> list:
        '''
        checks vertically from placed piece to flip
        '''
        pieces_to_flip = []
        pieces_to_add = []

        #checks above
        for column_index in range(column - 1, -1 ,-1):
            if self.game_board[column_index][row] == self.NONE:
                break

            if self.game_board[column_index][row] == self.current_player:
                for piece in pieces_to_add:
                    pieces_to_flip.append(piece[::-1])

                break

            if self.game_board[column_index][row] == self._get_opposite_player():
                pieces_to_add.append([column_index, row])

        #checks below
        pieces_to_add = []
        for column_index in range(column + 1, len(self.game_board)):
            if self.game_board[column_index][row] == self.NONE:
                break

            if self.game_board[column_index][row] == self.current_player:
                for piece in pieces_to_add:
                    pieces_to_flip.append(piece[::-1])

                break

            if self.game_board[column_index][row] == self._get_opposite_player():
                pieces_to_add.append([column_index, row])


        return pieces_to_flip[::-1]

    def _check_diagonal_positive(self, column: int, row: int) -> list:
        '''
        checks diagonal with positive slope
        '''

        pieces_to_flip = []
        pieces_to_add = []


        #checks above and to the right
        count = 1
        for column_index in range(column - 1, -1, -1):
            piece_index = row + count

            try:
                if self.game_board[column_index][piece_index] == self.NONE:

                    raise IndexError

                if self.game_board[column_index][piece_index] == self.current_player:

                    for piece in pieces_to_add:
                        pieces_to_flip.append(piece[::-1])

                    raise IndexError

                if self.game_board[column_index][piece_index] == self._get_opposite_player():

                    pieces_to_add.append([column_index, piece_index])

                count += 1

            except IndexError:
                pieces_to_add = []
                break

        #checks below and to the left
        count = 1
        for column_index in range(column + 1, len(self.game_board)):
            try:
                piece_index = row - count

                if piece_index < 0:
                    raise IndexError

                if self.game_board[column_index][piece_index] == self.NONE:

                    raise IndexError

                if self.game_board[column_index][piece_index] == self.current_player:

                    for piece in pieces_to_add:
                        pieces_to_flip.append(piece[::-1])

                    raise IndexError

                if self.game_board[column_index][piece_index] == self._get_opposite_player():

                    pieces_to_add.append([column_index, piece_index])

                count += 1

            except IndexError:
                pieces_to_add = []
                break

        return pieces_to_flip

    def _check_diagonal_negative(self, column: int, row: int):
        '''
        checks diagonal with negative slope
        '''

        pieces_to_flip = []
        pieces_to_add = []

        # checks above and to the left
        count = 1
        for column_index in range(column - 1, -1, -1):
            try:
                piece_index = row - count

                if piece_index < 0:
                    raise IndexError

                if self.game_board[column_index][piece_index] == self.NONE:
                    raise IndexError

                if self.game_board[column_index][piece_index] == self.current_player:

                    for piece in pieces_to_add:
                        pieces_to_flip.append(piece[::-1])

                    raise IndexError

                if self.game_board[column_index][piece_index] == self._get_opposite_player():
                    pieces_to_add.append([column_index, piece_index])

                count += 1

            except IndexError:
                pieces_to_add = []
                break

        # checks below and to the left
        count = 1
        for column_index in range(column + 1, len(self.game_board)):
            piece_index = row + count

            try:
                if self.game_board[column_index][piece_index] == self.NONE:
                    raise IndexError

                if self.game_board[column_index][piece_index] == self.current_player:

                    for piece in pieces_to_add:
                        pieces_to_flip.append(piece[::-1])

                    raise IndexError

                if self.game_board[column_index][piece_index] == self._get_opposite_player():
                    pieces_to_add.append([column_index, piece_index])

                count += 1

            except IndexError:
                break

        return pieces_to_flip
