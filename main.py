import turtle
import random
import time

#Window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("DUELITY")

floor = -380
roof = 380

#Border
border_draw = turtle.Turtle()
border_draw.color("white")
border_draw.speed(0)
border_draw.penup()
border_draw.setposition(-400, -400)
border_draw.pendown()
border_draw.pensize(3)
for side in range(4):
    border_draw.fd(800)
    border_draw.lt(90)
border_draw.hideturtle()

#healthbars
health_a = 5
health_b = 5

health_a_draw = turtle.Turtle()
health_a_draw.speed(0)
health_a_draw.color("purple")
health_a_draw.penup()
health_a_draw.setposition(-370, -380)
healthstring_a = "Health: %s" %health_a
health_a_draw.write(healthstring_a, False, align="left", font=("Gothic", 14, "normal"))
health_a_draw.hideturtle()

health_b_draw = turtle.Turtle()
health_b_draw.speed(0)
health_b_draw.color("purple")
health_b_draw.penup()
health_b_draw.setposition(-370, 370)
healthstring_b = "Health: %s" %health_b
health_b_draw.write(healthstring_b, False, align="left", font=("Gothic", 14, "normal"))
health_b_draw.hideturtle()

#Player A
player_a = turtle.Turtle()
player_a.shape("circle")
player_a.color("white")
player_a.speed(0)
player_a.penup()
player_a.setposition(0, -350)

#Player B
player_b = turtle.Turtle()
player_b.shape("circle")
player_b.color("white")
player_b.speed(0)
player_b.penup()
player_b.setposition(0, 350)

#Playerspeed
playerspeed = 15

#Bullets
bulletstate_a = "ready"
bulletstate_b = "ready"

bullet_a = turtle.Turtle()
bullet_a.color("red")
bullet_a.shape("square")
bullet_a.penup()
bullet_a.speed(0)
bullet_a.shapesize(0.5, 0.5)
bullet_a.hideturtle()

bullet_b = turtle.Turtle()
bullet_b.color("green")
bullet_b.shape("square")
bullet_b.penup()

bullet_b.speed(0)
bullet_b.shapesize(0.5, 0.5)
bullet_b.hideturtle()

bulletspeed = 20

#Player movement
def player_a_moveleft():
    x = player_a.xcor()
    x -= playerspeed
    if x < -380:
        x = -380
    player_a.setx(x)

def player_a_moveright():
    x = player_a.xcor()
    x += playerspeed
    if x > 380:
        x = 380
    player_a.setx(x)

def player_b_moveleft():
    x = player_b.xcor()
    x -= playerspeed
    if x < -380:
        x = -380
    player_b.setx(x)

def player_b_moveright():
    x = player_b.xcor()
    x += playerspeed
    if x > 380:
        x = 380
    player_b.setx(x)

#Bullet movement
def fire_bullet_a():
    global bulletstate_a
    if bulletstate_a == "ready":
        bulletstate_a = "fire"
        x = player_a.xcor()
        y = player_a.ycor() + 15
        bullet_a.setposition(x, y)
        bullet_a.showturtle()

def fire_bullet_b():
    global bulletstate_b
    if bulletstate_b == "ready":
        bulletstate_b = "fire"
        x = player_b.xcor()
        y = player_b.ycor() - 15
        bullet_b.setposition(x, y)
        bullet_b.showturtle()

def isCollision(p, pb):
    distance = p.distance(pb)
    if distance < 15:
        return True
    else:
        return False

#keybinds
wn.listen()
wn.onkeypress(player_a_moveleft, "a")
wn.onkeypress(player_a_moveright, "d")
wn.onkeypress(player_b_moveleft, "Left")
wn.onkeypress(player_b_moveright, "Right")
wn.onkey(fire_bullet_a, "space")
wn.onkey(fire_bullet_b, "0")

start_time = time.time()
#Main Loop
while True:
    wn.update()
    if bulletstate_a == "ready":
        bullet_a.goto(-800, -800)

    if bulletstate_b == "ready":
        bullet_b.goto(-1000, 1000)

    if bulletstate_a == "fire":
        y = bullet_a.ycor()
        y += bulletspeed
        bullet_a.sety(y)

    if bullet_a.ycor() > roof:
        bullet_a.hideturtle()
        bulletstate_a = "ready"

    if bulletstate_b == "fire":
        y = bullet_b.ycor()
        y -= bulletspeed
        bullet_b.sety(y)

    if bullet_b.ycor() < floor:
        bullet_b.hideturtle()
        bulletstate_b = "ready"

    #collisions
    if isCollision(player_a, bullet_b):
        bullet_b.hideturtle()
        bulletstate_b = "ready"
        health_a -= 1
        healthstring_a = "Health: %s" %health_a
        health_a_draw.clear()
        health_a_draw.write(healthstring_a, False, align="left", font=("Gothic", 14, "normal"))
        if health_a == 0:
            endA = turtle.Turtle()
            endA.color("white")
            endA.speed(0)
            endA.write("PLAYER B WINS!", False, align="center", font=("Gothic", 30, "bold"))
            endA.hideturtle()
            break

    if isCollision(player_b, bullet_a):
        bullet_a.hideturtle()
        bulletstate_a = "ready"
        health_b -= 1
        healthstring_b = "Health: %s" %health_b
        health_b_draw.clear()
        health_b_draw.write(healthstring_b, False, align="left", font=("Gothic", 14, "normal"))
        if health_b == 0:
            endB = turtle.Turtle()
            endB.color("white")
            endB.speed(0)
            endB.write("PLAYER A WINS!", False, align="center", font=("Gothic", 30, "bold"))
            endB.hideturtle()
            break

    if isCollision(bullet_a, bullet_b):
        bullet_b.hideturtle()
        bullet_a.hideturtle()
        bulletstate_a = "ready"
        bulletstate_b = "ready"
        
turtle.mainloop()



