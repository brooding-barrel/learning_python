# https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Chaos_game
# https://py2.codeskulptor.org/#user49_f6v83pKnVQ_10.py
import simplegui
import random as r
WIDTH=400
HEIGHT=400

points = [(0, HEIGHT), (WIDTH/2, 0), (WIDTH, HEIGHT)]
rpoints=[]
dot_radius=1
dot_line_width=1
dot_outline_color="red"
dot_fill_color="red"
num_points=1000
# number of milliseconds between each new point
new_point_interval=3

def random_point_in_tri():
    """
    Gets a random y point - the whole frame is valid
    Then finds a random point inside the two triangle edges
    """
    ry=r.randrange(HEIGHT)
    xmin=(ry/2)
    xmax=WIDTH-(ry/2)
    rx=r.randrange(xmin,xmax)
    return [rx, HEIGHT - ry]

def random_tri_point():
    """
    returns a random point in the original triangle
    """
    return r.choice(points)

def half_distance(p1, p2):
    """
    returns a point that is halfway between p1 and p2
    """
    hy = (p2[1]-p1[1])/2
    hx = (p2[0]-p1[0])/2
    return [p1[0]+hx, p1[1]+hy]
    
# Handler to draw on canvas
def draw(canvas):
    for p in rpoints:
        canvas.draw_circle(p, dot_radius, dot_line_width, dot_outline_color, dot_fill_color)

def new_point_handler():
    global num_points
    global p
    if num_points > 0:
        hp = half_distance(p, random_tri_point())
        p = hp
        rpoints.append(hp)
    else:
        draw_new_point_timer.stop()
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Title", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
p = random_point_in_tri()
draw_new_point_timer = simplegui.create_timer(new_point_interval, new_point_handler)
draw_new_point_timer.start()

# Start the frame animation
frame.start()

