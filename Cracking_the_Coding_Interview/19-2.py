
class tic_tac_toe:
    def __init__(self):
        self.black = 1
        self.white = 2
        self.empty = 0
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(self.empty)
                
    def put_black(self,x,y):
        if (x >= 3 or x < 0): return False
        if (y >= 3 or y < 0): return False
        if (self.board[y][x] != self.empty): return False
        self.board[y][x] = self.black
        return True

    def put_white(self,x,y):
        if (x >= 3 or x < 0): return False
        if (y >= 3 or y < 0): return False
        if (self.board[y][x] != self.empty): return False
        self.board[y][x] = self.white
        return True        
        
    def check_row(self, value):
        for i in range(3):
            if (self.board[i][0] == value and self.board[i][1] == value and self.board[i][2] == value):
                return True
        return False

    def check_column(self, value):
        for i in range(3):
            if (self.board[0][i] == value and self.board[1][i] == value and self.board[2][i] == value):
                return True
        return False
        
    def check_diagonal(self, value):    
        if (self.board[0][0] == value and self.board[1][1] == value and self.board[2][2] == value):
            return True
        if (self.board[0][2] == value and self.board[1][1] == value and self.board[2][0] == value):
            return True
        return False        
                    
    def check_black_success(self):
        result = False
        if (result == False): result = self.check_row(self.black)
        if (result == False): result = self.check_column(self.black)
        if (result == False): result = self.check_diagonal(self.black)        
        return result

    def check_white_success(self):
        result = False
        if (result == False): result = check_row(self.white)
        if (result == False): result = check_column(self.white)
        if (result == False): result = check_diagonal(self.white)        
        return result
       
    def print_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
         
ttt = tic_tac_toe()
ttt.put_black(0,0)
ttt.put_white(2,0)
ttt.put_black(0,2)
ttt.put_white(0,1)
ttt.put_black(2,2)
ttt.put_white(1,2)
ttt.put_black(1,1)
print("result = {0}".format(ttt.check_black_success()))
print("========================")
ttt.print_board()