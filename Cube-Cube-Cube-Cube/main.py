# pip install pygame PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

press = 0
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("05 Lab 1")
glEnable(GL_BLEND)
glDepthMask(GL_FALSE)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
gluPerspective(25, (display[0]/display[1]), 0.1, 50)
glTranslate(0, 0, -10)

vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
]

squares = [
    [[0, 1, 2], [2, 3, 0]],
    [[4, 5, 6], [6, 7, 4]],
    [[0, 4, 7], [7, 3, 0]],
    [[1, 5, 6], [6, 2, 1]],
    [[3, 2, 6], [6, 7, 3]],
    [[0, 1, 5], [5, 4, 0]]
]

colors = [
    # [1, 0, 1],
    # [0, 1, 1],
    [0, 1, 0]
    # [1, 0, 0],
    # [1, 1, 0],
    # [0, 0, 1]
]


def draw_cube():
    for a in range(5):
        glPushMatrix()
        glScalef(0.25 * a, 0.25 * a, 0.25 * a)
        glBegin(GL_TRIANGLES)
        for square in squares:
            # glColor3fv(colors[squares.index(square)])
            glColor4f(0, 1 , 0, 0.25)
            for triangle in square:
                for vertex in triangle:
                    glVertex3fv(vertices[vertex])
        glEnd()
        glPopMatrix()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glRotatef(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(15)