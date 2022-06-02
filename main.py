class game:
   
    def __init__(self):
        self.board=[['__ ' for i in range(3)] for j in range(3)]
        self.turn_count=1      
        self.print_board()
        self.play()
        
   
    def print_board(self):      
        print('\n')  
        for i in range(3):
            for j in range(3):
               
                print (self.board[i][j],end='')
            
            print('\n')
    
    def play(self):
       
        if(self.turn_count==9):
            print('\n'+"DRAW!"+'\n')
            return 
        
        if(self.turn_count%2==1):
            let="X  "
       
        else:            
            let="O  "

            pos=[]
            while(len(pos)!=2):
                pos=str(input("Enter the position to play ",let,": "))
                pos=pos.split()
                                    
            status=self.__modify_board(pos,let)
               
        if(status==None):
            self.turn_count+=1
            self.play()
       
        if(status=="again"):
            self.play()
    
    def __modify_board(self,inp,letter):
        
        count=0
        i,j=inp
        i,j=int(i),int(j)

        if(i>2 or j>2):
            print('\n'+"Invalid Position"+'\n'+"try again..."+'\n')
            return ("again")

        
        if(self.board[i][j]=='__ '):
            self.board[i][j]=letter
            self.print_board()
        
        else:
            print('\n'+"position already played!"+'\n'+"Try again.."+'\n')
            return ("again")
        
        if(self.__check_for_win()):
            
            if (letter=="X  "): print("player 1 has won!"+'\n')
            if (letter=="O  "): print("player 2 has won!"+'\n')
            return ("stop")
     
        else:
            return None
    
    def __check_for_win(self):

        if (self.board[0][0]==self.board[1][1]==self.board[2][2]!='__ '):
            return True
        
        if (self.board[0][2]==self.board[1][1]==self.board[2][0]!='__ '):
            return True
       
        for i in range(3):
           
            if (self.board[i][0]==self.board[i][1]==self.board[i][2]!='__ '):
                return True
           
            if (self.board[0][i]==self.board[1][i]==self.board[2][i]!='__ '):
                return True
       
        return False
        



game1=game()

