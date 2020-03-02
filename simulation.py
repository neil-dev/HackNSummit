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
car1 = [20,230,"blue",2]
color = ['red','green']
carimg = canvas.create_rectangle(car[0],car[1]-10,car[0]+10,car[1],fill=car[2])
carimg2 = canvas.create_rectangle(car1[0],car1[1],car1[0]+10,car1[1]+10,fill=car1[2])
sleeptimer = 0.2
tick = 5

traffic_lights = [{'xposition': 20, 'status': 0, 'people': 0}, {'xposition': 80, 'status': 1, 'people': 1}, {'xposition': 140, 'status': 1, 'people': 0}]
# for light in traffic_lights:
#     light['status'] = random.randint(0,1)
#     x = light['xposition']
#     canvas.create_oval(x,175,x+10,185, fill=color[light['status']])

counter = -5
next_traffic = 1
for light in traffic_lights:
    x = light['xposition']
    canvas.create_oval(x,210,x+10,220, fill=color[light['status']])
canvas.update()
for i in range(5):
    counter += 1
    time.sleep(sleeptimer)
traffic_lights[0]['status'] = 1
x = traffic_lights[0]['xposition']
canvas.create_oval(x,210,x+10,220, fill=color[traffic_lights[0]['status']])
canvas.update()
flag = False
while True:
    counter += 1
    if counter > 60:
        for light in traffic_lights:
            x=light['xposition']
            light['status'] = light['status'] ^ 1
            canvas.create_oval(x,210,x+10,220, fill=color[light['status']])
        canvas.update()
        counter = 0
    speed = random.randint(0,3)
    car[0] += 2
    car1[0] += speed
    if car1[0] < traffic_lights[2]['xposition'] and traffic_lights[2]['status'] == 0:
        flag = True
    if car1[0] < traffic_lights[2]['xposition'] and flag == True:
        canvas.move(carimg2,traffic_lights[2]['xposition']-(car1[0]-speed),0)
        while True:
            canvas.move(carimg,2,0)
            canvas.update()    
            time.sleep(sleeptimer)
    if car[0] >= 78 and car[0] <80:
        if traffic_lights[1]['people'] == 1:
            canvas.create_oval(traffic_lights[1]['xposition'],210,traffic_lights[1]['xposition']+10,220, fill='red')
            canvas.update()
            for i in range(10):
                time.sleep(sleeptimer)
            canvas.create_oval(traffic_lights[1]['xposition'],210,traffic_lights[1]['xposition']+10,220, fill='green')
            canvas.update()
    # if car1[0] >= 77:
    #     if traffic_lights[1]['person'] == 1:
    #         canvas.create_oval(x,210,x+10,220, fill='red')
    #         canvas.update()
    #         for i in range(10):
    #             time.sleep(sleeptimer)
    #         canvas.create_oval(x,210,x+10,220, fill='green')
    #         canvas.update()
    canvas.move(carimg,2,0)
    canvas.move(carimg2,speed,0)
    canvas.update()
    time.sleep(sleeptimer)
    # if speed % 3 == 0:
    #     for light in traffic_lights:
    #         light['people'] += random.randint(0,3)
    #         if light['people'] > 15:
    #             light['status'] = 0
    #             canvas.create_oval(x,175,x+10,185, fill=color[light['status']])
    #             canvas.update()
    #             for t in range(15):
    #                 counter += 1
    #                 time.sleep(sleeptimer)
    #             light['status']=1
    #             canvas.create_oval(x,175,x+10,185, fill=color[light['status']])
    #             canvas.update()


    # if car[0] > traffic_lights[next_traffic]['xposition'] and traffic_lights[next_traffic]['people'] > 15:
    #     car[0] = traffic_lights[next_traffic]['xposition'] 
    #     correction = traffic_lights[next_traffic]['xposition'] - (car[0] - speed)
    #     canvas.move(carimg,correction,0)
    #     x = traffic_lights[next_traffic]['xposition']
    #     canvas.create_oval(x,175,x+10,185, fill="red")
    #     canvas.update()
    #     for t in range(15):
    #         counter += 1
    #         time.sleep(sleeptimer)
    #     canvas.create_oval(x,175,x+10,185, fill="green")
    #     canvas.update()
    #     car[3] = 0
    #     traffic_lights[next_traffic]['status'] = 1
    #     next_traffic += 1
    #     continue
    # elif traffic_lights[next_traffic]['people'] > 15:
    #     x = traffic_lights[next_traffic]['xposition']
    #     canvas.create_oval(x,175,x+10,185, fill="red")
    #     canvas.update()
    #     for t in range(15):
    #         counter += 1
    #         speed = random.randint(0,3)
    #         if car[0] + speed <= x:
    #             car[0] += speed
    #             canvas.move(carimg,speed,0)
    #             canvas.update()
    #         else:
    #             canvas.move(carimg,x-car[0],0)
    #             canvas.update()
    #             car[3] = 0
    #         time.sleep(sleeptimer)
    #     canvas.create_oval(x,175,x+10,185, fill="green")
    #     canvas.update()
    #     traffic_lights[next_traffic]['status'] = 1
    #     continue

    # if car[3] == 2:
    #     traffic_lights[next_traffic]['status'] = 0
    # if(car[0] > traffic_lights[next_traffic]['xposition'] and car[3] != 2):
    #     car[3] += 1
    #     traffic_lights[next_traffic]['status'] = 1
    #     next_traffic += 1
    # if(car[0] > traffic_lights[next_traffic]['xposition'] and traffic_lights[next_traffic]['status'] == 0):
    #     car[0] = traffic_lights[next_traffic]['xposition'] 
    #     correction = traffic_lights[next_traffic]['xposition'] - (car[0] - speed)
    #     canvas.move(carimg,correction,0)
    # else:
    #     canvas.move(carimg,speed,0)
    #     canvas.update()


    # time.sleep(sleeptimer)

mainloop()