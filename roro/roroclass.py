import turtle

class roro_class():
    def draw_art(self,lncolor,bgcolor,speed):
        window = turtle.Screen()
        window.setup(width=1200,height=500,startx=None,starty=None)
        window.bgcolor(bgcolor)
        window.title("RoRo - My lovely kitty!")
        roro = turtle.Turtle()

        roro.color(lncolor)
        roro.shape("turtle")
        roro.pensize(10)
        roro.speed(speed)

        roro.penup()
        roro.setpos(-500,-200)
        roro.pendown()
        roro.left(90)
        roro.forward(400)
        roro.right(90)
        roro.forward(100)
        roro.circle(-100,180)
        roro.left(120)
        roro.forward(230)

        roro.penup()
        roro.left(60)
        roro.forward(50)
        roro.left(90)
        roro.forward(100)

        roro.pendown()
        roro.forward(200)
        roro.circle(-100,180)
        roro.forward(200)
        roro.circle(-100,180)

        roro.penup()
        roro.right(180)
        roro.forward(100)
        roro.left(90)
        roro.forward(250)

        roro.pendown()
        roro.left(90)
        roro.forward(400)
        roro.right(90)
        roro.forward(100)
        roro.circle(-100,180)
        roro.left(120)
        roro.forward(230)

        roro.penup()
        roro.left(60)
        roro.forward(50)
        roro.left(90)
        roro.forward(100)

        roro.pendown()
        roro.forward(200)
        roro.circle(-100,180)
        roro.forward(200)
        roro.circle(-100,180)

        window.exitonclick()
