import turtle
import random
import time

s = turtle.Screen()  # create a screen,set the size
s.setup(width=660, height=740)
s.tracer(0)          # make the screen still
g_t = turtle.Turtle()
g_t.hideturtle()
# set the default
g_direction, last_direction = 'Pause', ''
g_game_start, g_finish = False, False
g_click_time, g_contract, g_time, g_pause_or_not = 0, 0, 0, 1
list_body, random_numbers, g_dir, body_list = [], [], [], []
vaild_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# create a list to restore the snake's body
for i in range(50):
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.shape('square')
    turt.color('blue', 'black')
    turt.up()
    body_list.append(turt)


def square(length, easer):  # a function to draw a square
    angle = 90
    easer.color('white', 'white')
    easer.seth(0)
    easer.begin_fill()
    for i in range(4):
        easer.forward(length)
        easer.left(angle)
    easer.end_fill()


def print_outline():  # a funciton to draw the outline of the program
    global desci
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.up()
    pen.setpos(-250, 210)
    pen.down()
    pen.goto(250, 210)
    pen.up()
    pen.goto(0, 0)
    pen.shape('square')
    pen.shapesize(29, 25)
    pen.color('black', '')
    pen.showturtle()
    desci = turtle.Turtle()
    desci.hideturtle()
    desci.up()
    desci.goto(-200, 60)
    desci.down()
    desci.write("Welcome to Zhao Zhiyuan's version of snake\n\nYou are going to use the 4 arrow keys to move the snake\naround the screen, trying to consume all the food items\nbefore the monster catches you.\n\nClick anywhere on the screen to start the game, have fun!!", font=('Times New Roman', 12))
    s.update()


def d_status():   # draw the state bar
    global g_t
    g_t.clear()
    g_t.hideturtle()
    g_t.up()
    g_t.goto(-200, 240)
    g_t.down()
    g_t.write('Contact: %d    Time: %d    Motion: %s' %
              (g_contract, g_time, g_direction), font=('Times New Roman', 18))
    s.update()


def r_numbers():  # create the random food
    global random_numbers
    while True:
        random_numbers = []
        for number in range(1, 10):  # make the food distribute randomly
            random_numbers.append(
                (random.randint(0, 24)*20-240, random.randint(0, 24)*20-290))
        number_distances = []
        random_numbers.append((0, -40))
        for j in range(len(random_numbers)):  # check if two food is the close
            for k in range(j+1, len(random_numbers)):
                number_distance = (random_numbers[j][0]-random_numbers[k][0])**2+(
                    random_numbers[j][1]-random_numbers[k][1])**2
                number_distances.append(number_distance)
        number_distances.sort()
        if number_distances[0] < 800:  # find out the closest distance
            continue
        break
    printer = turtle.Turtle()
    printer.up()
    printer.hideturtle()
    # print the number at the position of food subsquently.
    for number in range(1, 10):
        x, y = random_numbers[number-1][0], random_numbers[number-1][1]
        printer.setpos(x, y)
        printer.write(number, align="center", font=12)
        s.update()
        time.sleep(0.5)


def timer():  # the function to account time
    global g_time
    if not catch() and not g_finish:
        g_time += 1
        d_status()
        s.ontimer(timer, 1000)

# four functions to control the direction of the snake


def onKeyLeft():
    global g_direction, last_direction
    g_direction = 'Left'
    if g_pause_or_not == -1:  # if the snake is pause, restart the snake
        last_direction = 'Left'
        pause()


def onKeyRight():
    global g_direction, last_direction
    g_direction = 'Right'
    if g_pause_or_not == -1:  # if the snake is pause, restart the snake
        last_direction = 'Right'
        pause()


def onKeyUp():
    global g_direction,  last_direction
    g_direction = 'Up'
    if g_pause_or_not == -1:  # if the snake is pause, restart the snake
        last_direction = 'Up'
        pause()


def onKeyDown():
    global g_direction,  last_direction
    g_direction = 'Down'
    if g_pause_or_not == -1:  # if the snake is pause, restart the snake
        last_direction = 'Down'
        pause()


def click(a, b):  # a function to act after the click
    global desci, g_click_time, monster, g_head, g_game_start
    g_click_time += 1
    if g_click_time == 1:
        g_game_start = True
        g_dir.insert(0, g_head)
        desci.reset()
        desci.hideturtle()
        r_numbers()
        timer()    # make the game start
        monster_move()
        move_one_step()


def pause():  # the funciton the pause the snake
    global g_pause_or_not, g_direction, last_direction
    if g_click_time > 0:  # make sure the game has started
        g_pause_or_not = (-1)*g_pause_or_not  # change the value every press
        if g_pause_or_not == -1:
            last_direction = g_direction
            g_direction = 'Pause'
            d_status()
        if g_pause_or_not == 1:
            g_direction = last_direction
            monster_move()
            move_one_step()
            d_status()


def head():
    global g_head   # Creating the head of snake
    g_head = turtle.Turtle()
    g_head.shape("square")       # Snake Head Shape
    g_head.color("red")        # Snake Head Colour
    g_head.penup()
    g_head.setpos(0, -40)
    s.update()


def body(n):
    global g_dir, easer,body_list
    if n != 0 and n in vaild_number:
        for i in range(n):  # append n turtle to the turtle list
            body_list[0].setpos(g_head.xcor(), g_head.ycor())
            body_list[0].showturtle()
            g_dir.append(body_list[0])
            del body_list[0]
        vaild_number.remove(n)  # make the food unavailble
        x, y = random_numbers[n-1][0], random_numbers[n-1][1]
        easer = turtle.Turtle()
        easer.hideturtle()
        easer.up()
        easer.goto(x-9.5, y)
        square(19, easer)  # use the square funtion to make the food unvisble
        return True
    else:
        return False


def body_start():  # create a inital body
    global g_head, g_dir
    for i in range(5):  # initally the body len is 5
        body_list[0].setpos(0, -40)
        body_list[0].showturtle()
        g_dir.append(body_list[0])
        del body_list[0]


def monster_show():  # a function to show the monster
    global monster
    monster = turtle.Turtle()
    monster.up()
    monster.shape('square')
    monster.color('purple')
    while True:  # check the distance between monster and the snake
        x, y = random.randint(0, 24)*20-240, random.randint(0, 24)*20-280
        if x**2+(y+40)**2 < 16000:  # make the monster far from the snake
            continue
        break
    monster.setpos(x, y)
    s.update()


def eat():  # a funciton to check whether the food is eaten or not
    distance_list = []
    for i in random_numbers:
        distance = (g_head.xcor()-i[0])**2 + (g_head.ycor()-i[1]-10)**2
        distance_list.append(distance)
    if sorted(distance_list)[0] < 200:
        # return the number of food
        return distance_list.index(sorted(distance_list)[0])+1
    else:
        return 0


def move_one_step():  # make the snake move one step
    global g_dir, g_head, g_contract,  g_finish
    # check whether the snake needs to move
    if g_game_start and not catch() and g_pause_or_not == 1 and not g_finish:
        body(eat())  # check the food is eaten or not
        if (g_dir[-1].xcor(), g_dir[-1].ycor()) == \
                (g_dir[-2].xcor(), g_dir[-2].ycor()):  # judge whether the snake slows down
            slow_down = True
        else:
            slow_down = False
        # receive the direction
        s.onkey(onKeyLeft, 'Left')
        s.onkey(onKeyRight, 'Right')
        s.onkey(onKeyUp, 'Up')
        s.onkey(onKeyDown, 'Down')
        s.onkey(pause, 'space')
        a = list(range(1, len(g_dir)))
        a.reverse()
        if can_move_one_step():  # judge whether the snake can move
            for i in a:  # every body move to the postion of the turtle in front of it
                x, y = g_dir[i-1].xcor(), g_dir[i-1].ycor()
                g_dir[i].up()
                g_dir[i].goto(x, y)
            x, y = round(g_head.xcor()), round(g_head.ycor())
            if g_direction == 'Up':
                g_head.sety(y + 20.0)
            if g_direction == 'Down':
                g_head.sety(y - 20.0)
            if g_direction == 'Left':
                g_head.setx(x - 20.0)
            if g_direction == 'Right':
                g_head.setx(x + 20.0)
        # if the snake eat all the food are strecth its body
        if len(vaild_number) == 0 and not slow_down:
            g_head.stamp()
            g_head.hideturtle()
            g_head.setpos(x+20.0, y+20.0)  # write the winner
            g_head.write('Winner!', font=('Times New Roman', 12))
            g_finish = True
            s.update()
            return None  # the player wins
        d_status()
        if slow_down:  # set the time of move time
            s.ontimer(move_one_step, 400)
        else:
            s.ontimer(move_one_step, 200)
    elif not catch():
        return None


def can_move_one_step():  # check the snake can move or not
    if g_direction == 'Up':
        y = g_head.ycor()
        if y + 20 > 200:
            return False
        else:
            return True
    if g_direction == 'Down':
        y = g_head.ycor()
        if y - 20 < -280:
            return False
        else:
            return True
    if g_direction == 'Left':
        x = g_head.xcor()
        if x - 20 < -240:
            return False
        else:
            return True
    if g_direction == 'Right':
        x = g_head.xcor()
        if x + 20 > 240:
            return False
        else:
            return True


def monster_move():  # a function the make the monster move
    global monster, g_head, g_dir, g_contract, g_finish
    angle = monster.towards(g_head)  # find the best path to meet snake
    to = round(angle/90)
    if to == 0 or to == 4:
        monster.seth(0)
    if to == 1:
        monster.seth(90)
    if to == 2:
        monster.seth(180)
    if to == 3:
        monster.seth(270)
    monster.forward(20.0)
    s.update()
    # check whether the monster touch the snake
    body_pos = []
    for i in range(1, len(g_dir)):
        x, y = round(g_dir[i].xcor()), round(g_dir[i].ycor())
        body_pos.append((x, y))
    x, y = round(monster.xcor()), round(monster.ycor())
    if (x, y) in body_pos:  # the monster touch the snake
        g_contract += 1
        d_status()
    # check whether the snake is slow down
    if (g_dir[-1].xcor(), g_dir[-1].ycor()) == \
            (g_dir[-2].xcor(), g_dir[-2].ycor()):
        slow_down = True
    else:
        slow_down = False
    if catch() and (len(vaild_number) != 0 or slow_down):  # the monster catch the snake
        time.sleep(0.4)
        x, y = g_dir[0].xcor(), g_dir[0].ycor()
        monster.setpos(x, y)
        writer = turtle.Turtle()
        writer.up()
        writer.color('purple')
        writer.hideturtle()
        writer.setpos(x+20, y+20)  # write game over
        writer.write('Game over!!', font=('Times New Roman', 12))
        g_finish = True
        s.update()
        return None
    elif len(vaild_number) == 0 and not slow_down:  # if the player win end the program
        return None
    else:  # contine the game
        refresh_time = int(5000/random.randint(10, 20)
                           )  # set the time randomly
        s.ontimer(monster_move, refresh_time)


def catch():  # the function to judge whether the monster catch the snake
    distance_2 = (g_head.xcor()-monster.xcor())**2 + \
        (g_head.ycor()-monster.ycor())**2
    while True:
        if distance_2 <= 400:  # if monster and snake are too close
            return True
        else:
            return False


# make the program work
s.listen()
print_outline()
d_status()
body_start()
head()
monster_show()
s.onclick(click)
s.onkey(pause, 'space')

input()
