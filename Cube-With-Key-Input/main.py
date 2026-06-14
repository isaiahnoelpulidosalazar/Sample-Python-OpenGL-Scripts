import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

press = 0
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("04 Lab 1")
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0]/display[1]), 0.1, 50)
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
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 1]
]

def draw_cube():
    glBegin(GL_TRIANGLES)
    for square in squares:
        glColor3fv(colors[squares.index(square)])
        for triangle in square:
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