from __future__ import annotations
import time

class Board:


    '''
    :next: is a set of boards one play ahead from this one.
    :turn: indicates wich player is next, by default it is initialized as 'x'.
    :squares: is a tuple that represents the state of the board and can have 3 values: 'e' if the square is empty, 'x' if it's occupied by 'x' player, and 'o' if it's occupied by 'o' player.
    :winner: determinates if the board either has a winner or has a guaranteed win line(in this case for 'x' player)
    '''

    def __init__(self, _squares : tuple, _turn : str = 'x', _winner : str = 'n') -> None:
    
        self.next = set()
        self.turn = _turn
        self.squares = _squares
        self.winner = _winner
    
    def __eq__(self, __o) -> bool:
        
        if type(__o) is Board:
            if self.squares == __o.squares:
                return True
            else:
                print("The boards are not the same.")
                return False
        else:
            print(f"The object {__o} is of type {type(__o)} and can't be compared to the type Board.")
            return False
    
    def __hash__(self) -> int:
        return hash(self.squares)
    
    def __repr__(self) -> str:
        return f"{self.squares[0]}|{self.squares[1]}|{self.squares[2]}\n{self.squares[3]}|{self.squares[4]}|{self.squares[5]}\n{self.squares[6]}|{self.squares[7]}|{self.squares[8]}"        

    def __sub__(self,other_board : Board) -> int:

        '''
        !!!IMPORTANT!!!
        Should only be used when comparing a board with another insid its next set of boards.
        Returns the index of the first different square between both boards.
        '''
        
        for square_index in range(9):
            if other_board.squares[square_index] != self.squares[square_index]:
                return square_index
    
    def return_next_board(self, square_index : int, move : str) -> Board:
        
        '''
        Returns the next board after a valid move.
        '''
        board : Board
        for board in self.next:
            if board.squares[square_index] == move:
                return board
    
    def check_winner(self):
        
        '''check rows'''
        for i in range(0,7,3):
            if self.squares[i] == self.squares[i+1] and self.squares[i+2] == self.squares[i] and self.squares[i] != 'e':
                self.winner = self.squares[i]
        
        if self.winner == 'n':
            '''check columns'''
            for i in range(3):
                if self.squares[i] == self.squares[i+3] and self.squares[i+6] == self.squares[i] and self.squares[i] != 'e':
                    self.winner = self.squares[i]
            
            if self.winner == 'n':
                '''check diagonals'''                
                if self.squares[0] == self.squares[4] and self.squares[8] == self.squares[0] and self.squares[0] != 'e':
                    self.winner = self.squares[0]
                
                if self.winner == 'n':
                    if self.squares[2] == self.squares[4] and self.squares[6] == self.squares[2] and self.squares[2] != 'e':
                        self.winner = self.squares[2]
    
class Tree:

    
    def __init__(self) -> None:
        
        squares = ('e','e','e',
                   'e','e','e',
                   'e','e','e')
    
        self.root = Board(squares)
        self.all_boards = set()
        self.cont = 0
        self.generate_tree()
        
    
    def generate_tree(self, current_board : Board = None) -> None:
        
        if current_board is None:
            current_board = self.root
        
        for square_index in range(9):
            
            if current_board.squares[square_index] == 'e':
                
                '''
                Creates a new tuple from list with one element different to pass as the squares of the next board
                '''
                turn = current_board.turn
                
                if turn == 'x':
                    _squares = tuple([current_board.squares[x] if x != square_index else 'x' for x in range(9)])
                    turn = 'o'
                else:        
                    _squares = tuple([current_board.squares[x] if x != square_index else 'o' for x in range(9)])
                    turn = 'x'
                    
                '''
                Creates the actual board and update it's winner value, then add to the tree set of boards 
                '''
                board = Board(_squares,turn)
                current_board.next.add(board)
                
                if board not in self.all_boards:    
                    board.check_winner()
                    self.all_boards.add(board)
                    
                    '''
                    If board already has a winner doesnt need to generate next boards
                    '''
                    if board.winner != 'n':
                        current_board.winner = board.winner
                    else:
                        self.generate_tree(board)

    def best_move(self,current_board : Board = None) -> int:
        
        '''
        Searches the tree board set looking for the better line to follow, in case there is no win line, it will go for the draw.
        '''    
        if current_board is None:
            current_board = self.root
        
        draw_line = 0
        
        board : Board
        for board in current_board.next:
            '''
            If none of the boards in the next set is already a winner line it chooses any of them.
            '''
            if board.winner == 'x':
                return current_board.__sub__(board)
            elif board.winner == 'n':
                draw_line = current_board.__sub__(board)
        return draw_line
        
    def print_tree(self, current_board : Board = None):
        
        if current_board is None: 
            current_board = self.root
        
        print("\n"+repr(current_board)+"\t"+current_board.turn+"\t"+current_board.winner)
        
        for board in current_board.next:
            self.print_tree(board)
            
            
class Game:
    
    def __init__(self, tree : Tree) -> None:
        self.tree = tree
        self.current_board = tree.root
        self.is_over = False
    
    def versus_pro_cpu(self):
        
        print(repr(self.current_board))
        while not self.is_over:
            
            self.current_board.check_winner
            print(self.current_board.winner)
            
            if self.current_board.turn == 'o':
                valid_move = False
                while not valid_move:
                    move = int(input("Enter 0-8 left-right top-botton empty position: "))
                    if self.current_board.squares[move] == 'e':
                        valid_move = True
                self.make_move(move)
            else:
                move = self.tree.best_move(self.current_board)
                self.make_move(move)         
                    
            if self.current_board.winner != 'n':
                self.is_over = True
            
            print("\n"+repr(self.current_board))
        
        print("The winner is: "+self.current_board.winner)
        
    
    def make_move(self, move_index : int):
        
        '''
        Takes and int from 0-8 then verifies if it's a valid move(square is empty), if so executes it.
        '''
        if self.current_board.squares[move_index] == 'e':
            self.current_board = self.current_board.return_next_board(move_index, self.current_board.turn)


if __name__ == "__main__":
    
    tree = Tree()
    game = Game(tree)
    game.versus_pro_cpu()
