from turtle import * #Import all the exturtle functions
from math import cos, sin, pi
 
def star(turtle, x, y, points, R, r):
    """
    The function star will use turtle graphics to draw a star.
    """
 
    angle = 360 / points     # Create the correct angle for each point
    angletwo = 2 * angle
    
    penup(turtle)
    goto(turtle, x - R, y - R)
    pendown(turtle)
 
    for i in range(points):
        forward(turtle, R)   
        right(turtle, angle)
        forward(turtle, R)
        left(turtle, angletwo)
 
def ring(turtle, cx, cy, Nstars, radius, points, R, r):
    """
    The function ring will draw a ring of 'Nstars' with distance 'radius' from
    the centre, the points argument specifies how many points each star has and
    'R' and 'r' specify the inner and outer radii of each star.
    """
 
    # Create a blue box for the flag.
    width = radius * 5.0
    height = radius * 3.0
    color(turtle, "blue", "blue")
    begin_fill(turtle)
    penup(turtle)
    goto(turtle, cx - (width // 2), cy + (height // 2)) # Top Left
    goto(turtle, cx + (width // 2), cy + (height // 2)) # Top Right
    goto(turtle, cx + (width // 2), cy - (height // 2)) # Bottom Right
    goto(turtle, cx - (width // 2), cy - (height // 2)) # Bottom Left
    goto(turtle, cx - (width // 2), cy + (height // 2)) # Top Left
    pendown(turtle)
    end_fill(turtle)
 
    # Now draw each star in the flag.
    for i in range(Nstars):
        x = cx + radius * cos(2 * pi * i / Nstars)
        y = cy + radius * sin(2 * pi * i / Nstars)
        color(turtle, "yellow", "yellow")
        begin_fill(turtle)
        star(turtle, x, y, points, R, r)
        end_fill(turtle)
 
# Create a turtle
graham = Turtle()
 
# Put graham in turbo mode.
speed(graham, 'fastest')
 
# Get graham to draw a ring of 10 stars each with 5 points in a ring with radius
# 100. Each star should have an inner radius of 8 and an outer radius of 10.
ring(graham, cx=0, cy=0, Nstars=12, radius=100, points=5, R=8, r=10)
 
# Draw the 4 stars with different numbers of points.
color(graham, "black", "white")
star(graham, x=175,  y=-250, points=5, R=25, r=None)
star(graham, x=80,   y=-250, points=6, R=25, r=None)
star(graham, x=-35,  y=-250, points=7, R=25, r=None)
star(graham, x=-175, y=-250, points=8, R=25, r=None)
 
# Stops the program terminating immediately after drawing.
mainloop()
