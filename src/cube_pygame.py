import pygame
from math import *

CYAN = "#00ffff"
COLORS=["#ff0000","#00ff00","#0000ff","#ffff00","#00aaff","#ff00ff"]

WIDTH, HEIGHT = 300,300
pygame.display.set_caption("cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 50

circle_pos = [150,150]

angle = 0

points=[[[-1],[-1],[1]],
        [[1],[-1],[1]],
        [[1],[1],[1]],
        [[-1],[1],[1]],
        [[-1],[-1],[-1]],
        [[1],[-1],[-1]],
        [[1],[1],[-1]],
        [[-1],[1],[-1]]]

projection=[[1,0,0],
            [0,1,0],
            [0,0,0]]

def multiply(A,B):
    result=[]
    for i in range(len(A)):
        result+=[[0]*len(B[0])]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def draw_plane(l,color):
    light=[[0],[0],[1]]
    if multiply(l[4],light)[0][0]>=0:
        temp=l[0:4]
        pygame.draw.polygon(screen,color,temp,width=0)

planes= [
        [[(-1,-1,1)],[(1,-1,1)],[(1,1,1)],[(-1,1,1)],[(0,0,1)]],
        [[(1,1,1)],[(-1,1,1)],[(-1,1,-1)],[(1,1,-1)],[(0,1,0)]],
        [[(-1,1,1)],[(-1,-1,1)],[(-1,-1,-1)],[(-1,1,-1)],[(-1,0,0)]],
        [[(-1,-1,1)],[(1,-1,1)],[(1,-1,-1)],[(-1,-1,-1)],[(0,-1,0)]],
        [[(1,-1,1)],[(1,1,1)],[(1,1,-1)],[(1,-1,-1)],[(1,0,0)]],
        [[(1,-1,-1)],[(1,1,-1)],[(-1,1,-1)],[(-1,-1,-1)],[(0,0,-1)]]
        ]

clock = pygame.time.Clock()
while True:
    surfaces =[
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
            ]

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    xrotation=[[1,0,0],
               [0,cos(angle),(-1)*sin(angle)],
               [0,sin(angle),cos(angle)]]

    yrotation=[[cos(angle),0,sin(angle)],
               [0,1,0],
               [(-1)*sin(angle),0,cos(angle)]]

    zrotation=[[cos(angle),-sin(angle),0],
               [sin(angle),cos(angle),0],
               [0,0,1]]
    angle+=0.008

    screen.fill(CYAN)

    m=0
    for i in planes:
        n=0
        for j in i:
            rotated3d=multiply(j,zrotation)
            rotated3d=multiply(rotated3d,yrotation)
            rotated3d=multiply(rotated3d,xrotation)

            if n!=4:
                projected3d=multiply(rotated3d,projection)

                x1=int(projected3d[0][0]*scale) + circle_pos[0]
                y1=int(projected3d[0][1]*scale) + circle_pos[1]

                surfaces[m][n] = [x1,y1]

            else:
                surfaces[m][n]=rotated3d

            n=n+1
        m=m+1

    for i in range(len(planes)):
        col=COLORS[i]
        draw_plane(surfaces[i],col)

    pygame.display.update()
