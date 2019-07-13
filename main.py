from tkinter import *
from tkinter import messagebox
window=Tk()

window.title("Tic Tac Toe")
window.geometry("800x600")

player = "X"
turn = 0
hidden_grid = [9]
gamemode = "Standard"

def begin():
    global hidden_grid

    lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
    lbl.grid(row=0,column=0)
    lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
    lbl.grid(row=1,column=0)
    lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
    lbl.grid(row=2,column=0)
    buttonClick = []
    buttonClick.append(Button(window, text="Standard",bg="gray", fg="Black",width=7,height=1,font=('Helvetica','10'),command=lambda:settingsClick(buttonClick[0])))
    buttonClick[0].grid(row = 3, column = 0)

    button = []
    for i in range(9):
        button.append(Button(window, text=" ",bg="gray", fg="Black",width=3,height=1,font=('Helvetica','70'),command=lambda i=i:clicked(button[i], button, i)))
        hidden_grid.append(" ")
        button[i].grid(column=int(i/3+1), row=int(i%3+1))

def clicked(self, button, number):
    global turn
    global hidden_grid
    global gamemode
    lock = "true"
    if turn % 2 == 0 and hidden_grid[number] != "X" and hidden_grid[number] != "O":
        self["text"]="X"
        hidden_grid[number] = "X"
        turn += 1
        lock = "false"
    elif turn % 2 == 1 and hidden_grid[number] != "X" and hidden_grid[number] != "O":
        self["text"]="O"
        hidden_grid[number] = "O"
        turn += 1

    if(gamemode == "Hidden" and lock == "false"):
        hide(player, number, button)
    check(button)

def settingsClick(self):
    global gamemode
    if(gamemode == "Hidden"):
        gamemode = "Standard"
    elif(gamemode == "Standard"):
        gamemode = "Hidden"
    self["text"] = gamemode

def check(self):   
    global turn 
    global hidden_grid
    for i in range(3):
        if(hidden_grid[3*i] == hidden_grid[3*i+1] == hidden_grid[3*i+2] != " "):
            win(hidden_grid[3*i])
        elif(hidden_grid[i] == hidden_grid[i+3] == hidden_grid[i+6] != " "):
            win(hidden_grid[i])
    if(hidden_grid[0] == hidden_grid[4] == hidden_grid[8] != " "):
        win(hidden_grid[0])
    elif(hidden_grid[2] == hidden_grid[4] == hidden_grid[6] != " "):
        win(hidden_grid[2])
    elif turn == 9:
        win(" ")
'''
        if(self[3*i]["text"] == self[3*i+1]["text"] == self[3*i+2]["text"] != " "):
            win(self[3*i]["text"])
        elif(self[i]["text"] == self[i+3]["text"] == self[i+6]["text"] != " "):
            win(self[i]["text"])
    if(self[0]["text"] == self[4]["text"] == self[8]["text"] != " "):
        win(self[0]["text"])
    if(self[2]["text"] == self[4]["text"] == self[6]["text"] != " "):
        win(self[2]["text"])
'''
    
def hide(player, exception, button):
    for i in range(9):
        if(button[i]["text"] != player and i != exception):
            button[i]["text"] = " "
        

def win(player):
    global turn
    if turn == 9 and player == " ":
        messagebox.showinfo("Game finished" ,"Tie game")
        window.destroy()  # is used to close the program
    else:
        ans = "Game complete " +player + " wins "
        messagebox.showinfo("Congratulations", ans)
        window.destroy()  # is used to close the program

def main():
    begin()    
    window.mainloop()


if __name__ == "__main__":
    main()




''' Reference tutorial - can be simplified

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn=1; #For first person turn.

def clicked1():
    global turn
    if btn1["text"]==" ":   #For getting the text of a button
        if turn==1:
            turn =2;
            btn1["text"]="X"
        elif turn==2:
            turn=1;
            btn1["text"]="O"
        check();
def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn =2;
            btn2["text"]="X"
        elif turn==2:
            turn=1;
            btn2["text"]="O"
        check();
def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn =2;
            btn3["text"]="X"
        elif turn==2:
            turn=1;
            btn3["text"]="O"
        check();
def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn =2;
            btn4["text"]="X"
        elif turn==2:
            turn=1;
            btn4["text"]="O"
        check();
def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn =2;
            btn5["text"]="X"
        elif turn==2:
            turn=1;
            btn5["text"]="O"
        check();
def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn =2;
            btn6["text"]="X"
        elif turn==2:
            turn=1;
            btn6["text"]="O"
        check();
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn =2;
            btn7["text"]="X"
        elif turn==2:
            turn=1;
            btn7["text"]="O"
        check();
def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn =2;
            btn8["text"]="X"
        elif turn==2:
            turn=1;
            btn8["text"]="O"
        check();
def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn =2;
            btn9["text"]="X"
        elif turn==2:
            turn=1;
            btn9["text"]="O"
        check();
flag=1;
def check():
    global flag;
    b1 = btn1["text"];
    b2 = btn2["text"];
    b3 = btn3["text"];
    b4 = btn4["text"];
    b5 = btn5["text"];
    b6 = btn6["text"];
    b7 = btn7["text"];
    b8 = btn8["text"];
    b9 = btn9["text"];
    flag=flag+1;
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"]);
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"]);
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"]);
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"]);
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"]);
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"]);
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"]);
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program


btn1 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
btn9.grid(column=3, row=3)

window.mainloop()

'''