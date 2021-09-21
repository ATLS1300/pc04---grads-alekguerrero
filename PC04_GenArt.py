"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: A. Guerrero

********* HEY, READ THIS FIRST **********

The code below depicts a spooky, silly skeleton. It uses multiple parametric patterns 
including a heart shape repurposed to look like a skeleton rib cage, an ellipse for the head,
and a spiral that is somewhat reminiscent of a spider web. I used the random function to have
the turtle display a color of it's choosing in most of the shapes. When looking at this it
should evoke feelings of fear, yet whimsy.

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 800 # width of panel
h = 800 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

# Adding a background image
image = "cemetery_background_2.gif" #creating a variable for image
panel.bgcolor(255,255,255) #black
panel.bgpic(image) #importing the image

#Define the variables to use
skeletonCoordinates = [(0,20),(-16,20),(16,20),(-13,20),(13,20)]
halloweenColors = [(255,196,12), (93, 63, 211), (247,95,28), (255,154,0), (169,169,169), (136,30,228), (133,226,31), (0,154,23)]
boneColor = (227,218,201)

#Second turtle for the first body
tSB = turtle.Turtle() #tS1 = turtleSkeletonBase
tSB.hideturtle()
tSB.pensize(4)
tSB.color(boneColor)
tSB.speed(10)
tSB.up()
tSB.goto(skeletonCoordinates[0])
tSB.down()

#Modified from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns
ANGLES = range(0,180) #changed the angle range to (0,180) in order to stop it at the bottom

for angle in ANGLES:
    angle = math.radians(angle)
    X = 600*(1/7*math.sin(2*angle)*(1 + math.cos(80*angle))*(1-1/12*(math.sin(2*angle))**15)) #changed formula: narrow body, different lines
    Y = 600*(-1/2*(2*angle/math.pi - 1)**2 + 1/4*math.sin(2*angle)*(math.sin(80*angle)**11)) #changed formula: narrow body, different lines
    tSB.goto(X,Y)

#Third turtle for the neck
tN = turtle.Turtle() #tN = turtleNeck
tN.hideturtle()
tN.pensize(4)
tN.color(boneColor)
tN.speed(10)
tN.up()
tN.goto(skeletonCoordinates[1])
tN.down()
tN.lt(90)
tN.fd(80)
tN.up()
tN.goto(skeletonCoordinates[2])
tN.down()
tN.fd(80)

#Fourth turtle for the head
tH = turtle.Turtle()
tH.hideturtle()
tH.pensize(4)
tH.pencolor(boneColor)
tH.fillcolor(random.choice(halloweenColors)) #used the random function to display a random fill for the head
tH.speed(12)
tH.up()
tH.goto(0,180)
tH.down()

tH.begin_fill()
radX1 = 6 #defining the x axis radius
radY1 = 10 #defining the y axis radius as larger
scale = 8 #size of the ellipse

ANGLES = range(0,360) #defines the possible angles to use
for angle in ANGLES:
    angle = math.radians(angle)        

angle = range(0,360) #defines the angles for the turtle to go
for angle in ANGLES:
    
    angle = math.radians(angle) #converts to radians
    Y = scale * math.sin(angle) * radY1 #ties Y to sin to make ellipse longer on y-axis
    X = scale * math.cos(angle) * radX1 #ties X to cosine
    tH.goto(X,Y+180) #shifted the Y-axis to move it up; code borrowed from https://math.libretexts.org/Bookshelves/Calculus/Book%3A_Calculus_(Apex)/09%3A_Curves_in_the_Plane/9.02%3A_Parametric_Equations
tH.end_fill()

#First turtle for the random head spiral
tSP = turtle.Turtle() #tSP = turtleSpiral
tSP.hideturtle()
tSP.speed(12)
tSP.color(random.choice(halloweenColors)) #used random function to pick a color spiral
tSP.pensize(2)
tSP.up()
tSP.goto(0,180)
tSP.down()
for i in range(90): # shape idea borrowed from PC03 pseudocode seliskarjack (https://drive.google.com/drive/folders/1TOcGo8msaZ1wEbiz75ABsVrHypVciL5w but modified to be a spiral instead of multiple polygons)
    tSP.forward(0.5+i)
    tSP.right(50)
    
#Fifth turtle for the second neck
tNR = turtle.Turtle() #tN = turtleNeckRandom
tNR.hideturtle()
tNR.pensize(3)
tNR.color(random.choice(halloweenColors)) #used random to pick a color for second neck
tNR.speed(10)
tNR.up()
tNR.goto(skeletonCoordinates[3])
tNR.down()
tNR.lt(90)
tNR.fd(80)
tNR.up()
tNR.goto(skeletonCoordinates[4])
tNR.down()
tNR.fd(80)

#Sixth turtle for the second body
tSR = turtle.Turtle() #tS = turtleSkeletonRandom
tSR.hideturtle()
tSR.pensize(2)
tSR.color(random.choice(halloweenColors)) #used random to overlay another body in a randowm halloween themed color from list above
tSR.speed(10)
tSR.up()
tSR.goto(skeletonCoordinates[0])
tSR.down()

#Modified from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns
ANGLES = range(0,180) #changed the angle range to (0,180) in order to stop it at the bottom

for angle in ANGLES:
    angle = math.radians(angle)
    X = 600*(1/7*math.sin(2*angle)*(1 + math.cos(80*angle))*(1-1/12*(math.sin(2*angle))**19)) #changed formula: narrow body, different lines
    Y = 600*(-1/2*(2*angle/math.pi - 1)**2 + 1/4*math.sin(2*angle)*(math.sin(80*angle)**13)) #changed formula: narrow body, different lines
    tSR.goto(X,Y)

# =================== CLEAN UP =========================
turtle.done()
