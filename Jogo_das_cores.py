from csv import *
import tkinter
from tkinter import *
from tkinter import messagebox
import os
from tempfile import NamedTemporaryFile
import shutil
from operator import itemgetter

root = Tk()
root.title("Tela base")
root.geometry('750x200')
main_lst = []
import tkinter 
import random 
global colours
colours = ['Red','Blue','Green','Black',
           'Yellow','White']
global user
global score



def countdown():     
    global timeleft
    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 

        timeLabel.after(1000, countdown)
    else:
        Score_update()

def Score_update():
    global user
    global score

    filename = "data_entry.csv"
    tempfile = NamedTemporaryFile(mode='a', delete=False, newline='')

    with open(filename, "r", newline='')as file, tempfile:
        Reader = reader(file)
        Writer = writer(tempfile)
        lst = [user,score]
        for Row in Reader:
            if user == Row[0]:
                Row[1] = score
            Writer.writerow(Row)

    shutil.move(tempfile.name, filename)
    Update()
    
timeleft = 30

def startGame(event): 

    if timeleft == 30: 

        countdown()
        
    nextColour() 

def nextColour():
    global colours
    global label
    global scoreLabel 
    global score
    global timeleft
 
    if timeleft > 0:
 
        e.focus_set()
 
        if e.get().lower() == colours[1].lower():
             
            score += 1
 
        e.delete(0, END)
         
        random.shuffle(colours)
         
        label.config(fg = str(colours[1]), text = str(colours[0]))
         
        scoreLabel.config(text = "Score: " + str(score))
            
def getcolour(text):
    global e
    e.delete(0,END)
    e.insert(0,text)
    return
    
def new_game():
   global timeleft
   global timeLabel
   global btn
   global scoreLabel
   global label 
   global e


   newWindow = Toplevel(root)

   newWindow.title("New Window")

   newWindow.geometry("1000x600")
   tela_base = Label (newWindow,text = "Bem vindo,Por favor digite seu nome",
        font = ('Red hat Mono',)) 
   btn = Button(newWindow, text = '      ', bg = "red",
        command = lambda:getcolour("red"))
   btn.grid(row=3,column=0)
   btn2 = Button(newWindow, text = '      ', bg = "blue",
                            command = lambda:getcolour("blue"))
   btn2.grid(row=3,column=1)

   btn3 = Button(newWindow, text = '      ', bg = "green",
                            command = lambda:getcolour("green"))
   btn3.grid(row=3,column=2)

   btn4 = Button(newWindow, text = '      ', bg = "yellow",
                            command = lambda:getcolour("yellow"))
   btn4.grid(row=4,column=0)

   btn5 = Button(newWindow, text = '      ', bg = "white",
                            command = lambda:getcolour("white"))
   btn5.grid(row=4,column=1)

   btn6 = Button(newWindow, text = '      ', bg = "black",
                            command = lambda:getcolour("black"))
   btn6.grid(row=4,column=2)
   scoreLabel = Label(newWindow, text = "Press enter to start", 
                                        font = ('Red Hat Mono', 12))
   scoreLabel.grid(row=1,column=2)
   timeLabel = Label(newWindow, text = "Time left: " +
                str(timeleft), font = ('Red Hat Mono', 12)) 

   timeLabel.grid(row=2,column=2)
   label = Label(newWindow, font = ('Red Hat Mono', 60)) 
   label.grid(row=3,column=4)
   e = Entry(newWindow) 
   newWindow.bind('<Return>', startGame) 
   e.grid(row=0,column=0)
   e.focus_set()
    
def Update():
    users = []
    top_players = []
    with open("data_entry.csv", "r", newline='')as file:
        Reader = reader(file)
        for i, Row in enumerate(Reader):
            if i != 0:
                users.append((Row[0],int(Row[1])))
    N = 3
 
    print(users)

    top_players = sorted(users, key = itemgetter(1), reverse = True)[:N]

    print(top_players)

    top1.configure(text=top_players[0][0])
    top2.configure(text=top_players[1][0])
    top3.configure(text=top_players[2][0])
    pontos1.configure(text=top_players[0][1])
    pontos2.configure(text=top_players[1][1])
    pontos3.configure(text=top_players[2][1])

def List():
    with open("data_entry.csv", "r", newline='') as file:
        Reader = reader(file)
        for row in Reader:
            print(row)

def Save():
    global score
    global user
    user = txt.get()
    score = 0
    lst = [user ,score]
    main_lst.append(lst) 
    with open("data_entry.csv", "r", newline='') as file:
        Reader = reader(file)
        for row in Reader:
            if user == row[0]:
                messagebox.showinfo("Information",f"Usuário já Existente: {user}")
                new_game()
                return

    with open("data_entry.csv", "a", newline='') as file:
        Writer = writer(file)
        Writer.writerow(lst)
        messagebox.showinfo("Information", "Jogador cadastrado")
    new_game()



txt = Entry(root, width=10)
txt.grid(column=5, row=5)

lbl = Label(root, text="Bem vindo,Por favor digite seu nome")
lbl.grid(column=3, row=3)
nomes = Label(root, text='Nome')
nomes.grid(row=3, column=10)
pontos = Label(root, text='    Pontuação')
pontos.grid(row=3, column=40)
top1 = Label(root, text='         ',)
top1.grid(row=4, column=10)

top2 = Label(root, text='          ',)
top2.grid(row=5, column=10)

top3 = Label(root, text='          ',)
top3.grid(row=6, column=10)

pontos1 = Label(root, text='        ',)
pontos1.grid(row=4, column=40)

pontos2 = Label(root, text='        ',)
pontos2.grid(row=5, column=40)

pontos3 = Label(root, text='        ',)
pontos3.grid(row=6, column=40)


entrar_jogo = Button(root, text='Iniciar jogo', command=Save)
entrar_jogo.grid(row=5, column=3)


timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Red Hat Mono', 12))
Update() 
root.mainloop()