import turtle
import time
import threading


#variables
mid_jump = False
mining = True
bullet_speed = 10
start = 0

#screen
screen = turtle.Screen()
screen.bgpic('backdrop.gif')
screen.setup(width=656, height=344)
screen.register_shape('miner_right.gif')
screen.register_shape('miner_left.gif')
screen.register_shape('miner_jump_left.gif')
screen.register_shape('miner_jump_left2.gif')
screen.register_shape('miner_jump_left3.gif')
screen.register_shape('miner_jump_left4.gif')
screen.register_shape('miner_jump_left5.gif')
screen.register_shape('miner_jump_right.gif')
screen.register_shape('miner_jump_right2.gif')
screen.register_shape('miner_jump_right3.gif')
screen.register_shape('miner_jump_right4.gif')
screen.register_shape('miner_jump_right5.gif')
screen.register_shape('camera_left.gif')
screen.register_shape('camera_left_frame1.gif')
screen.register_shape('camera_left_frame2.gif')
screen.register_shape('camera_left_frame3.gif')
screen.register_shape('camera_left_frame4.gif')
screen.register_shape('camera_right.gif')
screen.register_shape('camera_right_frame1.gif')
screen.register_shape('camera_right_frame2.gif')
screen.register_shape('camera_right_frame3.gif')
screen.register_shape('camera_right_frame4.gif')
screen.register_shape('prop.gif')
screen.register_shape('sign.gif')


#turtles
user = turtle.Turtle()
user.ht()
user.pu()
user.shape('miner_left.gif')
user.setpos(-150, -100)
user.setheading(180)
user.st()


camera1 = turtle.Turtle()
camera1.ht()
camera1.pu()
camera1.shape('camera_left.gif')
camera1.setpos(250, 110)
camera1.st()

camera2 = turtle.Turtle()
camera2.ht()
camera2.pu()
camera2.shape('camera_right.gif')
camera2.setpos(-250, 110)
camera2.st()

bullet = turtle.Turtle()
bullet.ht()
bullet.pu()
bullet.color('red')
bullet.setpos(camera1.pos())

bullet2 = turtle.Turtle()
bullet2.ht()
bullet2.pu()
bullet2.color('blue')
bullet2.setpos(camera2.pos())

poster = turtle.Turtle()
poster.ht()
poster.shape('prop.gif')
poster.pu()
poster.setpos(150, -10)
poster.st()

sign = turtle.Turtle()
sign.ht()
sign.shape('sign.gif')
sign.pu()
sign.setpos(250, 150)
sign.st()

#turtle functions/movement

def hit_check():
    if user.distance(bullet.pos()) <= 7 or user.distance(bullet2.pos()) <= 7:
        screen.clear()
        screen.bgcolor('black')
        screen.textinput(title='Congrats!', prompt=f'You lasted {time.time() - start} seconds! Save Your Name?')
    threading.Timer(0.1, hit_check).start()



def set_bullet():
    bullet.setheading(bullet.towards(user.xcor(), user.ycor()))
    bullet.st()

def set_bullet2():
    bullet2.setheading(bullet2.towards(user.xcor(), user.ycor()))
    bullet2.st()



def bullet_move():
    bullet.fd(bullet_speed)
    bullet2.fd(bullet_speed)
    threading.Timer(0.1, bullet_move).start()

def bullet_check():
    global bullet_speed
    if bullet.ycor() <= -150 or bullet.xcor() <= -300 or bullet.xcor() >= 300:
        bullet.ht()
        bullet.setpos(camera1.pos())
        set_bullet()
        bullet_speed += 3
    if bullet2.ycor() <= -150 or bullet2.xcor() <= -300 or bullet2.xcor() >= 300:
        bullet2.ht()
        bullet2.setpos(camera2.pos())
        set_bullet2()
        bullet_speed += 3
    threading.Timer(0.1, bullet_check).start()



def camera_confused_animation():
    camera1.shape('camera_left_frame1.gif')
    camera2.shape('camera_right_frame1.gif')
    time.sleep(0.5)
    camera1.shape('camera_left_frame2.gif')
    camera2.shape('camera_right_frame2.gif')
    time.sleep(0.5)
    camera1.shape('camera_left_frame3.gif')
    camera2.shape('camera_right_frame3.gif')
    time.sleep(0.5)
    camera1.shape('camera_left_frame4.gif')
    camera2.shape('camera_right_frame4.gif')
    time.sleep(0.5)
    camera1.shape('camera_left.gif')
    camera2.shape('camera_right.gif')


def jump_right_animation():
    time.sleep(0.1)
    user.shape('miner_jump_right2.gif')
    time.sleep(0.1)
    user.shape('miner_jump_right3.gif')
    time.sleep(0.1)
    user.shape('miner_jump_right4.gif')
    time.sleep(0.1)
    user.shape('miner_jump_right5.gif')
    time.sleep(0.1)
    user.shape('miner_jump_right.gif')

def jump_left_animation():
    time.sleep(0.1)
    user.shape('miner_jump_left2.gif')
    time.sleep(0.1)
    user.shape('miner_jump_left3.gif')
    time.sleep(0.1)
    user.shape('miner_jump_left4.gif')
    time.sleep(0.1)
    user.shape('miner_jump_left5.gif')
    time.sleep(0.1)
    user.shape('miner_jump_left.gif')

def right():
    user.shape('miner_right.gif')
    if user.heading() != 0:
        user.setheading(0)
    user.fd(10)


def left():
    user.shape('miner_left.gif')
    if user.heading() != 180:
        user.setheading(180)
    user.fd(10)

def jump():
    global mid_jump
    if mid_jump == False:
        if user.heading() == 0:
            user.shape('miner_jump_right.gif')
        elif user.heading() == 180:
            user.shape('miner_jump_left.gif')
        time.sleep(0.1)
        mid_jump = True
        user.sety(user.ycor() + 75)
        if user.heading() == 0:
            user.setx(user.xcor() + 75)
        elif user.heading() == 180:
            user.setx(user.xcor() - 75)
        time.sleep(0.3)
        user.sety(user.ycor() - 75)
        mid_jump = False


def stop_mining():
    global mining, start
    mining = False
    start = time.time()

#main

screen.textinput(title='Controls', prompt='space to stop mining, w to jump, a to move left, d to move right. Do your best to dodge!')
screen.onkey(key='space', fun=stop_mining)

while mining:
    jump_left_animation()
    time.sleep(0.6)
    user.shape('miner_left.gif')
    screen.listen()

camera_confused_animation()
time.sleep(1.8)
screen.onkeypress(key='d', fun=right)
screen.onkeypress(key='a', fun=left)
screen.onkey(key='w', fun=jump)
screen.listen()
set_bullet()
set_bullet2()
bullet_move()
bullet_check()
hit_check()
screen.mainloop()
screen.exitonclick()