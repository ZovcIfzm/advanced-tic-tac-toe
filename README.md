# tic-tac-toe
Tic tac toe with LAN, localhost, & one device multiplayer, AI, a GUI, dynamic size, and various settings including "Hidden mode"

## Multiplayer
For LAN or localhost multiplayer, type in your IP address and the port you wish you play on (any number between 1024-65535), otherwise type in 0 in those fields. The localhost IP is 127.0.0.1, and to find your Wi-Fi's IP address use ipconfig on Windows or ifconfig on Mac/Linux

Afterwards, press the "vs Player" button until you reach the Online option and start the game!

## Quickstart
Quickstart automatically fills in all field options (grid size: 9 "3x3", win length: 3 "3 in a row", IP: localhost, Port: 65005)

## Game fields
The Grid Size field determines the number of grid squares on the board. Entering 9 creates a 3x3 board, 16 a 4x4 board, and so on. You may also enter a number in between! The shape will be more rectangular if close to the previous square, or more square if close to the next square (10 is more rectangular, 15 is more square).

The Win Length field determines the number of icons in a row in order to win. Entering 3, means you have to get 3 in a row and so on.

The IP and Port fields are for multiplayer/localhost, if you're not playing multiplayer, enter 0 for each and don't select the online setting.

## vs AI
You can face an AI on varying difficulties by clicking the vs Player button to switch to vs AI. The AI is pretty smart on 3x3, but as you go to a larger number of grid squares it becomes less able to compete.

## Hidden
Only the last move is visible - basically a programmed version of mental tic tac toe

# Example pictures

## Home screen
<img src="https://github.com/ZovcIfzm/tic-tac-toe/blob/master/img/mainScreen.png" width="1000" height="200">

## Standard game
<img src="https://github.com/ZovcIfzm/tic-tac-toe/blob/master/img/standardGame.png" width="1000" height="450">

## 4x4 game
<img src="https://github.com/ZovcIfzm/tic-tac-toe/blob/master/img/4x4.png" width="1000" height="400">
