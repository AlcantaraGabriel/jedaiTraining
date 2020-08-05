import pygame
import time

#iniciando pygame
pygame.init()
#criando tela, setando legenda, carregando icone e colocando na tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("JedaiTraining")
icon = pygame.image.load('g851.png')
pygame.display.set_icon(icon)


playerImg1 = pygame.image.load('g852.png')
playerImg2 = pygame.image.load('g853.png')
playerImg3 = pygame.image.load('covid.png')




playerX = 10
playerY = 460

playerBadX = 490
playerBadY = 460

background = pygame.image.load("rect10.png")



def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



def playerBad():
    screen.blit(playerImg3, (playerBadX,playerBadX))


def pulo():


def tiro():

        
running = True
at = 0
angle = 0
playerBad()
while running:
    
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if(at==0):
        screen.blit(playerImg2, (playerX,playerY))
        at = 1
    else:
        screen.blit(playerImg1, (playerX,playerY))
        at = 0

    rotated_image = pygame.transform.rotate(playerImg3,angle)
    screen.blit(rotated_image,(playerBadX,playerBadY))
    angle= angle+1
    
    pygame.display.update()
    
    
    
