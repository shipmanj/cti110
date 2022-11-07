# Writing Initials With Turtle Graphics.
# 11-07-2022
# CTI-110 P4LAB1b-Initials
# JC Shipman
#
#------------------------------------------------------------------
#Psuedo Code

# Pickup blue pen.
# Move pen towards chosen spot.
# Place pen down on chose spot.
# Draw first initial of first name.
#
# Pick up orange pen.
# Move pen to next chosen spot.
# Place pen down on chosen spot
# Draw first initial of last name.
# Pick up pen.
##---------------------------------------------------------------
# This program draws the initials of my first name in blue and my last name with a orange.


import turtle
wn = turtle.Screen()

jsb = turtle.Turtle()
jsb.color("blue")
jsb.pensize(6)

jso = turtle.Turtle()
jso.color("orange")
jso.pensize(6)

jsb.penup()
jsb.backward(140)
jsb.pendown()


jsb.forward(60)
jsb.penup()
jsb.backward(30)
jsb.pendown()
jsb.right(90)
jsb.forward(100)
jsb.right(90)
jsb.forward(30)
jsb.right(90)
jsb.forward(40)
jsb.penup()


#raphael.forward(60)
#raphael.right(90)
#raphael.forward(180)
#raphael.right(180)
#raphael.pendown()


jso.penup()
jso.forward(60)
jso.pendown()
jso.backward(60)
jso.right(90)
jso.forward(50)
jso.left(90)
jso.forward(60)
jso.right(90)
jso.forward(50)
jso.right(90)
jso.forward(60)
jso.penup()

wn.mainloop()
