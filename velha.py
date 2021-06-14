from random import randint
# POC de jogo da velha no console

grid = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
] #

def showGrid():
    for row in grid:
        print(row)

def win(user):
    print("\033[1;32;40m Bright Green" + user + " ganhou! \n")
      

def CheckWin():
    for row in range (0, len(grid)):
        if grid[row][0] == grid[row][1] == grid[row][2] != "_": # sequential row
            return True
        elif grid[0][row] == grid[1][row] == grid[2][row] != "_": # sequential col
            return True
        elif grid[0][0] == grid[1][1] == grid[2][2] != "_": # diagonal rt - lb 
            return True
        elif grid[0][2] == grid[1][1] == grid[0][2] != "_": # diagonal lt - rb 
            return True


def Play(player_char, coord):
    grid_selected = grid[int(coord[0])][int(coord[1])]
    if grid_selected == "_":
        grid[int(coord[0])][int(coord[1])] = player_char
        print (f"Modificando a casa {coord[0]}, {coord[1]}")
        showGrid()
        return True
    else:
        print("Casa selecionada inválida!")
        return False

def botPlay(player_char): 
    while True:
        coords = [randint(0, 2),randint(0, 2)]
        if Play(player_char, coords):
            break

def userPlay(player_char):
    while True:
        c = input("Insira a casa desejada [ex. '0 1']:")

        if Play(player_char, coords):
            break



userPlay("O")
botPlay("X")


while True:
    userPlay("X")
    if CheckWin():
        win("user")
        break
    botPlay("O")
    if CheckWin():
        win("bot")
        break   