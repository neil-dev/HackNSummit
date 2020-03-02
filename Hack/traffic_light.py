import simpy
import random
from tkinter import *

class Clock:
    def __init__(self,canvas):
        self.canvas=canvas
        self.oval = canvas.create_oval(20,20,120,120,fill="green")
        self.rect = canvas.create_rectangle(150,20,250,70, fill ="white")
        self.txt = canvas.create_text(200,45,text = "",fill="red")
        self.rect1 = canvas.create_rectangle(150,90,250,140, fill ="white")
        self.txt1 = canvas.create_text(200,115,text = "")
        self.counter = canvas.create_text(60,140,text="",font="Times")
        self.red=0
        self.canvas.update()
        
    def tick(self,current_time, people):
        canvas.itemconfig(self.counter, text=str(current_time))
        # current_time += 1
        people = people + random.randint(0,3)
        canvas.itemconfig(self.txt1, text="People: "+str(people))
        if(self.red > 0):
            self.red -= 1
            canvas.itemconfig(self.txt, text=str(self.red))
            # canvas.after(1000,lambda : self.tick(current_time,0))
        elif(people > 15):
        # print("At {0} seconds\tpeople: {1}\tlight:{2}".format(env.now, people, "red"))
            self.red = 10
            canvas.itemconfig(self.txt, text=str(self.red))
            canvas.itemconfig(self.oval, fill="red")
            # canvas.after(1000,lambda : self.tick(current_time,0))
    # print("At {0} seconds\tpeople: {1}\tlight:{2}".format(env.now, people, "green"))
        else:
            canvas.itemconfig(self.oval, fill="green")
            canvas.itemconfig(self.txt, text="")
            # canvas.after(1000,lambda : tick(current_time,people))
        self.canvas.update()

    

#     while True:
#         print(name, env.now)
#         # myLabel2 = Label(root, text=str(env.now))
#         # myLabel2.pack()
#         # label.text = str(env.now)
#         yield env.timeout(tick)

def traffic(env, tick):
    # light = "green"
    people = 0
    while True:
        people = people + random.randint(0,3)
        if(people > 15):
            # light = red
            print("At {0} seconds\tpeople: {1}\tlight:{2}".format(env.now, people, "red"))
            # clock.config(text=str(env.now))
            # light.config(text="red")
            people = 0
            yield env.timeout(20)
        print("At {0} seconds\tpeople: {1}\tlight:{2}".format(env.now, people, "green"))
        # clock.config(text=str(env.now))
        # light.config(text="green")
        yield env.timeout(tick)

def create_clock(env):
    people = 0
    clock = Clock(canvas)
    while True:
        if clock.red >0 :
            people=0
        clock.tick(env.now,people)
        people = people + random.randint(0,3)
        yield env.timeout(1)

# root = Tk()

# e=Entry(root, width=10, borderwidth=5)
# e.grid(row=0, column=0,padx=10,pady=10)
# myLabel = Label(root, text="0")
# myLabel.pack()

# root = Tk()
# clock = Label(root, font = ("times", 50, "bold"), bg="white")
# light = Label(root, font = ("times", 50, "bold"), bg="white")
# clock.grid(row=0, column=1)
# light.grid(row=0, column=2)

root = Tk()
root.geometry('300x300')

canvas = Canvas(root, height=300, width=250, bg="white")

canvas.pack()

env = simpy.rt.RealtimeEnvironment(factor=0.5)
    # env = simpy.Environment()
    #env.process(clock(env, 'fast', 0.5))
# env.process(traffic(env, 1))
env.process(create_clock(env))
env.run(until=200)
mainloop()

# myLabel = Label(root, text="Hello world!")

# myLabel.pack()


