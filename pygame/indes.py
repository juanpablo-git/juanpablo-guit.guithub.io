import pygame
import random
pygame.init()
x =[410,340,410,450]
y = [400,300,200,100]
cars = [pygame.image.load("car.png"),pygame.image.load("green_car.png"),pygame.image.load("orange_car.png"),pygame.image.load("blcack_car.png")]

road = pygame.image.load("road .jpg")

janela = pygame.display.set_mode((800,800))
pygame.display.set_caption("Criando jogo")

janela_aberta = True
while  janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_DOWN]:
        y[0] = y[0] + 10
    if comandos[pygame.K_LEFT]:
        # y = y + 10
        x[0] = x[0] - 10
    if comandos[pygame.K_RIGHT]:
        x[0] = x[0] + 10
    if comandos[pygame.K_UP]:
        y[0] = y[0] - 10        
    janela.blit(road,(0,0))

    janela.blit(cars[0],(x[0],y[0]))
    janela.blit(cars[1],(x[1],y[1]))
    janela.blit(cars[2],(x[2],y[2]))
    # janela.blit(cars[3],(x[3],y[3]))
    y[2] += 10
    y[1] +=10
    y[3] +=10
    if(y[1] >= 700):
        y[1] = random.randint(0,700)
    if y[2] >= 700:
        y[2] = random.randint(0,700)
    if y[3] >= 700:
        y[3] = random.randint(0,700)    
    pygame.display.update()
pygame.quit()