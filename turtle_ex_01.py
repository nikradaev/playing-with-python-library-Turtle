import turtle 
from turtle import *
import random
from random import *

#get cursor to default - center position
turtle.home()

#colors 
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

#background
turtle.bgcolor('black')

#loop for 100 iterations
for x in range(100):

	#random color
	turtle.color(colors[randint(0, 5)])
	
	#randomly go in any direction X, Y - randomly, within 600 pixels
	turtle.goto(randint(-300, 300), randint(-300, 300))
		
	#draw a circle with random radius 0-50pxls
	turtle.circle(randint(0, 50))

print('Horray!')
turtle.done()