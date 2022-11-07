# Writing Initials With Turtle Graphics.
# 11-07-2022
# CTI-110 P4LAB1a-Shapes
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

# Pickup red pen.
# Move pen towards chosen spot.
# Place pen down on chose spot.
# Drawa a red square.
# Pick up pen.
#
#
# Pickup purple pen.
# Place pen down on chosen spot
# Draw upside down triangle in purple.
# Pick up pen.
##---------------------------------------------------------------
# This program draws a square with a red and an upside down triangle in purple.



import turtle
wn = turtle.Screen()
raphael = turtle.Turtle()
raphael.color("red")
raphael.pensize(8)

donatello = turtle.Turtle()
donatello.color("purple")
donatello.pensize(8)

raphael.penup()
raphael.backward(160)
raphael.pendown()

for i in range(4):
    raphael.forward(100)
    raphael.right(90)
    donatello.forward(100)
    donatello.right(120)

donatello.penup()



wn.mainloop()
