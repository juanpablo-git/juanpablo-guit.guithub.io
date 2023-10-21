import pygame
pygame.init()
x = 400
y = 400
car = pygame.image.load("car.png")
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
        y = y + 10
    if comandos[pygame.K_LEFT]:
        # y = y + 10
        x = x - 10
    if comandos[pygame.K_RIGHT]:
        x = x + 10
    if comandos[pygame.K_UP]:
        y = y - 10        
    janela.blit(road,(0,0))

    janela.blit(car,(x,y))
    pygame.display.update()
pygame.quit()