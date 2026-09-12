from time import sleep
from turtle import *

focal = 400
cam_x = 0.0
cam_y = 0.0
cam_z = 0.0

def move(x,y,z):
    goto(focal*(x-cam_x)/(z-cam_z),focal*(y-cam_y)/(z-cam_z))

def draw_line(x1,y1,z1,x2,y2,z2):
    penup()
    move(x1,y1,z1)
    pendown()
    move(x2,y2,z2)
    penup()

pressed = []
def key_press(event):
    k = event.keysym.lower()
    if k not in pressed:
        pressed.append(k)

def key_release(event):
    k = event.keysym.lower()
    if k  in pressed:
        pressed.remove(k)

getcanvas().bind_all('<KeyPress>',key_press)
getcanvas().bind_all('<KeyRelease>',key_release)


def key_down(key):
    if key in pressed:
        return 1
    else:
        return 0

def control():
    global cam_x,cam_y,cam_z
    cam_x += (key_down('d') - key_down('a')) / 10
    cam_y += (key_down('w') - key_down('s')) / 10
    cam_z += (key_down('e') - key_down('q')) / 10

setup(800,600)
bgcolor('black')
title("python版3d跑酷 a/d左右 w/s升降 e/p前后")
color("cyan")
pensize(2)
hideturtle()
tracer(0)

while True:
    clear()
    control()
    draw_line(1,-1,5,1,1,5)
    draw_line(1,1,5,-1,1,5)
    draw_line(-1,1,5,-1,-1,5)
    draw_line(-1,-1,5,1,-1,5)
    draw_line(1,-1,7,1,1,7)
    draw_line(1,1,7,-1,1,7)
    draw_line(-1,1,7,-1,-1,7)
    draw_line(1,-1,7,-1,-1,7) 
    draw_line(-1,-1,5,-1,-1,7)
    draw_line(1,-1,5,1,-1,7)
    draw_line(1,1,5,1,1,7)
    draw_line(-1,1,5,-1,1,7)
    update()
    sleep(0.03)