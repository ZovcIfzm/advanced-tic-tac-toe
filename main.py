from tkinter import *
from tkinter import messagebox
import random
window=Tk()

window.title("Tic Tac Toe")
window.geometry("800x600")

player = "X"
turn = 0
hidden_grid = []
gamemode = "Standard"
aiMode = "vs Player"

button = []
settingButtons = []

def generate_seed():
    seed = []
    counter = 0
    while len(seed) < 9 and counter < 50:
        counter = 0
        rand = random.randint(0,8)
        for number in seed:
            if(rand == number):
                counter = counter + 1
        if(counter == 0):
            seed.append(rand)
    return seed

def begin():
    global hidden_grid
    global button

    lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
    lbl.grid(row=0,column=0)
    #lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
    #lbl.grid(row=1,column=0)
    #lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
    #lbl.grid(row=2,column=0)
    settingButtons.append(Button(window, text="Reset",bg="lightblue", fg="Black",width=7,height=1,font=('Helvetica','10'),command=lambda:reset()))
    settingButtons[0].grid(row = 1, column = 0)
    settingButtons.append(Button(window, text="Standard",bg="lightblue", fg="Black",width=7,height=1,font=('Helvetica','10'),command=lambda:settingsClick(settingButtons[1])))
    settingButtons[1].grid(row = 2, column = 0)
    settingButtons.append(Button(window, text="vs Player",bg="lightblue", fg="Black",width=7,height=1,font=('Helvetica','10'),command=lambda:aiClick(settingButtons[2])))
    settingButtons[2].grid(row = 3, column = 0)

    for i in range(9):
        button.append(Button(window, text=" ",bg="lightblue", fg="Black",width=3,height=1,font=('Helvetica','70'),command=lambda i=i:clicked(button[i], button, i)))
        hidden_grid.append(" ")
        button[i].grid(row=int(i/3+1), column=int(i%3+1))

def reset():
    global hidden_grid
    global turn
    global player
    global button
    global gamemode
    global aiMode
    global settingButtons

    for i in range(9):
        hidden_grid[i] = " ";
        button[i]["text"] = " "
    
    turn = 0
    player = "X"
    gamemode = "Standard"
    settingButtons[1]["text"] = "Standard"

    aiMode = "vs Player"
    settingButtons[2]["text"] = "vs Player" 

def switchPlayer():
    global player
    if(player == "X"):
        player = "O"
    elif(player == "O"):
        player = "X"

def clicked(self, button, number):
    global hidden_grid
    global gamemode
    global player
    global turn
    if hidden_grid[number] != "X" and hidden_grid[number] != "O":
        self["text"] = player
        hidden_grid[number] = player
        turn += 1
        if(gamemode == "Standard"):
            switchPlayer()
        elif(gamemode == "Hidden"):
            hide(number, button)
            switchPlayer()
        check()
        if(aiMode == "vs AI" and gamemode != "Over"):
            turnAI(hidden_grid, player)
            check()

def settingsClick(self):
    global gamemode
    if(gamemode == "Hidden"):
        unhide()
        gamemode = "Standard"
    elif(gamemode == "Standard"):
        gamemode = "Hidden"
    self["text"] = gamemode

def aiClick(self):
    global aiMode
    if(aiMode == "vs Player"):
        aiMode = "vs AI"
    elif(aiMode == "vs AI"):
        aiMode = "vs Player"
    self["text"] = aiMode

def check():   
    global turn 
    global hidden_grid
    lock = True
    for i in range(3):
        if(hidden_grid[3*i] == hidden_grid[3*i+1] == hidden_grid[3*i+2] != " "):
            win(hidden_grid[3*i])
            break
        elif(hidden_grid[i] == hidden_grid[i+3] == hidden_grid[i+6] != " "):
            win(hidden_grid[i])
            break
        elif(hidden_grid[0] == hidden_grid[4] == hidden_grid[8] != " "):
            win(hidden_grid[0])
            break
        elif(hidden_grid[2] == hidden_grid[4] == hidden_grid[6] != " "):
            win(hidden_grid[2])
            break
        else:
            lock == False
    if turn > 8 and lock == False:
        win(" ")         

def hide(exception, button):
    for i in range(9):
        if(i != exception):
            button[i]["text"] = " "
        
def unhide():
    global hidden_grid
    for i in range(9):
        if(button[i]["text"] != hidden_grid[i]):
            button[i]["text"] = hidden_grid[i]

def win(player):
    global gamemode
    gamemode = "Over"
    unhide()
    if player == " ":
        messagebox.showinfo("Game finished" ,"Tie game")
        reset()
    else:
        ans = "Game complete " + player + " wins "
        messagebox.showinfo("Congratulations", ans)
        reset()


def turnAI(entryGrid, player):
    predictionGrid = []
    for i in range(9):
        predictionGrid.append(entryGrid[i])

    decision = possibilitySearch(predictionGrid, player)

    global hidden_grid
    global button

    if(decision != 10):
        hidden_grid[decision] = player
        button[decision]["text"] = player
        if(gamemode == "Hidden"):
            hide(decision, button)
    global turn
    turn = turn + 1
    switchPlayer()

def possibilitySearch(predictionGrid, aiPlayer):
    originalPlayer = aiPlayer
    iterationNumber = 0
    iterationLimit = 10
    aiOptions = []
    tempGrid = []
    for i in range(9):
        aiOptions.append(0)
        tempGrid.append(predictionGrid[i])

    while (iterationNumber < iterationLimit):
        j = 0
        seed = generate_seed()

        while(j < 9): #each value of the seed is a unique number between 0-8 inclusive
            if tempGrid[seed[j]] == " ":
                tempGrid[seed[j]] = aiPlayer
                aiOptions[seed[0]] += checkPrediction(tempGrid, originalPlayer)

                #create baseline options - if it's blank it has - some - weight
                if aiOptions[seed[j]] == 0:
                    aiOptions[seed[j]] = 0.001

                if aiPlayer == "X":
                    aiPlayer = "O"
                elif aiPlayer == "O":
                    aiPlayer = "X"
            elif tempGrid[seed[j]] != " ": #this works, because each part of the grid is selected only once,
                #and so this statement basically says that if the actual (hidden_grid) had an
                #icon here, then weight this move as -100 (don't make this move)
                aiOptions[seed[j]] = -100
            j = j + 1
        iterationNumber = iterationNumber + 1
        
        for i in range(9):
            tempGrid[i] = predictionGrid[i]

    highestNumber = -1000
    finalDecision = 0
    for i in range(9):
        if aiOptions[i] > highestNumber:
            highestNumber = aiOptions[i]
            finalDecision = i
    if(highestNumber == -100):
        finalDecision = 10
    return finalDecision


def checkPrediction(predictionGrid, aiPlayer):
    #defining what icon the opponent is
    if aiPlayer == "X":
        opPlayer = "O"
    elif aiPlayer == "O":
        opPlayer = "X"

    counter = 0
    for i in range(9):
        if(predictionGrid[i] != " "):
            counter = counter + 1

    for i in range(3):
        #first two are for rows, second two are for columns, last two are for diagonals- all for 3x3 only
        if(predictionGrid[3*i] == predictionGrid[3*i + 1] == predictionGrid[3*i + 2] == aiPlayer):
            return 1
        elif(predictionGrid[3*i] == predictionGrid[3*i + 1] == predictionGrid[3*i + 2] == opPlayer):
            return -0.5
        elif(predictionGrid[i] == predictionGrid[i + 3] == predictionGrid[i + 6] == aiPlayer):
            return 1
        elif(predictionGrid[i] == predictionGrid[i + 3] == predictionGrid[i + 6] == opPlayer):
            return -0.5
        elif(predictionGrid[0] == predictionGrid[4] == predictionGrid[8] == aiPlayer):
            return 1
        elif(predictionGrid[0] == predictionGrid[4] == predictionGrid[8] == opPlayer):
            return -0.5
        elif(predictionGrid[2] == predictionGrid[4] == predictionGrid[6] == aiPlayer):
            return 1
        elif(predictionGrid[2] == predictionGrid[4] == predictionGrid[6] == opPlayer):
            return -0.5
    return 0

def main():
    begin()    
    window.mainloop()


if __name__ == "__main__":
    main()
