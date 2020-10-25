import pygame
import time
from playsound import playsound

#iniciando pygame
pygame.init()

#criando tela, setando legenda, carregando icone e colocando na tela
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("rect10.png")
pygame.display.set_caption("JedaiTraining")
icon = pygame.image.load('g851.png')
pygame.display.set_icon(icon)

font  = pygame.font.Font('Arial.ttf',20)

def showAtenMed():
    valores = font.render("Valor Meditação: \nValor Atenção: ",True,(255,255,255))
    screen.blit(valores,(20,20))

class P_cariribot:
    def __init__(self):
        self.p_X = None
        self.p_Y = None
        self.playerImg = None
        self.at = 0

    def setImg(self,s):
        self.playerImg = pygame.image.load(s)

    def setX(x):
        self.p_X = x
    def setX(y):
        self.p_Y = y
            

    def setDisplay(self):
        screen.blit(self.playerImg, (self.p_X,self.p_Y))

    def moviment(self):
        if(self.at):
            self.at = 0
        else:
            self.at = 1
            
    def som(self): 
        pygame.mixer.music.load('infectado.ogg')
        pygame.mixer.music.play(1)

    def som2(self): 
        pygame.mixer.music.load('eliminado.ogg')
        pygame.mixer.music.play(1)

class P_covid:
    def __init__(self):
        self.p_X = 490
        self.p_Y = 460
        self.playerImg = None
        self.angle = 0

    def setImg(self,s):
        self.playerImg = pygame.image.load(s)


    def setDisplay(self):
        screen.blit(self.playerImg, (self.p_X,self.p_Y))

    def rotat(self):
        rotated_image = pygame.transform.rotate(self.playerImg,self.angle)
        screen.blit(rotated_image,(self.p_X,self.p_Y))
        self.p_X -=1
        self.angle= self.angle+1
        
    def resetPos(self):
        self.p_X = 490
        self.p_Y = 465

class proteCovid:
    def __init__(self):
        self.p_X = None
        self.p_Y = None
        self.velocity = None
        self.obejectImg = None
        
    def setImg(self,s):
        self.obejectImg = pygame.image.load(s)

    def setDisplay(self):
        screen.blit(self.obejectImg, (self.p_X,self.p_Y))

    def resetPos(self):
        self.p_X = 10
        self.p_Y = 460

    def som(self): 
        pygame.mixer.music.load('fire.ogg')
        pygame.mixer.music.play(1)
       
        
#playerImg1 = pygame.image.load('g852.png')
#playerImg2 = pygame.image.load('g853.png')
#playerImg3 = pygame.image.load('covid.png')


    
condicao = True
at = 0

caririBot =  P_cariribot()
caririBot.p_X = 10
caririBot.p_Y = 460
caririBot.setImg('g852.png')

covid19 = P_covid()
covid19.p_X = 490
covid19.p_Y = 465
covid19.setImg('covid3d.png')

alcool = proteCovid()
alcool.p_X = 10
alcool.p_Y = 460
alcool.setImg('gel2.png')
alcool.setDisplay()

while condicao:
    
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                alcool.som()
                alcool.velocity = 0
    if(caririBot.at==0):
        caririBot.setImg('g853.png')
        caririBot.moviment()
    else:
        caririBot.setImg('g852.png')
        caririBot.moviment()

    if(alcool.velocity==0):
        
        if(alcool.p_Y >= covid19.p_Y and alcool.p_Y <= covid19.p_Y+55 and alcool.p_X >= covid19.p_X and alcool.p_X <= covid19.p_X+55):
            alcool.velocity = None
            caririBot.som2()
            alcool.resetPos()
            covid19.resetPos()
        elif(alcool.p_Y+58 >= covid19.p_Y and alcool.p_Y+58 <= covid19.p_Y+55 and alcool.p_X+91 >= covid19.p_X and alcool.p_X+91 <= covid19.p_X+55): 
            alcool.velocity = None
            caririBot.som2()
            alcool.resetPos()
            covid19.resetPos()
        else:
            alcool.setDisplay()
            alcool.p_X +=2
            
    if(covid19.p_X<=caririBot.p_X+5):
        caririBot.som()
        covid19.resetPos()
            
            
    caririBot.setDisplay()
    covid19.setDisplay()
    covid19.rotat()
    showAtenMed()
    pygame.display.update()
    
    
    

