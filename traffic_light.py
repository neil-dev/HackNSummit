import simpy
import random
from tkinter import *

# def clock(env, name, tick):
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

def create():
    env = simpy.rt.RealtimeEnvironment(factor=0.2)
    # env = simpy.Environment()
    #env.process(clock(env, 'fast', 0.5))
    env.process(traffic(env, 1))
    env.run(until=50)

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

c = Canvas(root, height=300, width=250, bg="white")

oval = c.create_oval(20,20,120,120,fill="green")
rect = c.create_rectangle(150,20,250,70, fill ="white")
txt = c.create_text(200,45,text = "")
rect1 = c.create_rectangle(150,90,250,140, fill ="white")
txt1 = c.create_text(200,115,text = "")

c.pack()

root.mainloop()
create()

# myLabel = Label(root, text="Hello world!")

# myLabel.pack()


