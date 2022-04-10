# https://py2.codeskulptor.org/#user49_3vIgNhoRWQ_6.py
import simplegui
import random

speed = 5.0
width = 400
height = 400
rcolors = ["white", "blue", "red", "yellow", "orange", "gray"]

points = []
vel = []
colors = []


# Handler to draw on canvas
def draw(canvas):
    for i in range(len(points)):
        points[i][0] += vel[i][0]
        points[i][1] += vel[i][1]
        points[i] = clamp_to_frame(points[i])
        canvas.draw_circle(points[i], 1, 1, colors[i], colors[i])
        
def clamp_to_frame(p):
    if ((p[0] < 0 or p[1] < 0) or (p[0] > width or p[1] > height)):
        return [width/2, height/2]
    return p

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.set_draw_handler(draw)

for i in range (100):
    p = [width/2,height/2]
    v = [random.random()*speed - speed / 2, random.random()*speed - speed / 2]
    points.append(p)
    vel.append(v)
    colors.append(random.choice(rcolors))
    
    
# Start the frame animation
frame.start()
]
