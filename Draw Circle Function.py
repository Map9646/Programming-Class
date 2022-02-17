import turtle

t = turtle.Turtle()

t.speed(0)


def draw_circle(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    
    for i in range(360):
      t.forward(1)
      t.rt(1)
      t.circle(radius)#Don't do. Will make 100 circles in a circle Cool, but not what you want for penguins head, would be cool for a sun though
    
    t.end_fill()
    
    
draw_circle(t, 100, "Yellow")
  
