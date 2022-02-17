import turtle

t = turtle.Turtle()

t.speed(0)



def draw_rectangle(t, side1, side2, side3, side4, color):
    t.fillcolor(color)
    t.begin_fill()
    
    for i in range(4):
        t.forward(100)
        t.rt(90)
        t.forward(side2)
        t.rt(90)
        t.forward(side4)
        
    t.end_fill()
    
    return
    
        
        
draw_rectangle(t, 50, 100, 50, 100, "blue")