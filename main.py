from tkinter import *
from tkinter import messagebox
import time
import random as rnd


root = Tk()
root.title("Snake")
root.resizable(0, 0)
canvas = Canvas(root, width=500, height=500)
canvas.pack()
root.update()

snakeItem = 10
coo1, coo2 = 25, 25
nav1, nav2 = 0, 0
snakeList = []
snakeSize = 3
foodList = []
foodQuantity = 7

for i in range(foodQuantity):
    x = rnd.randrange(50)
    y = rnd.randrange(50)
    oval = canvas.create_oval(x * snakeItem, y * snakeItem, x *
                              snakeItem + snakeItem, y * snakeItem + snakeItem, fill="red")
    foodList.append([x, y, oval])


def snake(canvas, x, y):
    global snakeList
    rec = canvas.create_rectangle(x * snakeItem, y * snakeItem, x *
                                  snakeItem + snakeItem, y * snakeItem + snakeItem, fill="purple")
    snakeList.append([x, y, rec])


snake(canvas, coo1, coo2)


def delete():
    if len(snakeList) >= snakeSize:
        temp = snakeList.pop(0)
        canvas.delete(temp[2])


def findFood():
    global snakeSize, foodQuantity
    for i in range(len(foodList)):
        if foodList[i][0] == coo1 and foodList[i][1] == coo2:
            snakeSize += 1
            foodQuantity -= 1
            canvas.delete(foodList[i][2])


def moveSnake(event):
    global coo1, coo2, nav1, nav2
    if event.keysym == "Up":
        nav1 = 0
        nav2 = -1
        delete()
    elif event.keysym == "Down":
        nav1 = 0
        nav2 = 1
        delete()
    elif event.keysym == "Left":
        nav1 = -1
        nav2 = 0
        delete()
    elif event.keysym == "Right":
        nav1 = 1
        nav2 = 0
        delete()
    coo1 = coo1 + nav1
    coo2 = coo2 + nav2
    snake(canvas, coo1, coo2)
    findFood()


canvas.bind_all("<KeyPress-Left>", moveSnake)
canvas.bind_all("<KeyPress-Right>", moveSnake)
canvas.bind_all("<KeyPress-Up>", moveSnake)
canvas.bind_all("<KeyPress-Down>", moveSnake)


def borders():
    if coo1 > 50 or coo1 < 0 or coo2 > 50 or coo2 < 0:
        messagebox.showerror("Game Over", "You touched the borders.")
        exit()


def touchSelf(fX, fY):
    global Game_Running
    if not (nav1 == 0 and nav2 == 0):
        for i in range(len(snakeList)):
            if snakeList[i][0] == fX and snakeList[i][1] == fY:
                messagebox.showerror("Game Over", "You touched yourself.")
                exit()


while True:
    delete()
    findFood()
    borders()
    touchSelf(coo1 + nav1, coo2 + nav2)
    coo1 = coo1 + nav1
    coo2 = coo2 + nav2
    snake(canvas, coo1, coo2)
    root.update_idletasks()
    root.update()
    time.sleep(0.1)
    if foodQuantity < 0:
        messagebox.showinfo("Thats it", "You won the game!")
        exit()
