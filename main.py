import pygame

pygame.init()

altura = 600
largura = 600
display = pygame.display.set_mode( (largura,altura) )
fps = pygame.time.Clock()
background = pygame.image.load("venv/fundo21.jpg")
mario = pygame.image.load("venv/mario1.png")
mario = pygame.transform.scale(mario, (120, 120))
cascov = pygame.image.load("venv/cascoverde.png")
cascov = pygame.transform.scale(cascov, (80, 80))


preto = (0,0,0)
branco = (255,255,255)
marioposicaox = largura * 0.40
marioposicaoy= altura * 0.8
movimentx = 0

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentx = -10
            elif evento.key == pygame.K_RIGHT:
                movimentx = 10
        if evento.type == pygame.KEYUP:
            movimentx = 0


        display.fill(branco)
        display.blit(background,[0,0])

        marioposicaox = marioposicaox + movimentx
        if marioposicaox < 0 :
            marioposicaox = 0
        elif marioposicaox > 480:
            marioposicaox = 480
        display.blit(mario, (marioposicaox,marioposicaoy))

        display.blit(cascov, (100,300,))

        pygame.display.update()
        fps.tick(60)

