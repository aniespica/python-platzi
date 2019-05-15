import turtle


window = turtle.Screen()
tortuga = turtle.Turtle()
line = 0
while line < 4:
	tortuga.forward(100)
	tortuga.right(90)
	line += 1
window.mainloop()
