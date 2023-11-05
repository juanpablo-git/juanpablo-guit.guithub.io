import turtle
import random

atualiza =  True
direction = "left"

window = turtle.Screen()
window.bgcolor("green")
window.title("Space Invaders")
turtle.bgpic("background.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
setposition = border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")


player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -200)

numbers_of_invaders = 10
invaders = []

for i in range(numbers_of_invaders):
    invaders.append(turtle.Turtle())

for enemy in invaders:
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    pos_x = random.randint(-200, 200)
    pos_y = random.randint(100, 250)
    enemy.setposition(pos_x, pos_y)


enemy.hideturtle()

def create_fire(x):
    fire = turtle.Turtle(visible=False)
    fire.color("yellow")
    fire.shape("triangle")
    fire.penup()
    fire.speed(0)
    fire.setheading(90)
    fire.shapesize(0.5, 0.5)
    fire.setposition(x, -185)   
    fire.showturtle()
    return fire 

fire = turtle.Turtle()
fire.color("yellow")
fire.shape("triangle")
fire.penup()
fire.speed(0)
fire.setheading(90)
fire.shapesize(0.5, 0.5)
fire.setposition(0, -185)


firespeed = 15
playerspeed = 15
fire_on = False

def atualiza_invazor(interval = -1):
    global  atualiza
    global direction
    frame_atual = 0
    positions = []


    for pos_invaders in invaders:
        position = pos_invaders.xcor()
        positions.append(position)

    left_pos = min(positions)
    right_pos = max(positions)

    left_index = positions.index(left_pos)
    right_index = positions.index(right_pos)

    speedinvaders = 10
    
    
    if interval > frame_atual:
        frame_atual += 1
    elif frame_atual == 1:
        atualiza = False

    while atualiza: 
        if frame_atual == 1:
            atualiza = False
        if direction == "left":
            
            x_left = invaders[left_index].xcor()
            if x_left >= -280:
                for pos_invaders in invaders:
                    position = pos_invaders.xcor()
                    position -= speedinvaders
                    pos_invaders.setx(position)

                x_left -= speedinvaders

            else:
                for pos_invaders in invaders:
                    position = pos_invaders.ycor()
                    position -= 20
                    pos_invaders.sety(position)
                direction = "right"

        elif direction == "right":
            
            x_right = invaders[right_index].xcor()
            if x_right < 280:
                for pos_invaders in invaders:
                    position = pos_invaders.xcor()
                    position += speedinvaders
                    pos_invaders.setx(position)

                x_right += speedinvaders
            else:
                for pos_invaders in invaders:
                    position = pos_invaders.ycor()
                    position -= 20
                    pos_invaders.sety(position)
                direction = "left"


def move_fire():
    global atualiza 
    global fire_on
    atualiza_fire = True
    atualiza = False
    if not fire_on:
        fire_on = True
 
        fire_atual = create_fire(player.xcor())
        
        while  atualiza_fire:
            for pos_invaders in invaders:
                fire_atual_x = fire_atual.xcor()
                fire_atual_y = fire_atual.ycor()
                print(fire_atual_y,"-",pos_invaders.ycor(),"//",abs(abs(fire_atual_y) - abs(pos_invaders.ycor())))
                if (abs(fire_atual_x - pos_invaders.xcor()) in [1,2,3,4,5,6,7,8,9,10] or fire_atual_x  == pos_invaders.xcor() ) and (abs(fire_atual_y - pos_invaders.ycor()) in [1,2,3,4,5,6,7,8,9,10] or fire_atual_y  == pos_invaders.ycor() ):
                    pos_invaders.hideturtle()
                    print("morreu")
                # if abs(fire_atual_y - pos_invaders.ycor()) in [1,2,3,4,5,6,7,8,9,10] or fire_atual_y  == pos_invaders.ycor() :
                #     pos_invaders.hideturtle()
                #     print("morreu")

               

            
                    
            atualiza = False
            if(fire_atual.ycor()  >= 300):
                atualiza_fire = False            
            fire_atual.sety(fire_atual.ycor() +15)

           


                   
            atualiza = True
            atualiza_invazor(1)
        atualiza = True
        fire_atual.hideturtle()
        fire_on = False
    # global fire_on
    # global atualiza
    # atualiza = False
    # fire_on = True
    # y = fire.ycor()
    # while y < 300:
    #     y += firespeed
    #     fire.sety(y)
    #     atualiza = True
    #     atualiza_invazor(1)
    #     atualiza = False
    # atualiza = True

    # fire.hideturtle()
    # fire.sety(-185)
    # fire_on = False
    # fire.setx(player.xcor())
    # fire.showturtle()


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    # if not fire_on:
    fire.setx(x)


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    # if not fire_on:
    fire.setx(x)


turtle.listen()
turtle.onkey(move_fire,"space")
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")

atualiza_invazor()


turtle.mainloop()


# asyncio.run(atualiza_invazor())

# positions = []


# for pos_invaders in invaders:
#     position = pos_invaders.xcor()
#     positions.append(position)

# left_pos = min(positions)
# right_pos = max(positions)

# left_index = positions.index(left_pos)
# right_index = positions.index(right_pos)

# speedinvaders = 10
# direction = "left"
# while True: 
#     if direction == "left":
#         x_left = invaders[left_index].xcor()
#         if x_left >= -280:
#             for pos_invaders in invaders:
#                 position = pos_invaders.xcor()
#                 position -= speedinvaders
#                 pos_invaders.setx(position)

#             x_left -= speedinvaders

#         else:
#             direction = "right"

#     elif direction == "right":
#         x_right = invaders[right_index].xcor()
#         if x_right < 280:
#             for pos_invaders in invaders:
#                 position = pos_invaders.xcor()
#                 position += speedinvaders
#                 pos_invaders.setx(position)

#             x_right += speedinvaders
#         else:
#             direction = "left"



turtle.done()

