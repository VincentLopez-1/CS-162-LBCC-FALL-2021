#! usr/bin/env python3
"""" This program will take inputted number of sides and output a picture of a polygon with the corresponding number of sides

Step 1: Ask user to input an interger for n and a color range for f.
Step 2: imports turtle, then runs it through for conditions.
step 3: Displays the corresponding polygon drawn by a turtle filled in with the color range of f.

"""
import turtle
yurtle = turtle.Turtle()
yurtle = turtle.getscreen()


print( "Hello! Given the number of sides and color of fill, this program will draw a polygon for you")
n=int(input("Please enter a number of sides for the polygon:")) # Prompts user to input a number of sides for the polygon
print("Please enter a value between 0.0 and 1.0 for each color range:") 

r=float(input("Range for Red?:"))
g=float(input("Range for Green?:"))
b=float(input("Range for Blue?:")) # This and above prompts the user to input a float number between 0.0 and 1.0

if 0<=r<=1 and 0<=g<=1 and 0<=b<=1: # Runs a if statement that checks if all the values inputted are between the range of 0.0 and 1
    turtle.begin_fill() 
    turtle.fillcolor(r,g,b) # Begins filling the drawn polygon wwith the color range the user used
else:
    print("Sorry, I cannot process numbers more than 1 or less then 0; The polygon will be drawn, but without a fill color. Please press ENTER:") # When the staemnt is not true r,g, or b are not between the range; the program will tell the user the error then halt until the user presses a key
    input() # THe program will still provide the polygon but not filled
for poly in range(n): # Runs a for loop for the range of the number of sides
    turtle.down()
    turtle.forward(100)
    turtle.left(360/n) # 360 degrees is the total sum of outer angles of a regular polygon
    turtle.up()
turtle.end_fill() #Ceases the fill of the polygon

turtle.mainloop() # Halts the program and holds the screen