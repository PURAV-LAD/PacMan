import turtle
pen = turtle.Turtle()
turtle.Screen().bgcolor('BLACK') # BACKGROUND

pen.up()

pen.fillcolor('YELLOW') #PAC-MAN
pen.begin_fill()
pen.setpos(150 , -100)
pen.down()
pen.left(60)
pen.circle(200 , -300)
pen.up()
pen.end_fill()

pen.setpos(150 , -100) #MOUTH
pen.down()
pen.left(26)
pen.forward(180)
pen.right(112)
pen.forward(180)
pen.up()

pen.fillcolor('BLACK') # EYE
pen.begin_fill()
pen.setpos(20 , 90)
pen.down()
pen.circle(20 , 360)
pen.end_fill()
pen.up()

pen.fillcolor('RED') # CHERRY
pen.begin_fill()
pen.setpos(200 , -45)
pen.down()
pen.circle(50 , 360)
pen.end_fill()
pen.up()

pen.fillcolor('SEAGREEN')
pen.begin_fill()
pen.setpos(185 , 25)
pen.down()
pen.circle(7 , 360)
pen.end_fill()

pen.fillcolor('DARKOLIVEGREEN')
pen.begin_fill()
pen.setpos(185 , 25)
pen.down()
pen.circle(5 , 360)
pen.end_fill()
pen.up()

pen.fillcolor('OLIVEDRAB') # LEAF
pen.begin_fill()
pen.setpos(180 , 30)
pen.down()
pen.circle(30 , 80)
pen.end_fill()

pen.hideturtle()
