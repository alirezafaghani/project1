#packages
import turtle
import time
import random




delay = 0.1
score = 0



wn = turtle.Screen()
wn.title("alireza's game ")
wn.bgcolor('blue')
wn.setup(width=600, height=600)
wn.tracer(0)

#creating the head object

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('yellow')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#creating the apple object

apple = turtle.Turtle()
apple.speed(0)
apple.shape('circle')
apple.color('red')
apple.penup()
apple.goto(0,100)

# segments
segments = []

# Move 
def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'



# Function to Move the Snake
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)




# bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_right, 'd')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_down, 's')




while True:
    wn.update()

    # if colision happens between border and the snake
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments
        segments.clear()
        score = 0
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x,y)


    # check if any colision happend between the food and the snake
    if head.distance(apple) < 20:
        # Move the food to a random location
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x,y)

        # add segments to snake

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)
        score = score+10
        print(score)


    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move the segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)




    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments
            segments.clear()
            score = 0
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            food.goto(x,y)

    time.sleep(delay)



    



wn.mainloop()