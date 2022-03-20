from __future__ import annotations


class Board:


    '''
    :next: is a set of boards one play ahead from this one.
    :turn: indicates wich player is next, by default it is initialized as 'x'.
    :squares: is a tuple that represents the state of the board and can have 3 values: 'e' if the square is empty, 'x' if it's occupied by 'x' player, and 'o' if it's occupied by 'o' player.
    :winner: determinates if the board has a winner after 
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
        
    def __repr__(self) -> str:
        return f"{self.squares[0]}|{self.squares[1]}|{self.squares[2]}\n{self.squares[3]}|{self.squares[4]}|{self.squares[5]}\n{self.squares[6]}|{self.squares[7]}|{self.squares[8]}"        

    def check_winner(self):
        
        print("Enter check")
        '''check rows'''
        for i in range(0,7,3):
            if self.squares[i] == self.squares[i+1] and self.squares[i+2] == self.squares[i] and self.squares[i] != 'n':
                self.winner = self.squares[i]
        
        if self.winner == 'n':
            '''check columns'''
            for i in range(3):
                if self.squares[i] == self.squares[i+3] and self.squares[i+6] == self.squares[i] and self.squares[i] != 'n':
                    self.winner = self.squares[i]
            
            if self.winner == 'n':
                '''check diagonals'''                
                if self.squares[0] == self.squares[4] and self.squares[8] == self.squares[0] and self.squares[0] != 'n':
                    self.winner = self.squares[0]
                
                if self.winner == 'n':
                    if self.squares[2] == self.squares[4] and self.squares[6] == self.squares[2] and self.squares[2] != 'n':
                        self.winner = self.squares[2]

class Tree:

    
    def __init__(self) -> None:
        
        squares = ('e','e','e',
                   'e','e','e',
                   'e','e','e')
        self.root = Board(squares)
        
    
    def generate_tree(self) -> Tree:
        pass
    
    
if __name__ == "__main__":
    
    tree = Tree()
