import tkinter
import othello



class StartQuitScreen:
    #Intro window to start or quit
    def __init__(self):
        self.start_quit_window = tkinter.Tk()
        self.start_quit_window.title("Welcome")
        self.icon_photo = tkinter.PhotoImage(file="othello.png")


        #Create Widgets
        self.welcome_message = tkinter.Label(self.start_quit_window,
                                             text="Welcome to Othello",
                                             font=("Calibri", 20))
        self.author_message = tkinter.Label(self.start_quit_window,
                                             text="created by Santiago Uriarte",
                                            font=("Calibri", 10))
        self.start_button = tkinter.Button(self.start_quit_window,
                                           text="START GAME",
                                           font=("Calibri", 11))
        self.quit_button = tkinter.Button(self.start_quit_window,
                                           text="QUIT GAME",
                                           font=("Calibri", 11))
        self.icon_label = tkinter.Label(self.start_quit_window,
                                        image = self.icon_photo)


        #Bind Widgets
        self.start_button.bind("<Button-1>", self._start_game)
        self.quit_button.bind("<Button-1>", self._quit_game)


        #Place Widgets
        self.welcome_message.grid(row=0,
                                  column=0,
                                  columnspan=2,
                                  padx=20
                                  )

        self.author_message.grid(row=1,
                                 column=0,
                                 columnspan=2,
                                 pady=(0,10)
                                 )

        self.icon_label.grid(row=2,
                        column=0,
                        columnspan=2,
                        padx=0,
                        pady=20
                             )

        self.start_button.grid(row=3,
                               column=0,
                               padx=10,
                               pady=10,
                               sticky=tkinter.W
                               )

        self.quit_button.grid(row=3,
                              column=1,
                              padx=10,
                              pady=10,
                              sticky=tkinter.W
                              )

        #Set Configure Weights
        self.start_quit_window.rowconfigure(2, weight=1)
        self.start_quit_window.columnconfigure(0, weight=1)

    #Public Methods
    def run(self):
        #Starts the Program
        self.start_quit_window.mainloop()

    #Private Methods
    def _start_game(self, event):
        #Quits Start Screen and launches screen to input initial game settings
        self.start_quit_window.destroy()
        game_settings = GameSettings()
        game_settings.run()


    def _quit_game(self, event):
        #Quits Program
        self.start_quit_window.destroy()


class GameSettings:
    #Window to choose initial game settings
    def __init__(self):
        self.settings_window = tkinter.Tk()
        self.settings_window.title("Settings")
        self.setting_icon = tkinter.PhotoImage(file="setting.png")

        #Create and Place Widgets
        #-----------------------
        #Settings Label
        settings_message = tkinter.Label(master=self.settings_window, text="Othello Game Settings", font=("Calibri", 20))
        settings_message.grid(
            row=0,
            columnspan=5,
            pady=10
        )

        #Photo Icon
        self.icon_label = tkinter.Label(master=self.settings_window, image=self.setting_icon)
        self.icon_label.grid(
            row=1,
            column=0,
            columnspan=5,
            pady=20
        )

        # Row Widget
        row_label = tkinter.Label(master=self.settings_window, text="Rows: ", font=("Calibri", 13))
        row_label.grid(row=2,
                       column=0,
                       sticky=tkinter.W,
                       padx=(20, 0),
                       pady=10
                       )

        self.row_entry = tkinter.Spinbox(master=self.settings_window, from_=4, to=16, font=("Calibri", 13))
        self.row_entry.grid(row=2,
                            column=1,
                            columnspan=2,
                            padx=10,
                            pady=10
                            )

        #Column Widget
        column_label = tkinter.Label(master=self.settings_window, text="Columns: ", font=("Calibri", 13))
        column_label.grid(row=3,
                       column=0,
                       sticky=tkinter.W,
                       padx=(20,0),
                       pady = 10
                       )

        self.column_entry = tkinter.Spinbox(master=self.settings_window, from_=4, to=16, font=("Calibri", 13))
        self.column_entry.grid(row=3,
                            column=1,
                            columnspan=2,
                            padx = 20,
                            pady=10
                           )



        #Starting Player
        starting_player_label = tkinter.Label(master=self.settings_window, text="Starting Color:", font=("Calibri", 13))
        starting_player_label.grid(row=4,
                                   column=0,
                                   columnspan=1,
                                   padx=20,
                                   sticky=tkinter.W
                                   )

        self.starting_player = tkinter.StringVar()

        #White
        white_choice = tkinter.Radiobutton(master=self.settings_window,
                                          text="White",
                                          variable=self.starting_player,
                                          font=("Calibri", 13),
                                          indicatoron=0,
                                          value="White"
                                          )
        white_choice.grid(row=4,
                          column=1,
                          columnspan=1,
                          padx=10,
                          sticky=tkinter.W+tkinter.E
                          )
        white_choice.select()

        #Black
        black_choice = tkinter.Radiobutton(master=self.settings_window,
                                          text="Black",
                                          variable=self.starting_player,
                                          font=("Calibri", 13),
                                          indicatoron=0,
                                          value="Black"
                                          )
        black_choice.grid(row=4,
                          column=2,
                          columnspan=1,
                          padx=10,
                          sticky=tkinter.W + tkinter.E
                          )

        #Win Condition
        win_condition_label = tkinter.Label(master=self.settings_window, text="Win Condition:", font=("Calibri", 13))
        win_condition_label.grid(row=5,
                                   column=0,
                                   columnspan=1,
                                   padx=20,
                                   sticky=tkinter.W
                                   )

        self.win_condition = tkinter.StringVar()

        #More than
        most_pieces_choice = tkinter.Radiobutton(master=self.settings_window,
                                           text="Most Pieces",
                                           variable=self.win_condition,
                                           font=("Calibri", 13),
                                           indicatoron=0,
                                           value=">"
                                           )
        most_pieces_choice.grid(row=5,
                          column=1,
                          columnspan=1,
                          padx=10,
                          pady=10,
                          sticky=tkinter.W + tkinter.E
                          )
        most_pieces_choice.select()

        #Less than
        least_pieces_choice = tkinter.Radiobutton(master=self.settings_window,
                                           text="Least Pieces",
                                           variable=self.win_condition,
                                           font=("Calibri", 13),
                                           indicatoron=0,
                                           value="<"
                                           )
        least_pieces_choice.grid(row=5,
                          column=2,
                          columnspan=1,
                          padx=10,
                          pady=10,
                          sticky=tkinter.W + tkinter.E
                          )

        #Finished Button
        finished_button = tkinter.Button(master=self.settings_window, text="Finished", font=("Calibri", 13))
        finished_button.grid(row=6,
                             column=0,
                             columnspan=4,
                             padx=10,
                             pady=(10,20),
                             sticky=tkinter.W + tkinter.E
                             )

        finished_button.bind("<Button-1>", self._finish_settings)

        #Window reconfigure
        self.settings_window.rowconfigure(1, weight=1)
        self.settings_window.columnconfigure(0, weight=1)

    #Public functions
    def run(self):
        self.settings_window.mainloop()

    #Private functions
    def _finish_settings(self, event):
        settings = {}

        settings["rows"] = int(self.row_entry.get())
        settings["columns"] = int(self.column_entry.get())

        settings["starting_player"] = self.starting_player.get()

        settings["win_condition"] = self.win_condition.get()

        self.settings_window.destroy()

        board_settings = InitialBoardSettings(settings)
        board_settings.run()


class InitialBoardSettings:
    #Creates window to set up initial board
    def __init__(self, settings: dict):
        #Create Attributes
        self.settings = settings
        self.rows = settings["rows"]
        self.columns =  settings["columns"]
        self.placed_pieces = {}

        self.board_settings = tkinter.Tk()
        self.board_settings.title("Board Settings")

        #Create Widgets
        #---------------
        #Setup Label
        set_up_label = tkinter.Label(self.board_settings, text="Initial Board Settings", font=("Calibri", 20))
        set_up_label.grid(row=0,
                          column=0,
                          columnspan=5,
                          pady=(20,0),
                          sticky=tkinter.E+tkinter.W)

        #Instructions
        instruction_label = tkinter.Label(self.board_settings, text="Place initial pieces", font=("Calibri", 10))
        instruction_label.grid(row=1,
                          column=0,
                          columnspan=4,
                          pady=(0,20),
                          sticky=tkinter.E + tkinter.W)


        # Create game board
        self.board = tkinter.Canvas(self.board_settings, bg="Green", height=500, width=500)
        self.board.grid(row=2,
                        column=0,
                        columnspan=5,
                        padx=10,
                        sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self.board.update()
        self._draw_grid()

        #Color Label
        color_label = tkinter.Label(self.board_settings, text="Choose Color to Place: ", font=("Calibri", 13))
        color_label.grid(row=3,
                         column=0,
                         sticky=tkinter.W,
                         padx=10,
                         pady=20)

        #Color Choice
        self.current_color = tkinter.StringVar()
        self.current_color.set(settings["starting_player"])

        #White
        self.white_choice = tkinter.Radiobutton(self.board_settings, text="White", font=("Calibri", 13), indicatoron=0,
                                                variable=self.current_color,
                                                value="White"
                                                )
        self.white_choice.grid(row=3,
                               column=1,
                               columnspan=1,
                               sticky=tkinter.W,
                               pady=10,
                               padx=(10,0),
                               )

        #Black
        self.black_choice = tkinter.Radiobutton(self.board_settings, text="Black", font=("Calibri", 13), indicatoron=0,
                                                variable=self.current_color,
                                                value="Black")
        self.black_choice.grid(row=3,
                               column=3,
                               sticky=tkinter.W,
                               pady=10,
                               padx=10,
                               )

        # Reset
        self.reset_button = tkinter.Button(self.board_settings, text="Reset", font=("Calibri", 20))
        self.reset_button.grid(row=4,
                               column=0,
                               columnspan=5,
                               padx=10,
                               pady=10,
                               sticky=tkinter.W)

        #Done
        self.done_button = tkinter.Button(self.board_settings, text="Done", font=("Calibri", 20))
        self.done_button.grid(row=4,
                              column=3,
                              columnspan=1,
                              padx=10,
                              pady=10,
                              sticky=tkinter.W)






        #Bind Commands
        self.board.bind("<Configure>", self._window_resized)
        self.board.bind("<Button-1>", self._board_click)
        self.done_button.bind("<Button-1>", self._done_click)
        self.reset_button.bind("<Button-1>", self._reset_click)



        #Window reconfigure
        self.board_settings.rowconfigure(2, weight=1)
        self.board_settings.columnconfigure(0, weight=1)


    #Public functions
    def run(self):
        self.board_settings.mainloop()

    #Private functions
    def _draw_grid(self):
        #Create rows
        for row in range(1, int(self.rows) + 1):
            self.board.create_line((self.board.winfo_width() / self.rows) * row,
                                    0,
                                   (self.board.winfo_width() / self.rows) * row,
                                    self.board.winfo_height(),
                                   fill="Black")

        #Create columns
        for column in range(1, int(self.columns) + 1):
            self.board.create_line(0,
                                   (self.board.winfo_height() / self.columns) * column,
                                    self.board.winfo_width(),
                                   (self.board.winfo_height() / self.columns) * column,
                                   fill="Black")

    def _window_resized(self, event):
        #Handle when window gets resized
        self._get_row(event)
        self._get_column(event)

        self._redraw_board()

    def _redraw_board(self):
        #Redraws grid and board
        self.board.delete(tkinter.ALL)

        self._draw_grid()
        self._redraw_pieces()


    def _board_click(self, event):
        #Handles when board is clicked


        column = self._get_column(event)
        row = self._get_row(event)

        color = self.current_color.get()

        #If piece exists and is current color then delete it, otherwise placed piece and ut it into placed pieces
        if (column, row) in self.placed_pieces and self.placed_pieces[(column, row)] == color:
            del self.placed_pieces[(column, row)]

        else:
            self._place_piece(column, row, color)
            self.placed_pieces[(column, row)] = color

        self._redraw_board()


    def _done_click(self, event):
        #Handles when done button is clicked

        self.board_settings.destroy()

        othello_gui = OthelloGUI(self.settings, self.placed_pieces)
        othello_gui.run()

    def _get_row(self, event):
        #Gets row mouse clicked

        self.cell_y = self.board.winfo_height() / self.columns

        return int(event.y / self.cell_y) + 1

    def _get_column(self, event):
        #Gets column mouse clicked

        self.cell_x = self.board.winfo_width() / self.rows

        return int(event.x / self.cell_x) + 1

    def _place_piece(self, column: int, row: int, color: str):
        #Places piece at specified column and row

        self.board.create_oval((column - 1) * self.cell_x,
                               (row - 1) * self.cell_y,
                               column * self.cell_x,
                               row * self.cell_y,
                               fill = color
                               )
    def _redraw_pieces(self):
        #Redraws all pieces from placed pieces dictioanry

        for piece_location in self.placed_pieces:
            self._place_piece(piece_location[0], piece_location[1], self.placed_pieces[piece_location])

    def _reset_click(self, event):
        self.board.delete(tkinter.ALL)

        self.placed_pieces = {}

        self._draw_grid()

class OthelloGUI:
    #GUI window for playing Othello
    def __init__(self, settings: dict, initial_board: dict):
        #Create Attributes
        self.settings = settings
        self.placed_pieces = initial_board

        self.rows = settings["rows"]
        self.columns = settings["columns"]

        #Create logic instance
        self.othello_game_state = othello.OthelloGameState(settings["starting_player"], settings["win_condition"], self.columns, self.rows)
        self.othello_game_state.new_game()
        self._place_piece_in_logic()

        self.othello_gui = tkinter.Tk()
        self.othello_gui.title("Othello")


        # Create Widgets
        #------------------
        # Title
        title_label = tkinter.Label(self.othello_gui, text="Othello", font=("Calibri", 40))
        title_label.grid(row=0,
                          column=0,
                          columnspan=5,
                          pady=(20, 0),
                          sticky=tkinter.E + tkinter.W)

        # Description
        full_label = tkinter.Label(self.othello_gui, text="FULL", font=("Calibri", 13))
        full_label.grid(row=1,
                               column=0,
                               columnspan=5,
                               pady=(0, 20),
                               padx=10,
                               sticky=tkinter.E + tkinter.W)

        # Create game board
        self.board = tkinter.Canvas(self.othello_gui, bg="Green", height=500, width=500)
        self.board.grid(row=2,
                        column=0,
                        columnspan=5,
                        padx=10,
                        pady=(0, 30),
                        sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self.board.update()

        self.cell_x = self.board.winfo_width() / self.rows
        self.cell_y = self.board.winfo_height() / self.columns

        #Initial state
        self._draw_grid()
        self._redraw_pieces()

        #Score
        self.w_score = tkinter.IntVar()
        self.b_score = tkinter.IntVar()


        self.score_label = tkinter.Label(self.othello_gui, text="White Score: {}, Black Score: {}".format(self.w_score.get(), self.b_score.get()), font=("Calibri", 15))
        self.score_label.grid(row=3,
                         column=0,
                         columnspan=4,
                         padx=10,
                         pady=(0,20),
                         sticky=tkinter.W)

        #Turn
        self.turn_label = tkinter.Label(self.othello_gui, text="Turn: {}".format(self.othello_game_state.current_player), font=("Calibri", 15))
        self.turn_label.grid(row=3,
                        column=3,
                        padx=10,
                        pady=(0,20),
                        sticky=tkinter.E)

        # Bind methods
        self.board.bind("<Configure>", self._window_resized)
        self.board.bind("<Button-1>", self._board_click)

        # Configure Window
        self.othello_gui.rowconfigure(2, weight=1)
        self.othello_gui.columnconfigure(0, weight=1)

        # Initial Update
        self._check_for_game_over()

    #Public Methods
    def run(self):
        #Runs the Othello GUI
        self.othello_gui.mainloop()

    #Private Methods
    def _check_for_game_over(self):
        self._check_for_moves()
        if self.othello_game_state.game_over == True:
            self.othello_gui.destroy()

            win_screen = WinScreen(self.othello_game_state)
            win_screen.run()
        else:
            self._update_GUI()

    def _draw_grid(self):
        #Create rows
        for row in range(1, int(self.rows) + 1):
            self.board.create_line(self.cell_x * row,
                                   0,
                                   self.cell_x * row,
                                   self.board.winfo_height(),
                                   fill="Black")

        #Create columns
        for column in range(1, int(self.columns) + 1):
            self.board.create_line(0,
                                   self.cell_y * column,
                                   self.board.winfo_width(),
                                   self.cell_y * column,
                                   fill="Black")

    def _window_resized(self, event):
       self.board.delete(tkinter. ALL)

       self._get_column(event)
       self._get_row(event)

       self._draw_grid()

       for piece_location in self.placed_pieces:
           self._place_piece(piece_location[0], piece_location[1], self.placed_pieces[piece_location])



    def _check_for_moves(self):
        #Check if both players have any moves left
        current_player_moves, forget = self.othello_game_state.find_available_moves()

        if len(current_player_moves) == 0:
            self.othello_game_state.change_player()
            opposite_player_moves, forget = self.othello_game_state.find_available_moves()

            if len(opposite_player_moves) == 0:
                self.othello_game_state.game_over = True

        self._update_GUI()

    def _board_click(self, event):
        #Handles Board click
        #---------------------

        column = self._get_column(event)
        row = self._get_row(event)
        color = self.othello_game_state.current_player
        move = [column - 1, row - 1]

        available_moves, pieces_to_flip = self.othello_game_state.find_available_moves()

        if move in available_moves:
            move_index = available_moves.index(move)

            self._place_piece(column, row, color)
            self.othello_game_state.place_piece(move[0], move[1], color)

            self._flip_pieces(pieces_to_flip[move_index], color)
            self.othello_game_state.flip_pieces(pieces_to_flip[move_index], color)

            self.othello_game_state.change_player()

            self._check_for_game_over()

    def _place_piece_in_logic(self):
        for move in self.placed_pieces:
            self.othello_game_state.place_piece(int(move[0]) - 1, int(move[1]) - 1, self.placed_pieces[move])

    def _get_row(self, event):
        # Gets row mouse clicked

        self.cell_y = self.board.winfo_height() / self.columns

        return int(event.y / self.cell_y) + 1

    def _get_column(self, event):
        #Gets column mouse clicked

        self.cell_x = self.board.winfo_width() / self.rows

        return int(event.x / self.cell_x) + 1

    def _place_piece(self, column: int, row: int, color: str):
        #Places piece at specified column and row

        self.board.create_oval((column - 1) * self.cell_x,
                               (row - 1) * self.cell_y,
                               column * self.cell_x,
                               row * self.cell_y,
                               fill = color
                               )

        self.placed_pieces[(column, row)] = color

    def _flip_pieces(self,pieces_to_flip: list, color: str):

        for piece in pieces_to_flip:

            self._place_piece(piece[0] + 1, piece[1] + 1, color)

    def _redraw_pieces(self):
        #Redraws all pieces from placed pieces dictionary

        for piece_location in self.placed_pieces:
            self._place_piece(piece_location[0], piece_location[1], self.placed_pieces[piece_location])

    def _update_GUI(self):
        #Updates label and board
        self.othello_game_state.set_score()

        self.w_score.set(self.othello_game_state.white_score)
        self.b_score.set(self.othello_game_state.black_score)

        self.score_label.config(text="White Score: {}, Black Score: {}".format(self.w_score.get(), self.b_score.get()))
        self.turn_label.config(text="Turn: {}".format(self.othello_game_state.current_player))

        self.othello_gui.update()

class WinScreen:
    #Intro window to start or quit
    def __init__(self, othello_game_state):
        self.othello_game_state = othello_game_state
        self.othello_game_state.set_score()

        self.win_screen = tkinter.Tk()
        self.win_screen.title("Winner")
        self.icon_photo = tkinter.PhotoImage(file="winner.png")


        #Create Widgets
        self.winner_message = tkinter.Label(self.win_screen,
                                             text="WINNER!",
                                             font=("Calibri", 25))
        self.description_message = tkinter.Label(self.win_screen,
                                             text="Game Over",
                                            font=("Calibri", 10))
        self.score_message = tkinter.Label(self.win_screen,
                                           text="Winner: {}\n\nWhite Score: {}\nBlack Score: {}".format(self.othello_game_state.get_winner(), self.othello_game_state.white_score, self.othello_game_state.black_score),
                                           font=("Calibri", 13))
        self.start_button = tkinter.Button(self.win_screen,
                                           text="Play Again",
                                           font=("Calibri", 13))
        self.quit_button = tkinter.Button(self.win_screen,
                                           text="Quit",
                                           font=("Calibri", 13))
        self.icon_label = tkinter.Label(self.win_screen,
                                        image = self.icon_photo)


        #Bind Widgets
        self.start_button.bind("<Button-1>", self._start_game)
        self.quit_button.bind("<Button-1>", self._quit_game)


        #Place Widgets
        self.winner_message.grid(row=0,
                                  column=0,
                                  columnspan=2,
                                  padx=20
                                  )

        self.description_message.grid(row=1,
                                 column=0,
                                 columnspan=2,
                                 pady=(0,10)
                                 )

        self.icon_label.grid(row=2,
                        column=0,
                        columnspan=2,
                        padx=0,
                        pady=20
                             )
        self.score_message.grid(row=3,
                                column=0,
                                columnspan=2,
                                padx=10,
                                pady=(10, 20),
                                sticky=tkinter.E+tkinter.W)

        self.start_button.grid(row=4,
                               column=0,
                               padx=10,
                               pady=10,
                               sticky=tkinter.W
                               )

        self.quit_button.grid(row=4,
                              column=1,
                              padx=10,
                              pady=10,
                              sticky=tkinter.W
                              )

        #Set Configure Weights
        self.win_screen.rowconfigure(2, weight=1)
        self.win_screen.columnconfigure(0, weight=1)

    #Public Methods
    def run(self):
        #Starts the Program
        self.win_screen.mainloop()

    #Private Methods
    def _start_game(self, event):
        #Quits Start Screen and launches screen to input initial game settings
        self.win_screen.destroy()
        game_settings = GameSettings()
        game_settings.run()


    def _quit_game(self, event):
        #Quits Program
        self.win_screen.destroy()

def main():
    start_screen = StartQuitScreen()
    start_screen.run()

if __name__ == "__main__":
    main()