import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

Vertices = ((0,0,0), (4,0,0), (4,4,0), (0,4,0),
            (0,4,4), (0,0,4),(4,0,4), (4,4,4))
Edges = ((0,1), (0,3), (0,5), (2,1), (2,3), (2,7),
         (4,3), (4,5), (4,7), (6,1), (6,5), (6,7))

def Cube():
    glBegin(GL_LINES)
    for edge in Edges:
        for vertex in edge:
            glVertex3fv(Vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, 800/600, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(5)

main()
