import turtle as t

t.bgcolor("black")
t.pencolor("yellow")
t.speed(0)

def shape (angle,side,lim):
    rev_dir = 200
    t.forward(side)

    if side % (rev_dir*2) == 0:
        angle = angle +2
    t.right(angle)
    side = side + 2
    if side < lim:
        shape(angle,side,lim)

angle = 119
side = 0
lim = 600
shape(angle,side,lim)
t.done()