import turtle
import time
import random

delay = 0.1
score = 0
start_time = time.time()
game_duration = 45  # seconds

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("lightgreen")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food (apple)
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-280, 260)
pen.write("Score: 0", align="left", font=("Arial", 16, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Main game loop
while True:
    win.update()

    # End game after 45 seconds
    elapsed = time.time() - start_time
    if elapsed > game_duration:
        pen.goto(0, 0)
        pen.write(f"Time up! Final Score: {score}", align="center", font=("Arial", 20, "bold"))
        break

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        pen.goto(0, 0)
        pen.write("Game Over!", align="center", font=("Arial", 20, "bold"))
        break

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 250)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        pen.clear()
        pen.goto(-280, 260)
        pen.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            pen.goto(0, 0)
            pen.write("Game Over!", align="center", font=("Arial", 20, "bold"))
            win.update()
            time.sleep(2)
            win.bye()
            quit()

    time.sleep(delay)

win.mainloop()
