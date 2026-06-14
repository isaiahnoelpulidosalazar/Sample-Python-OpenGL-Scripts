# pip install pygame PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Textured Cube")
image = pygame.image.load('texture.png')
data = pygame.image.tostring(image, 'RGBA', 1)
texID = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texID)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glEnable(GL_TEXTURE_2D)
glEnable(GL_DEPTH_TEST)
gluPerspective(25, (display[0]/display[1]), 0.1, 50)
glTranslate(0, 0, -10)

vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
]

tex_coords = [
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
]


def draw_square():
    glBegin(GL_TRIANGLES)
    for triangle in [[0, 1, 2], [2, 3, 0]]:
        for vertex in triangle:
            glTexCoord2fv(tex_coords[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_cube():
    glPushMatrix()
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    draw_square()
    glPopMatrix()
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    draw_square()
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