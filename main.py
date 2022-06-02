class game:
   
    def __init__(self):
        self.board=[['__ ' for i in range(3)] for j in range(3)]
        self.turn_count=0       
        self.print_board()
        self.player_one()
        
   
    def print_board(self):      
        print('\n')  
        for i in range(3):
            for j in range(3):
               
                print (self.board[i][j],end='')
            
            print('\n')
    
    def player_one(self):
        
        pos=int(input("Enter the position to play X : "))
        status=self.__modify_board(pos,"X  ")

        if(status==None):
            self.turn_count+=1
            self.player_two()
       
        if(status=="again"):
            self.player_one()

    def player_two(self):
       
        if(self.turn_count==9):
            print('\n'+"DRAW!"+'\n')
            return 

        pos=int(input("Enter the position to play O : "))
        status=self.__modify_board(pos,"O  ")
       
        if(status==None):
            self.turn_count+=1
            self.player_one()
        if(status=="again"):
            self.player_two()
    
    def __modify_board(self,inp,letter):
        
        count=0
        
        for i in range(3):
            for j in range(3):
                count+=1
                
                if(count==inp):
                    if(self.board[i][j]=='__ '):
                        self.board[i][j]=letter
                        self.print_board()
                    
                    else:
                        print('\n'+"position already played!"+'\n'+"Try again.."+'\n')
                        return ("again")
                    
                    if(self.__check_for_win()==True):
                        
                        if (letter=="X  "): print("player 1 has won!"+'\n')
                        if (letter=="O  "): print("player 2 has won!"+'\n')
                        return ("stop")

                    return None
     
        if(count==9):
            print('\n'+"Invalid Position"+'\n'+"try again..."+'\n')
            return ("again")
    
    def __check_for_win(self):
       
        for i in range(3):
           
            if (self.board[i][0]==self.board[i][1]==self.board[i][2]!='__ '):
                return True
           
            if (self.board[0][i]==self.board[1][i]==self.board[2][i]!='__ '):
                return True
           
            if (self.board[0][0]==self.board[1][1]==self.board[2][2]!='__ '):
                return True
           
            if (self.board[0][2]==self.board[1][1]==self.board[2][0]!='__ '):
                return True
           
            else:
                return False



game1=game()

