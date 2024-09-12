import turtle

def circle_face(x,y,radius,fill_color): #depend on these parameters, once you reach the mouth add an angle parameter.
  turtle.speed(10) #0 is the fastest speed, where you could choose the speed from 1-10.
  turtle.hideturtle() #In order to hide the cursor while drawing the picture you want to create.
  turtle.penup()
  turtle.goto(x,y-radius)
  turtle.pendown()
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()

def nose(x,y,radius,fill_color):
   turtle.penup()
   turtle.goto(x,y-radius)
   turtle.pendown()
   turtle.fillcolor(fill_color)
   turtle.begin_fill()
   turtle.circle(radius)
   turtle.end_fill()

def eye1(x,y,radius,fill_color):
   turtle.tracer(False) #Turtle.tracer process is the code that cancels the animation of the function where you start with turtle.tracer(False) then end up with Turtle.Tracer(True) in order to cancel the animation of the function. (Must include False then True).
   turtle.penup()
   turtle.goto(x,y-radius)
   turtle.pendown()
   turtle.fillcolor(fill_color) #Choosing the color that you want.
   turtle.begin_fill()
   turtle.circle(radius)
   turtle.end_fill()
   turtle.tracer(True) #Turtle.tracer process is the code that cancels the animation of the function where you start with turtle.tracer(False) then end up with Turtle.Tracer(True) in order to cancel the animation of the function. (Must include False then True).

def eye2(x,y,radius,fill_color):
   turtle.tracer(False)
   turtle.penup()
   turtle.goto(x,y-radius)
   turtle.pendown()
   turtle.fillcolor(fill_color)
   turtle.begin_fill()
   turtle.circle(radius)
   turtle.end_fill()
   turtle.tracer(True)

def mouth(x,y,radius,fill_color,angle): #When making the mouth, you should create an angle for the setheading after goto.
   turtle.penup()
   turtle.goto(x,y-radius) #y-radius: This moves the turtle down by the length of the radius so that it starts drawing from the bottom of the circle. The turtle works its way counterclockwise around the circle.
   turtle.setheading(angle)
   turtle.pendown()
   turtle.fillcolor(fill_color)
   turtle.begin_fill()
   turtle.circle(150,120) #(Size of the semi-circle , 120 *stable* *half a circle in a 120 degree*)
   turtle.end_fill()
      
def main(): #Organizing the order of the callouts to draw the parts in order.
   circle_face(0,0,200,"yellow")
   nose(0,0,25,"pink")
   eye1(-90,100,50,"white") #(x-cordinate,y-cordinate,control size of the circle,color type)
   eye1(-90,100,22,"Blue")
   eye1(-90,100,15,"Black")
   eye2(90,100,50,"White")
   eye2(90,100,22,"Blue")
   eye2(90,100,12,"Black")
   mouth(-130,-10,45,"black",-60) #(control right to left,y-coordinate,control where the semi circle goes up or down)
   input("Press Enter to exit:")


main()

