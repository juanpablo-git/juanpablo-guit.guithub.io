import turtle
import random

class jogo():
    jogo_runing = True
    score = 0
    numbers_of_invaders = 11
    invaders = []
    firespeed = 40
    playerspeed = 15
    fire_on = False
    x_fire = 0
    y_fire = 0
    fire = turtle.Turtle()
    player = turtle.Turtle()
    direction = "left"
    speedinvaders = 15
    inviders_loop = True
    score_pen = turtle.Turtle()
    def generate_fire(self):
        self.fire.color("yellow")
        self.fire.shape("triangle")
        self.fire.penup()
        self.fire.speed(0)
        self.fire.setheading(90)
        self.fire.shapesize(0.5, 0.5)
        self.fire.setposition(0, -185)
        self.fire.showturtle()
        return self.fire
    def generate_player(self):
        turtle.register_shape("player.gif")
        self.player.shape("player.gif")
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0, -200)
        self.player.showturtle()
        return self.player
    def index(self):
        self.fire.hideturtle()
        self.score_pen.hideturtle()
        self.player.hideturtle()
        turtle.register_shape("invader.gif")
        turtle.register_shape("reload.gif")

        window = turtle.Screen()
        window.bgcolor("green")
        window.title("Space Invaders")
        turtle.bgpic("background.gif")


        border_pen = turtle.Turtle()
        border_pen.speed(0)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-300, -300)
        border_pen.pendown()
        border_pen.pensize(3)
        border_pen.hideturtle()

        for side in range(4):
            border_pen.fd(600)
            border_pen.lt(90)

        border_pen.hideturtle()
        self.generate_inviders()
        self.generate_fire()
        self.generate_player()


        # Set the score to 0
        score = 0

        # Draw the pen
        self.score_pen = turtle.Turtle()
        self.score_pen.speed(0)
        self.score_pen.color("red")
        self.score_pen.penup()
        self.score_pen.setposition(-290, 270)
        scorestring = "SCORE: %s" % score
        self.score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        self.score_pen.hideturtle()

        turtle.listen()
        turtle.onkey(lambda : self.move_fire(self.fire), "space")
        turtle.onkey(self.move_right, "Right")
        turtle.onkey(lambda  : self.move_left(self.player,self.fire), "Left")

        self.move_inimigos()

        
        turtle.done()


    def refresh(self):
        invaders = self.invaders
        left_index, right_index, down_index = self.init_pos()
        y = self.invaders[left_index].ycor()
        if self.direction == "left":
            x_left = invaders[left_index].xcor()

            if x_left >= -280:
                for pos_invaders in self.invaders:
                    position = pos_invaders.xcor()
                    position -= self.speedinvaders
                    pos_invaders.setx(position)
                x_left -= self.speedinvaders
            else:
                y -= 40
                self.direction = "right"
                for pos_invaders in self.invaders:
                    position = pos_invaders.ycor()
                    position -= 40
                    pos_invaders.sety(position)

        elif self.direction == "right":
            x_right = invaders[right_index].xcor()
            if x_right < 280:
                for pos_invaders in self.invaders:
                    position = pos_invaders.xcor()
                    position += self.speedinvaders
                    pos_invaders.setx(position)
                x_right += self.speedinvaders
            else:
                y -= 40
                direction = "left"
                for pos_invaders in self.invaders:
                    position = pos_invaders.ycor()
                    position -= 40
                    pos_invaders.sety(position)
    def write(self,x,y,text):
        game_over = turtle.Turtle()
        game_over.speed(0)
        game_over.color("red")
        game_over.penup()
        game_over.setposition(x, y)
        game_over.write(text, False, align="center", font=("Arial", 30, "normal"))
        game_over.hideturtle()
        return game_over
    def move_inimigos (self):
        # global left_index, right_index, down_index,direction,invaders
        invaders = self.invaders
        inviders_loop = self.inviders_loop
        direction = self.direction
        while self.inviders_loop:
            left_index, right_index, down_index = self.init_pos()
            y = invaders[left_index].ycor()
            if direction == "left":
                x_left = invaders[left_index].xcor()
                if x_left >= -280:
                    for pos_invaders in invaders:
                        position = pos_invaders.xcor()
                        position -= self.speedinvaders
                        pos_invaders.setx(position)
                        if (pos_invaders.xcor() - self.player.xcor() <= 20) and (pos_invaders.ycor() - self.player.ycor() <= 20):
                            self.game_breack()
                            self.inviders_loop = False
                            break
                    x_left -= self.speedinvaders
                else:
                    y -= 40
                    direction = "right"
                    for pos_invaders in invaders:
                        position = pos_invaders.ycor()
                        position -= 40
                        pos_invaders.sety(position)

            elif direction == "right":
                x_right = invaders[right_index].xcor()
                if x_right < 280:
                    for pos_invaders in invaders:
                        position = pos_invaders.xcor()
                        position += self.speedinvaders
                        pos_invaders.setx(position)
                    x_right += self.speedinvaders
                else:
                    y -= 40
                    direction = "left"
                    for pos_invaders in invaders:
                        position = pos_invaders.ycor()
                        position -= 40
                        pos_invaders.sety(position)

            y_down = invaders[down_index].ycor()
            if y_down <= -280:
                self.game_breack()
                self.inviders_loop = False
                break
    def move_fire(self,fire):
        # global fire_on, x_fire, y_fire,score,jogo_runing
        if self.fire_on == False and self.jogo_runing:
            self.fire_on = True
            y_fire =fire.ycor()
            x_fire = fire.xcor()
            while y_fire < 300:
                for inimigo in self.invaders:
                    x_ini = inimigo.xcor()
                    y_ini = inimigo.ycor()
                   
                    if x_fire >= x_ini -20 and x_fire <= x_ini + 20:
                        if y_fire >= y_ini:
                            global left_index, right_index, down_index
                            inimigo.setx(random.randint(-280, 280))
                            inimigo.sety(random.randint(100, 250))
                            y_fire = 400
                            left_index, right_index, down_index = self.init_pos()
                            self.score_pen.clear()
                            self.score+=1
                            self.score_pen.write("Score: "+str(self.score), False, align="left", font=("Arial", 14, "normal"))
                            break
                y_fire += self.firespeed
                fire.sety(y_fire)
                # self.refresh()

            fire.hideturtle()
            fire.sety(-185)
            fire.setx(self.player.xcor())
            fire.showturtle()
            self.fire_on = False
    def generate_inviders(self):
        numbers_of_invaders = self.numbers_of_invaders 
        invaders = self.invaders

        for i in range(numbers_of_invaders):
            invaders.append(turtle.Turtle())

        for enemy in self.invaders:
            enemy.shape("invader.gif")
            enemy.penup()
            enemy.speed(0)
            pos_x = random.randint(-200, 200)
            pos_y = random.randint(100, 250)
            enemy.setposition(pos_x, pos_y)
    def move_right(self):
        x = self.player.xcor()
        x += self.playerspeed
        if x > 280:
            x = 280
        self.player.setx(x)
        if not self.fire_on:
             self.fire.setx(x)
    def move_left(self,player,fire):
        x = player.xcor()
        x -= self.playerspeed
        if x < -280:
            x = -280
        player.setx(x)
        if not self.fire_on:
            fire.setx(x)
        print(fire.xcor())
    def init_pos(self):
        x_positions = []
        y_positions = []
        for pos_invaders in self.invaders:
            x_position = pos_invaders.xcor()
            y_position = pos_invaders.ycor()
            x_positions.append(x_position)
            y_positions.append(y_position)

        left_pos = min(x_positions)
        right_pos = max(x_positions)

        down_pos = min(y_positions)

        left_id = x_positions.index(left_pos)
        right_id = x_positions.index(right_pos)
        down_id = y_positions.index(down_pos)

        return left_id, right_id, down_id
    def game_breack(self):
        self.jogo_runing = False
        self.score = 0
        self.inviders_loop = False
        game_over = turtle.Turtle()
        game_over.speed(0)
        game_over.color("red")
        game_over.penup()
        game_over.setposition(0, 0)
        game_over.write("Game Over", False, align="center", font=("Arial", 30, "normal"))
        game_over.hideturtle()
        reload = self.write(0,100,"")
        reload.showturtle()
        reload.shape("reload.gif")
        def reload_game(x,y):
             
            self.inviders_loop = True
            self.jogo_runing = True
            for enemy in self.invaders:
                enemy.shape("invader.gif")
                enemy.penup()
                enemy.speed(0)
                pos_x = random.randint(-200, 200)
                pos_y = random.randint(100, 250)
                enemy.setposition(pos_x, pos_y)
            reload.clear()
            reload.hideturtle()
            game_over.clear()
            self.move_inimigos()
        reload.onclick(reload_game)


j = jogo()
j.index()