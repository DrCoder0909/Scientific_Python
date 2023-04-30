import matplotlib.pyplot as plt
import matplotlib.animation as animation

g =9.81
XMAX =5
cor = 0.65
dt =0.005
x0, y0 = 0,4
vx0, vy0 = 1,0

def get_pos(t=0):
    """ A generator yielding the balls position at time t"""
    x , y, vx, vy = x0, y0, vx0, vy0
    while x<XMAX:
        t +=dt
        x+= vx0*dt
        y+= vy*dt
        vy -= g*dt
        if y<0:
            y=0
            vy = -vy*cor
        yield x,y

def init():
    """Initialize the animation figure"""
    ax.set_xlim(0,XMAX)
    ax.set_ylim(0,y0)
    ax.set_xlabel("$x$/m")
    ax.set_ylabel("$y$/m")
    line.set_data(xdata, ydata)
    ball.set_center((x0,y0))
    height_text.set_text(f"Height: {y0:.1f}m")
    return line, ball, height_text

def animate(pos):
    """for each frame advance the animation to a new position, pos"""
    x,y =pos
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata,ydata)
    ball.set_center((x,y))
    height_text.set_text(f"Height:{y:.1f}m")
    return line, ball,height_text

fig, ax = plt.subplots()
ax.set_aspect("equal")

line, = ax.plot([],[], lw= 2)
ball = plt.Circle((x0,y0), 0.08)
height_text = ax.text(XMAX*0.5, y0*0.8, f"Height:{y0:.1f}m")
ax.add_patch(ball)
xdata, ydata=[],[]

interval =1000*dt
ani = animation.FuncAnimation(fig, animate, get_pos, blit = True,
interval = interval,repeat =True, init_func = init)
plt.show()
