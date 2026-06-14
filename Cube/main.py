import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Sample Python OpenGL - Cube")

gluPerspective(45, (display[0]/display[1]), 0.1, 50)
glTranslate(0, 0, -5)

def draw_cube():
    glBegin(GL_LINES)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glEnd()


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