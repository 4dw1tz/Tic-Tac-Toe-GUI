#TicTacToe
from tkinter import *

root=Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Tic-Tac-Toe by Witty_Coding")
root.config(bg="light green")

#The following functions describe what happens if their corresponding buttons are pressed
def x1y1():
    global Turn
    #Checks which player's turn it is by the Turn count. (Even=Player 1; Odd=Player 2)
    if Turn%2==0:
        x1y1B.config(text="O")
    else:
        x1y1B.config(text="X")
    #This following line disables the button once pressed to prevent it being pressed again or filled by another player
    x1y1B["state"]= "disabled"
    Turn+=1
    Play()	
def x2y1():
    global Turn
    if Turn%2==0:
        x2y1B.config(text="O")
    else:
        x2y1B.config(text="X")
    x2y1B["state"]= "disabled"
    Turn+=1
    Play()
def x3y1():
    global Turn
    if Turn%2==0:
        x3y1B.config(text="O")
    else:
        x3y1B.config(text="X")
    x3y1B["state"]= "disabled"
    Turn+=1
    Play()
def x1y2():
    global Turn
    if Turn%2==0:
        x1y2B.config(text="O")
    else:
        x1y2B.config(text="X")
    x1y2B["state"]= "disabled"
    Turn+=1
    Play()
def x2y2():
    global Turn
    if Turn%2==0:
        x2y2B.config(text="O")
    else:
        x2y2B.config(text="X")
    x2y2B["state"]= "disabled"
    Turn+=1
    Play()
def x3y2():
    global Turn
    if Turn%2==0:
        x3y2B.config(text="O")
    else:
        x3y2B.config(text="X")
    x3y2B["state"]= "disabled"
    Turn+=1
    Play()
def x1y3():
    global Turn
    if Turn%2==0:
        x1y3B.config(text="O")
    else:
        x1y3B.config(text="X")
    x1y3B["state"]= "disabled"
    Turn+=1
    Play()
def x2y3():
    global Turn
    if Turn%2==0:
        x2y3B.config(text="O")
    else:
        x2y3B.config(text="X")
    x2y3B["state"]= "disabled"
    Turn+=1
    Play()
def x3y3():
    global Turn
    if Turn%2==0:
        x3y3B.config(text="O")
    else:
        x3y3B.config(text="X")
    x3y3B["state"]= "disabled"
    Turn+=1
    Play()

def Play():
    #This is the main function that keeps iterating every turn after the start of the game until the end
    Main.config(text="Player "+str((Turn%2)+1)+"'s Turn")
    Main.place(x=125, y=0)
    #The following statements place the buttons created at the start of the game in their correct grid spaces.
    x1y1B.place(x=10, y=100)
    x1y2B.place(x=10, y=200)
    x1y3B.place(x=10, y=300)
    x2y1B.place(x=150, y=100)
    x2y2B.place(x=150, y=200)
    x2y3B.place(x=150, y=300)
    x3y1B.place(x=290, y=100)
    x3y2B.place(x=290, y=200)
    x3y3B.place(x=290, y=300)
    #Following Selection statements check the text inside each button after every turn to see if there's a winner
    #Rows
    if x1y1B["text"] == "O" and x2y1B["text"] == "O" and x3y1B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        #The following statements highlight the 3 winning boxes in a straight line in blue to make it obvious how a player won.
        x1y1B.config(bg="light blue")
        x2y1B.config(bg="light blue")
        x3y1B.config(bg="light blue")
    elif x1y1B["text"] == "X" and x2y1B["text"] == "X" and x3y1B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x1y1B.config(bg="light blue")
        x2y1B.config(bg="light blue")
        x3y1B.config(bg="light blue")
    elif x1y2B["text"] == "O" and x2y2B["text"] == "O" and x3y2B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x1y2B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x3y2B.config(bg="light blue")
    elif x1y3B["text"] == "X" and x2y2B["text"] == "X" and x3y2B["text"] == "X":
        Main.config(text="Player 1 (O) has won")
        x1y2B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x3y2B.config(bg="light blue")
    elif x1y3B["text"] == "O" and x2y3B["text"] == "O" and x3y3B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x1y3B.config(bg="light blue")
        x2y3B.config(bg="light blue")
        x3y3B.config(bg="light blue")
    elif x1y3B["text"] == "X" and x2y3B["text"] == "X" and x3y3B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x1y3B.config(bg="light blue")
        x2y3B.config(bg="light blue")
        x3y3B.config(bg="light blue")
    #Columns
    elif x1y1B["text"] == "O" and x1y2B["text"] == "O" and x1y3B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x1y1B.config(bg="light blue")
        x1y2B.config(bg="light blue")
        x1y3B.config(bg="light blue")
    elif x1y1B["text"] == "X" and x1y2B["text"] == "X" and x1y3B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x1y1B.config(bg="light blue")
        x1y2B.config(bg="light blue")
        x1y3B.config(bg="light blue")
    elif x2y1B["text"] == "O" and x2y2B["text"] == "O" and x2y3B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x2y1B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x2y3B.config(bg="light blue")
    elif x2y1B["text"] == "X" and x2y2B["text"] == "X" and x2y3B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x2y1B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x2y3B.config(bg="light blue")
    elif x3y1B["text"] == "O" and x3y2B["text"] == "O" and x3y3B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x3y1B.config(bg="light blue")
        x3y2B.config(bg="light blue")
        x3y3B.config(bg="light blue")
    elif x3y1B["text"] == "X" and x3y2B["text"] == "X" and x3y3B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x3y1B.config(bg="light blue")
        x3y2B.config(bg="light blue")
        x3y3B.config(bg="light blue")
    #Diagonals
    elif x1y1B["text"] == "O" and x2y2B["text"] == "O" and x3y3B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x1y1B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x3y3B.config(bg="light blue")
    elif x1y1B["text"] == "X" and x2y2B["text"] == "X" and x3y3B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x1y1B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x3y3B.config(bg="light blue")
    elif x3y1B["text"] == "O" and x2y2B["text"] == "O" and x1y3B["text"] == "O":
        Main.config(text="Player 1 (O) has won")
        x3y1B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x1y3B.config(bg="light blue")
    elif x3y1B["text"] == "X" and x2y2B["text"] == "X" and x1y3B["text"] == "X":
        Main.config(text="Player 2 (X) has won")
        x3y1B.config(bg="light blue")
        x2y2B.config(bg="light blue")
        x1y3B.config(bg="light blue")
    #If all boxes are filled (after 9 turns) the main lable will indicate that it's a tie
    elif Turn == 9:
        Main.config(text="It's a tie!")

#The variable "Turn" keeps incrementing with every turn of the game. It indicates which player's turn it is
global Turn
Turn=0
#The Main label is the large text widget at the top of the window which tells who's turn it is and who wins
Main=Label(root, text="Welcome!", font="ArielBold 20", bg="light green")
Main.place(x=160, y=0)
#The following sequence creates all the button widgets at the start of the game with the names as their co-ordinates.
x1y1B=Button(root, height=5, width=13, command=x1y1)
x2y1B=Button(root, height=5, width=13, command=x2y1)
x3y1B=Button(root, height=5, width=13, command=x3y1)
x1y2B=Button(root, height=5, width=13, command=x1y2)
x2y2B=Button(root, height=5, width=13, command=x2y2)
x3y2B=Button(root, height=5, width=13, command=x3y2)
x1y3B=Button(root, height=5, width=13, command=x1y3)
x2y3B=Button(root, height=5, width=13, command=x2y3)
x3y3B=Button(root, height=5, width=13, command=x3y3)
Play()

root.mainloop()
