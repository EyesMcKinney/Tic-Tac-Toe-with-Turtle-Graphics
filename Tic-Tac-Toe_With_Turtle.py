from turtle import *

The_Board = []
for i in range(3):
    row = []
    for x in range(3):
        row.append(" ")
    The_Board.append(row)

def draw_x(x, y):
    up()
    pensize(5)
    goto(x, y)
    right(45)
    pencolor("Red")
    down()
    for i in range(4):
        forward(50)
        back(50)
        right(90)
    left(135)


def draw_o(x, y):
    up()
    pensize(5)
    goto(x, y)
    pencolor("Blue")
    forward(25)
    down()
    left(90)
    circle(50)


def init(): # Game-Board
    speed(10)
    pensize(3)
    for i in range(2):
        up()
        goto(-300, 100 - 200 * i)
        down()
        forward(600)
    right(90)
    for i in range(2):
        up()
        goto(-100 + 200 * i, 300)
        down()
        forward(600)


def place_X(a, b):
    if The_Board[a][b] == "x" or The_Board[a][b] == "o":
        print("That spot is filled, please select another")
        a, b = player()
        place_X(a, b)
    else:
        draw_x(-200 + 200 * b, 200 - 200 * a)
        The_Board[a][b] = "x"


def place_O():
    for i in range(3):
        for x in range(3):
            if The_Board[i][x] == " ":
                The_Board[i][x] = "o"
                if win("o"):
                    draw_o(-200 + 200 * x, 200 - 200 * i)
                    return
                The_Board[i][x] = " "
    for i in range(3):
        for y in range(3):
            if The_Board[i][y] == " ":
                The_Board[i][y] = "x"
                if win("x"):
                    The_Board[i][y] = "o"
                    draw_o(-200 + 200 * y, 200 - 200 * i)
                    return
                The_Board[i][y] = " "
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if The_Board[i][j] == " ":
                The_Board[i][j] = "o"
                draw_o(-200 + 200 * j, 200 - 200 * i)
                return
    for i in range(3):
        for z in range(3):
            if The_Board[i][z] == " ":
                The_Board[i][z] = "o"
                draw_o(-200 + 200 * z, 200 - 200 * i)
                return


def win(z):
    for i in range(3):
        if The_Board[i][0] == The_Board[i][1] and The_Board[i][1] == The_Board[i][2] and The_Board[i][0] == z:
            return True
        if The_Board[0][i] == The_Board[1][i] and The_Board[1][i] == The_Board[2][i] and The_Board[0][i] == z:
            return True

    if The_Board[0][0] == The_Board[1][1] and The_Board[1][1] == The_Board[2][2] and The_Board[0][0] == z:
        return True
    if The_Board[0][2] == The_Board[1][1] and The_Board[1][1] == The_Board[2][0] and The_Board[0][2] == z:
        return True

    else:
        return False


def square(placement):
    if placement == 1:
        x = 0
        y = 0
        return x, y
    elif placement == 2:
        x = 0
        y = 1
        return x, y
    elif placement == 3:
        x = 0
        y = 2
        return x, y
    elif placement == 4:
        x = 1
        y = 0
        return x, y
    elif placement == 5:
        x = 1
        y = 1
        return x, y
    elif placement == 6:
        x = 1
        y = 2
        return x, y
    elif placement == 7:
        x = 2
        y = 0
        return x, y
    elif placement == 8:
        x = 2
        y = 1
        return x, y
    elif placement == 9:
        x = 2
        y = 2
        return x, y
    else:
        pass


def draw():
    count = 0
    for x in range(3):
        for y in range(3):
            if The_Board[x][y] == "x":
                count += 1
    if count > 3:
        return True
    else:
        return False


def player():
    placement = int(input("Enter a square to place: "))
    a, b = square(placement)
    return a, b


def game(): # Main
    init()
    player_moves = 0
    while player_moves <= 5:
        placement = int(input("Enter a square to place: "))
        x, y = square(placement)
        place_X(x, y)
        player_moves += 1
        if win("x"):
            print("You Won!")
            done()
        else:
            place_O()
            if win("o"):
                print("You lose!")
                done()
            elif draw():
                print("There was a tie!")
                done()


if __name__ == '__main__':
    game()
