import turtle
import time
import random

WIDTH=500
HEIGHT=500
COLORS=["red","green","blue","orange","yellow","pink","grey","purple","brown","black"]


def get_number_of_racers(): 
    while True: 
        racers=int(input("Введите количество черепах для гонки от 2 до 10: "))
        if racers < 2 or racers > 10:
            print("Количество черепах должно быть от 2 до 10")
        else:
            print("Количество черепах одобрено: ")
            return racers

        
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Гонки Черепах")
    time.sleep(5)


def create_turtles(colors):
    racers=[]
    spacing=WIDTH//(len(colors)+1)
    for index, color in enumerate(colors):
        t = turtle.Turtle()
        t.color(color)
        t.left(90)
        t.shape("turtle")
        t.penup()
        t.setpos(-WIDTH//2+(index+1)*spacing, -HEIGHT//2+20)
        t.pendown()
        racers.append(t)
    return racers


def race(colors):
    racers=create_turtles(colors)
    while True:
        for racer in racers:
            distance=random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y >=HEIGHT//2-10:
                return f"Победила черепаха {colors[racers.index(racer)]}"

            
def main():
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors=COLORS[:racers]
    print(race(colors))
    time.sleep(3)


if __name__ == '__main__':
    main()

    