import pygame

# pygame setup
pygame.display.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = 30  # tamanho do quadrado
player_speed = 5  # velocidade do movimento

player_pos2 = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == quit:
            running = False

    # Obter as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Atualizar a posição do jogador com base nas teclas pressionadas
    player_pos.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    player_pos.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    player_pos2.x += (keys[pygame.K_d] - keys[pygame.K_a]) * player_speed
    player_pos2.y += (keys[pygame.K_s] - keys[pygame.K_w]) * player_speed

    # Tema de fundo
    screen.fill("black")

    # Desenhar o quadrado na tela
    pygame.draw.rect(screen, (255, 0, 0), (player_pos.x,
                     player_pos.y, player_size, player_size))

    pygame.draw.rect(screen, (255, 255, 255), (player_pos2.x,
                     player_pos2.y, player_size, player_size))

    # Atualizar a tela
    pygame.display.flip()

    # Definir a taxa de quadros por segundo
    clock.tick(60)

pygame.display.quit()
