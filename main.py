from tkinter import *
import random
import sys
import os

root = Tk()
root.title("камень, ножницы, бумага")
root.geometry("800x600")
root["bg"] = "#E6E6FA"

like = PhotoImage(file = 'like.png')
dislike = PhotoImage(file = 'dislike.png')
photo1 = PhotoImage(file = 'камень.png')
Label(root, image = photo1, borderwidth = 0, compound = "center", highlightthickness = 0, padx = 0, pady = 0).place(x = 290, y = 90)
photo2 = PhotoImage(file = 'ножницы.png')
Label(root, image = photo2, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 290, y = 250)
photo3 = PhotoImage(file = 'бумага.png')
Label(root, image = photo3, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 290, y = 410)

a = {1:"камень", 2:"ножницы", 3:"бумага"}
bot = a[random.randint(1, 3)]

a1 = {1:"ничья", 2:"вы победили", 3:"вы проиграли"}
if bot == a[1]:
    bot1 = a1[1]
if bot == a[2]:
    bot1 = a1[2]
if bot == a[3]:
    bot1 = a1[3]

a2 = {1:"вы проиграли", 2:"ничья", 3:"вы победили"}
if bot == a[1]:
    bot2 = a2[1]
if bot == a[2]:
    bot2 = a2[2]
if bot == a[3]:
    bot2 = a2[3]
    
a3 = {1:"вы победили", 2:"вы проиграли", 3:"ничья"}
if bot == a[1]:
    bot3 = a3[1]
if bot == a[2]:
    bot3 = a3[2]
if bot == a[3]:
    bot3 = a3[3]
 
stone = Button(text = "камень",
             background = "#00FF00",
             foreground = "#000000",
             padx = "59",
             pady = "50",
             font = "Arial 14")
stone.place(x = 75, y = 70)

scissors = Button(text = "ножницы",
             background = "#00FF00",
             foreground = "#000000",
             padx = "50",
             pady = "50",
             font = "Arial 14")
scissors.place(x = 75, y = 230)

paper = Button(text = "бумага",
             background = "#00FF00",
             foreground = "#000000",
             padx = "60",
             pady = "50",
             font = "Arial 14")
paper.place(x = 75, y = 390)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

new_game = Button(text = "новая игра",
             background = "#FFFF00",
             foreground = "#000000",
             padx = "32",
             pady = "16",
             font = "Arial 14",
             command = restart_program)
new_game.place(x = 500, y = 420)

text1 = Label(text = "сделайте выбор:", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 20")
text1.place(x = 110, y = 25)

def click_stone(event):
    text2 = Label(text = "выбор компьютера:", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 20")
    text2.place(x = 430, y = 260)
    text3 = Label(text = bot, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20",)
    text3.place(x = 430, y = 300)
    text4 = Label(text = bot1, foreground = "#000000", background = "#E6E6FA", font = "Arial 40")
    if bot2 == a2[1]:
        text4.place(x = 430, y = 104)
    else:
        text4.place(x = 430, y = 74)    
    if bot1 == a1[2]:
        Label(root, image = like, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 560, y = 140)
    if bot1 == a1[3]:
        Label(root, image = dislike, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 560, y = 140)    
    text5 = Label(text = "*", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 40")
    text5.place(x = 30, y = 118)
stone.bind("<Button-1>", click_stone)

def click_scissors(event):
    text2 = Label(text = "выбор компьютера:", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 20")
    text2.place(x = 430, y = 260) 
    text3 = Label(text = bot, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text3.place(x = 430, y = 300)
    text4 = Label(text = bot2, foreground = "#000000", background = "#E6E6FA", font = "Arial 40")
    if bot2 == a2[2]:
        text4.place(x = 430, y = 104)
    else:
        text4.place(x = 430, y = 74)
    if bot2 == a2[3]:
        Label(root, image = like, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 560, y = 140) 
    if bot2 == a2[1]:
        Label(root, image = dislike, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 560, y = 140)    
    text5 = Label(text = "*", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 40")
    text5.place(x = 30, y = 278)    
scissors.bind("<Button-1>", click_scissors)

def click_paper(event):
    text2 = Label(text = "выбор компьютера:", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 20")
    text2.place(x = 430, y = 260)
    text3 = Label(text = bot, foreground = "#0000FF", background = "#E6E6FA", font = "Arial 20")
    text3.place(x = 430, y = 300)
    text4 = Label(text = bot3, foreground = "#000000", background = "#E6E6FA", font = "Arial 40")
    if bot2 == a2[3]:
        text4.place(x = 430, y = 104)
    else:
        text4.place(x = 430, y = 74)    
    if bot3 == a3[1]:
        Label(root, image = like, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 560, y = 140) 
    if bot3 == a3[2]:
        Label(root, image = dislike, borderwidth = 0, compound = "center", highlightthickness = 0,padx = 0, pady = 0).place(x = 560, y = 140)    
    text5 = Label(text = "*", foreground = "#FF0000", background = "#E6E6FA", font = "Arial 40")
    text5.place(x = 30, y = 438)    
paper.bind("<Button-1>", click_paper)

root.mainloop()
