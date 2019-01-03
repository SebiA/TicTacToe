#Tic Tac Toe Game
from tkinter import *

class Board:
    
    #class attributes
    spaces = []
    spaceWidth = 10
    spaceHeight = 5
    clicks = 0
    
    #lists to keep track of spaces each player chooses
    x = []
    o = []
    
    spaceCoords = [] #list that stores grid coordinates of the corresponding space index
    
    def __init__(self,n=3): #creates board, default is 3 rows and 3 columns
        if n > 2 and n < 10: #the limit is 9 by 9, and 3 by 3 is the minimum size
            self.gridNum = n
            self.rows = n
            self.columns = n
        
    def drawSpaces(self,win): #creates a grid of buttons
        for i in range(self.rows):
            for j in range(self.columns):
                btn = Button(win,width=self.spaceWidth,height=self.spaceHeight,justify="center",bg="white")
                btn.grid(row=i,column=j) #buttons alligned to grid coordinates on screen
                self.spaces.append(btn)
                self.spaceCoords.append([j,i]) #for every button there is an x and y grid coordinate stored
                #adds the command after the button is created so the parameter is corresponding to the button index
                btn.config(command= lambda btn=btn: self.clickSpace(btn))
    
    def clickSpace(self,btn): #alternates between x and o, and changes the color
        spaceIndex = self.spaces.index(btn)
        currentSpace = self.spaces[spaceIndex]
        if self.clicks % 2 == 0:
            txt = "X"
            color = "blue"
            self.x.append(spaceIndex)
            self.checkWinner("X",self.x)
        else:
            txt = "O"
            color = "red"
            self.o.append(spaceIndex)
            self.checkWinner("O",self.o)
        self.clicks += 1
        currentSpace["text"] = txt #changes the button's text to x or o
        currentSpace.config(state=DISABLED,fg="white",bg=color) #disable the button once it is clicked
            
    #helper functions 
    def getSpaceX(self,spaceNum):#returns the X coordinate of a given space
        return self.spaceCoords[spaceNum][0]
    
    def getSpaceY(self,spaceNum):#returns the Y coordinate of a given space
        return self.spaceCoords[spaceNum][1]
  
    #win detection functions
    def checkWinner(self,txt,lst):
        if self.rowWin(lst) or self.colWin(lst) or self.fwdDiagWin(lst) or self.revDiagWin(lst):
            print(txt + " wins!")
            self.endGame()
        elif len(self.x)+len(self.o) == self.rows*self.columns:
            print("Tie!")
            self.endGame()
            
    def rowWin(self,lst): #function that checks if an entire row contains the same kind of space
        for y in range(self.rows):
            pts = 0 #helper variable used to store spaces of the same kind in a row
            for s in lst:
                if y == self.getSpaceY(s):
                    pts += 1
                    if pts == self.columns:
                        return True
        return False
            
    def colWin(self,lst): #similar to rowWin function
        for x in range(self.columns):
            pts = 0
            for s in lst:
                if x == self.getSpaceX(s):
                    pts += 1
                    if pts == self.rows:
                        return True
        return False                    
    
    def fwdDiagWin(self,lst):  #function that determines if the spaces are in a forward diagonal pattern
        pts = 0
        for s in lst:
            if self.getSpaceX(s) == self.getSpaceY(s): #x is same as y for each space
                pts += 1
                if pts == self.gridNum:
                    return True
        return False
    
    def revDiagWin(self,lst): #similar to fwdDiagWin function
        pts = 0
        for s in lst:
            if (self.gridNum-1) - self.getSpaceX(s) == self.getSpaceY(s):
                pts += 1
                if pts == self.gridNum:
                    return True
        return False
            
    def endGame(self): #disables all the buttons once game ends
        for s in self.spaces:
            s.config(state=DISABLED)
        print("Game Over")
    
#end of class Board        
        
def main():
    #window
    win = Tk()
    win.title = ("Tic Tac Toe")
    win.geometry = ("300x300")
    boardSize = 3 #value between 3 and 9, inclusive
    b = Board(boardSize) #creates board object
    b.drawSpaces(win)
    win.mainloop()
    
main()