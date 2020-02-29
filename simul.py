import simpy
import random
import time
from tkinter import *

root = Tk()
root.geometry('500x500')

canvas = Canvas(root, height =700, width = 900, bg ="white")

canvas.pack()
# color = ["red", "blue", "green"]
canvas.create_line(10,200,800,200,fill="black",width=3)
canvas.create_line(10,230,800,230,fill="black",width=3)

car = [20,200,"red",2]
carimg = canvas.create_rectangle(car[0],car[1]-10,car[0]+10,car[1],fill=car[2])

i=1
sleeptime = 0.05

color = ["red","green"]

# traffic_lights = []
# for j in range(0,27):
#     if j%3 == 2:
#         traffic_lights.append([60+30*j,0]) 
#         canvas.create_oval(,175,60+30*j+10,185,fill="red")
#     else:
#         traffic_lights.append([60+30*j,1]) 
#         canvas.create_oval(60+30*j,175,60+30*j+10,185,fill="green")
# count = 0
# flag1 = false
# flag2 = false
# flag3 = false

canvas.create_oval(60,175,70,185,fill="green")
while True:
    # canvas.delete()
    canvas.move(carimg,1,0)
    canvas.update()
    car[0] += 1

    if car[0] == 60:
        canvas.create_oval(60,175,70,185,fill="red")
        txt1 = canvas.create_text(65,170,font="Times",fill="red",text=str(30))
        heading = canvas.create_text(145, 250, fill="black",text="Demonstration of Normal Stoppage at Signal")
        canvas.update()
        for i in range(30):
            canvas.itemconfig(txt1,text=str(29-i))
            canvas.update()
            time.sleep(sleeptime)
        # time.sleep(sleeptime)
        canvas.itemconfig(txt1,text="")
        canvas.delete(heading)
        canvas.create_oval(60,175,70,185,fill="green")    
        canvas.create_oval(100,175,110,185,fill="green")
        canvas.update()
    if car[0] == 70:
        canvas.create_oval(60,175,70,185,fill="white", outline="white")
        canvas.update()    
    if car[0] == 100:
        canvas.create_oval(100,175,110,185,fill="red")
        canvas.create_text(105,155,font="Times",fill="red",text="Pedestrians over limit")
        txt2 = canvas.create_text(105,170,font="Times",fill="red",text=str(15))
        heading = canvas.create_text(145, 250, fill="black",text="Demonstration of Short-term Stoppage when Excess Pedestrians")
        canvas.update()
        for i in range(15):
            canvas.itemconfig(txt2,text=str(15-i))
            canvas.update()
            time.sleep(sleeptime)
        # time.sleep(sleeptime)
        canvas.itemconfig(txt2,text="")
        canvas.create_oval(100,175,110,185,fill="green") 
        canvas.create_oval(150,175,160,185,fill="green") 
        canvas.delete(heading)
        canvas.update() 
    if car[0]  == 110:  
        canvas.create_oval(100,175,110,185,fill="white", outline="white")
        canvas.update()    
    heading1 = canvas.create_text(165, 250, fill="black",text="")
    if car[0] == 135:
        canvas.itemconfig(heading1,text="Demonstration of Smart Crossing when less Traffic is present")
        canvas.create_oval(150,175,160,185,fill="red")
        canvas.update()
        # time.sleep(sleeptime)
    if car[0]>120 and car[0]<150:
        time.sleep(sleeptime*20)
    if car[0]  == 145:
        canvas.create_oval(150,175,160,185,fill="green")
        canvas.update()
    if car[0] == 150:
        canvas.delete(heading1)
    time.sleep(sleeptime)
        # canvas.create_oval(100,175,110,185,fill="green")

    # if i%30 == 0:
    #     for j in range(0,27):
    #         if j%3 == count:
    #             canvas.create_oval(60+30*j,175,60+30*j+10,185,fill="red")
    #         else:
    #             canvas.create_oval(60+30*j,175,60+30*j+10,185,fill="green")
    #     count = (count + 2) % 3
    #     for x in range(15):
    #         for car in cars:
    #             if car[3] != 2:
    #                 canvas.move(car[4],1,0)
    #                 # canvas.itemconfig(car[4],fill="white")
    #                 # canvas.create_rectangle(car[0]+1,car[1]-10,car[0]+10+1,car[1],fill=car[2])
    #                 canvas.update()
    #                 # car[0] = car[0] + 1
    #             i += 1
    #         time.sleep(sleeptime)
    #     for car in cars:
    #         car[3] = (car[3] + 1) % 3
    #     for j in range(0,27):
    #         canvas.create_oval(60+30*j,175,60+30*j+10,185,fill="green")
    # else:
    #     for car in cars:
    #         canvas.move(car[4],1,0)
    #         # canvas.itemconfig(car[4],fill="white")
    #         # canvas.create_rectangle(car[0]+1,car[1]-10,car[0]+10+1,car[1],fill=car[2])
    #         canvas.update()
    #         # car[0] += 1
    #     i+=1
    #     time.sleep(sleeptime)



# env = simpy.rt.RealtimeEnvironment(factor=0.5)
#     # env = simpy.Environment()
#     #env.process(clock(env, 'fast', 0.5))
# env.process(traffic(env, 1))
# env.process(create_clock(env))
# env.run(until=200)
mainloop()