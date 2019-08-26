import numpy as np
from matplotlib import pyplot as plt

class game_2048:
    def __init__(self):
        '''Creates random starting board'''
        self.board=np.zeros((4,4),dtype=int)
        self.add_random()

    def print_board(self):
        '''Prints the board as a figure'''
        plt.clf()
        plt.xticks([])
        plt.yticks([])
        plt.imshow(np.log2(self.board),cmap='YlOrBr',
                   vmin=0,vmax=15)
        for i in range(4):
            for j in range(4):
                if self.board[i,j]:
                    plt.text(j,i,self.board[i,j],fontsize=20,
                             horizontalalignment='center',
                             verticalalignment='center')
        plt.show()
                
    def add_random(self):
        '''Adds one or two new tile, where are either 2 or 4'''
        for i in range(np.random.randint(1,3)):
            if (0 in self.board):
                value = 2 if np.random.rand() < 0.9 else 4
                pos = np.random.choice(np.where(self.board.flat==0)[0])
                self.board[pos//4,pos%4] = value
                
    def sweep(self):
        '''Moves all tiles as far left as possible'''
        for i in range(4):
            k = 0
            for j in range(4):
                if self.board[i,j] != 0:
                    curr = self.board[i,j]
                    self.board[i,j] = 0
                    self.board[i,k] = curr
                    k += 1
    
    def combine(self):
        '''Combines adjacent, identical values into sum'''
        for i in range(4):
            for j in range(3):
                if (self.board[i,j]==self.board[i,j+1]):
                    self.board[i,j]=2*self.board[i,j]
                    self.board[i,j+1]=0
                    break
        
    def move(self,x):
        '''Does move left (0), up (1), right (2), or down (3)'''
        
        #Flips or transposes board, depending on value of x
        if x%2:
            self.board = self.board.transpose()
        if x//2:
            self.board = np.flip(self.board,axis=1)
            
        #Slide tiles to the left, with combinations
        self.sweep()
        self.combine()
        self.sweep()

        #Undoes previous flip or tranpose
        if x//2:
            self.board = np.flip(self.board,axis=1)        
        if x%2:
            self.board = self.board.transpose()

        #Checks if board has empty spaces after move
        if not(0 in self.board):
            print('full')
            
        self.add_random()
    
game = game_2048()
plt.figure(0)
for i in range(100):
    game.move(0) 
    game.print_board()
    plt.pause(0.1)