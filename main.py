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


    def get_letter(self):
        
        if(self.turn_count%2==1):
            return("X  ")
       
        else:            
            return("O  ")


    def get_and_validate_play(self):
        
        pos=[]
        while(len(pos)!=2):
            pos=str(input("Enter the position to play "+self.get_letter()+": "))
            pos=pos.split()
       
        i,j=pos
        i,j=int(i),int(j)

        if(i>2 or j>2):
            self.play()
        
        else:
            return (i,j)
    

    def play(self):

        k,l=self.get_and_validate_play()
                                
        status=self.__modify_board(k,l,self.get_letter())
               
        if(status==None):
            self.turn_count+=1
            self.play() 
       
        elif(status=="again"):
            self.play()

        else:
            return
    
    def __modify_board(self,r,c,letter):
        
        if(self.board[r][c]=='__ '):
            self.board[r][c]=letter
            self.print_board()
        
        else:
            print('\n'+"position already played!"+'\n'+"Try again.."+'\n')
            return ("again")
        
        if(self.__check_for_win_or_draw()=="win"):
            
            if (letter=="X  "): print("player 1 has won!"+'\n')
            if (letter=="O  "): print("player 2 has won!"+'\n')
            return ("stop")
        
        elif(self.__check_for_win_or_draw()=="tie"):
            print('\n'+"DRAW!"+'\n')
            return ("stop")
     
        else:
            return None
    

    def __check_for_win_or_draw(self):

        if (self.board[0][0]==self.board[1][1]==self.board[2][2]!='__ '):
            return ("win")
        
        if (self.board[0][2]==self.board[1][1]==self.board[2][0]!='__ '):
            return ("win")
       
        for i in range(3):
           
            if (self.board[i][0]==self.board[i][1]==self.board[i][2]!='__ '):
                return ("win")
           
            if (self.board[0][i]==self.board[1][i]==self.board[2][i]!='__ '):
                return ("win")
        
        if(self.turn_count==9):
            return ("tie")
    
        return None
        



game1=game()

