import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # Ask the user for the radius in pixels and store it in a variable
    radius=simpledialog.askinteger(title='i hate titles',prompt='what is the radius?')
    #Make a new
    # turtle draw a circle with the correct radius
    # my_turtle.circle()
    idiot=turtle.Turtle()
    # Call the turtle .penup() method
    idiot.circle(radius=radius, extent=360,steps=10000)
    # Move your turtle to a new x,y position using .goto()
    idiot.penup()
    idiot.goto(0,0)
    # Calculate the area of your circle and store it in a variable
    area=math.pi*radius*radius
    # Hint, you can use math.pi
    
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    idiot.write(arg="area =" + str(area), move=True, align='left', font=('Arial',8,'normal'))
    # Hide your turtle
    idiot.hideturtle()
    turtle.done()
   # Call turtle.done() ok yeah
