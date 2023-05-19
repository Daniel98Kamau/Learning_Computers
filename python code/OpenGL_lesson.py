#Import all necessary libraries.
from OpenGL.GL import * #This format allows use of modules/functions
from OpenGL.GLU import * # without use of the dot notation.
from OpenGL.GLUT import *
import sys   #provides some housekeeping tools to create the graphics display. 

#Draw a teapot of the specified size
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    #glutWireTeapot(1) #Wire teapot
    glutSolidTeapot(0.5) #Solid teapot
    glFlush()

glutInit(sys.argv) #Displaying GLUT style graphics.
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) #using a single display screen (buffer) and the RGB (red, green, blue) color scheme.
glutInitWindowSize(800, 600)
glutInitWindowPosition(100,100)
glutCreateWindow("Teapot") #Sets title of display window
glutDisplayFunc(draw) #tells GLUT where to find the function that creates the graphics scene.
#glutMainLoop() #Starts the program


def init(): #Initialises the plotting process
    glClearColor(1.0, 0.0, 1.0 , 1.0) #sets background color(R,G,B,A)
    gluOrtho2D(-8.0, 8.0, -8.0, 8.0) #sets origin at the centre of the window

#Drawing a point at the centre of window
def plot_point():
    glClear(GL_COLOR_BUFFER_BIT) #Clears the sreen, sets background colour
    glColor3f(1.0, 1.0, 1.0) #sets color of plotting pen
    glPointSize(10.0) #sets the size of the point
    glBegin(GL_POINTS)
    glVertex2f(0, 0) #Sets position of point to be drawn
    glVertex2f(4,0)
    glVertex2f(-3,-3)
    glVertex2f(2,-4)

    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Central Point")
    glutDisplayFunc(plot_point)
    init()
    glutMainLoop()

main()
