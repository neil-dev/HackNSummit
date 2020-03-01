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
color = ['red','green']
carimg = canvas.create_rectangle(car[0],car[1]-10,car[0]+10,car[1],fill=car[2])
sleeptimer = 0.05
tick = 5

traffic_lights = [{'xposition': 100, 'status': 1, 'people': 0}, {'xposition': 200, 'status': 1, 'people': 0}, {'xposition': 300, 'status': 1, 'people': 0},{'xposition': 400, 'status': 1, 'people': 0}]
for light in traffic_lights:
    light['status'] = random.randint(0,1)
    x = light['xposition']
    canvas.create_oval(x,175,x+10,185, fill=color[light['status']])
canvas.update()
counter = 0
next_traffic = 0
while True:
    counter += 1
    if counter > 60:
        for light in traffic_lights:
            if light['status'] == 0:
                light['status']=1
            else:
                light['status']=0
            x = light['xposition']
            canvas.create_oval(x,175,x+10,185, fill=color[light['status']])
        canvas.update()
        counter = 0
    speed = random.randint(0,3)
    car[0] += speed
    if speed % 3 == 0:
        for light in traffic_lights:
            light['people'] += random.randint(0,3)
            if light['people'] > 15:
                light['status'] = 0
                canvas.create_oval(x,175,x+10,185, fill=color[light['status']])
                canvas.update()
                for t in range(15):
                    counter += 1
                    time.sleep(sleeptimer)
                light['status']=1
                canvas.create_oval(x,175,x+10,185, fill=color[light['status']])
                canvas.update()


    if car[0] > traffic_lights[next_traffic]['xposition'] and traffic_lights[next_traffic]['people'] > 15:
        car[0] = traffic_lights[next_traffic]['xposition'] 
        correction = traffic_lights[next_traffic]['xposition'] - (car[0] - speed)
        canvas.move(carimg,correction,0)
        x = traffic_lights[next_traffic]['xposition']
        canvas.create_oval(x,175,x+10,185, fill="red")
        canvas.update()
        for t in range(15):
            counter += 1
            time.sleep(sleeptimer)
        canvas.create_oval(x,175,x+10,185, fill="green")
        canvas.update()
        car[3] = 0
        traffic_lights[next_traffic]['status'] = 1
        next_traffic += 1
        continue
    elif traffic_lights[next_traffic]['people'] > 15:
        x = traffic_lights[next_traffic]['xposition']
        canvas.create_oval(x,175,x+10,185, fill="red")
        canvas.update()
        for t in range(15):
            counter += 1
            speed = random.randint(0,3)
            if car[0] + speed <= x:
                car[0] += speed
                canvas.move(carimg,speed,0)
                canvas.update()
            else:
                canvas.move(carimg,x-car[0],0)
                canvas.update()
                car[3] = 0
            time.sleep(sleeptimer)
        canvas.create_oval(x,175,x+10,185, fill="green")
        canvas.update()
        traffic_lights[next_traffic]['status'] = 1
        continue

    if car[3] == 2:
        traffic_lights[next_traffic]['status'] = 0
    if(car[0] > traffic_lights[next_traffic]['xposition'] and car[3] != 2):
        car[3] += 1
        traffic_lights[next_traffic]['status'] = 1
        next_traffic += 1
    if(car[0] > traffic_lights[next_traffic]['xposition'] and traffic_lights[next_traffic]['status'] == 0):
        car[0] = traffic_lights[next_traffic]['xposition'] 
        correction = traffic_lights[next_traffic]['xposition'] - (car[0] - speed)
        canvas.move(carimg,correction,0)
    else:
        canvas.move(carimg,speed,0)
        canvas.update()


    time.sleep(sleeptimer)

mainloop()