# pip install pygame PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

press = 0
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Sample Python OpenGL Diamond With Key Input")
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0]/display[1]), 0.1, 50)
glTranslate(0, 0, -10)

vertices = [
    [0, 1, 0],
    [1, 0, 0],
    [0, -1, 0],
    [-1, 0, 0],
    [0, 0, 1],
    [0, 0, -1]
]

squares =  [
    [0, 1, 4],
    [0, 4, 3],
    [0, 3, 5],
    [0, 5, 1],
    [2, 1, 4],
    [2, 4, 3],
    [2, 3, 5],
    [2, 5, 1]
]

colors = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]

def draw_cube():
    glBegin(GL_TRIANGLES)
    for triangle in squares:
        glColor3fv(colors[squares.index(triangle)])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                glTranslatef(0, 1, 0)
                press += 1
            if event.key == pygame.K_a:
                glTranslatef(-1, 0, 0)
                press += 1
            if event.key == pygame.K_s:
                glTranslatef(0, -1, 0)
                press += 1
            if event.key == pygame.K_d:
                glTranslatef(1, 0, 0)
                press += 1
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if press < 4:
        glRotatef(1, 1, 0, 0)
    elif 4 <= press < 11:
        glRotatef(1, 0, 1, 0)
    else:
        glRotatef(1, 1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(15)