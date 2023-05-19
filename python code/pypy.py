from OpenGL.GLUT import *
from OpenGL.GL import*
from OpenGL.GLU import*
import sys

Vertices = ((0,0,0), (4,0,0), (4,4,0), (0,4,0),
            (0,4,4), (0,0,4),(4,0,4), (4,4,4))
Edges = ((0,1), (0,3), (0,5), (2,1), (2,3), (2,7),
         (4,3), (4,5), (4,7), (6,1), (6,5), (6,7))

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 5.0, -1.0, 5.0)

def Cube():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_LINES)
    for edge in Edges:
        for vertex in edge:
            glVertex3fv(Vertices[vertex])
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(800,800)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Cube")
    glutDisplayFunc(Cube)
    init()
    glutMainLoop()

main()