# Demo 1
# Author: nmessa
# Date: 12/17/2015

from graphics import *

def main():
    win = GraphWin('Circle', 640, 480)
    shape = Circle(Point(200, 200), 30)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()

main()
