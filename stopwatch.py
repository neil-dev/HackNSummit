from tkinter import *
import random
import time

red = 0
def tick(current_time, people):
    global red
    c.itemconfig(txt, text=str(current_time))
    c.itemconfig(txt1, text=str(people))
    current_time += 1
    people = people + random.randint(0,3)
    if(red != 0):
        red -= 1
        c.after(1000,lambda : tick(current_time,0))
    elif(people > 15):
        # print("At {0} seconds\tpeople: {1}\tlight:{2}".format(env.now, people, "red"))
        c.itemconfig(oval, fill="red")
        people = 0
        red = 5
        c.after(1000,lambda : tick(current_time,0))
    # print("At {0} seconds\tpeople: {1}\tlight:{2}".format(env.now, people, "green"))
    else:
        c.itemconfig(oval, fill="green")
        c.after(1000,lambda : tick(current_time,people))
    
    # clock.config(text=str(current_time))
    # clock.after(1000,lambda : tick(current_time))

root = Tk()
root.geometry('300x300')

c = Canvas(root, height=300, width=250, bg="white")

oval = c.create_oval(20,20,120,120,fill="green")
rect = c.create_rectangle(150,20,250,70, fill ="white")
txt = c.create_text(200,45,text = "")
c.create_text(200,75,text="Time")
rect1 = c.create_rectangle(150,90,250,140, fill ="white")
txt1 = c.create_text(200,115,text = "")
c.create_text(200,150,text="People")
# txt = c.create_text(200,45,text = "Hello")
c.pack()
# clock = Label(root, font = ("times", 50, "bold"), bg="white")
# clock.grid(row=0, column=1)
tick(0,0)
root.mainloop()