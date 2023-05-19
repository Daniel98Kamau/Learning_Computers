#Import all necessary libraries.
from OpenGL.GL import * #This format allows use of modules/functions
from OpenGL.GLU import * # without use of the dot notation.
from OpenGL.GLUT import *
import sys   #provides some housekeeping tools to create the graphics display. 

#Draw a wireteapot of the specified size
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    #glutWireTeapot(1)
    glutSolidTeapot(0.5)
    glFlush()

glutInit(sys.argv) #Displaying GLUT style graphics.
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) #using a single display screen (buffer) and the RGB (red, green, blue) color scheme.
glutInitWindowSize(800, 600)
glutInitWindowPosition(100,100)
glutCreateWindow("Teapot") #Sets title of display window
glutDisplayFunc(draw) #tells GLUT where to find the function that creates the graphics scene.
glutMainLoop() #Starts the program

