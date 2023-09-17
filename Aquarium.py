import pygame
import random


pygame.init()

Larg, Haut = 800, 600
FPS = 10 #vitesse de déplacement des objets

#Couleurs des objets


cyan = (0,255,255)

ecran = pygame.display.set_mode((Larg, Haut)) #Zone de l'écran exploitable par les objets
pygame.display.set_caption("Aquarium")


Poisson_chat = pygame.image.load("poisson1.png")
Poisson_chat_pos = Poisson_chat.get_rect() 
Poisson_chat_pos.centerx = Larg / 2
Poisson_chat_pos.centery = Haut / 2

Poisson_globe = pygame.image.load("poisson2.png")
Poisson_globe_pos = Poisson_globe.get_rect()
Poisson_globe_pos.centerx = random.randint(0, Larg - 130)
Poisson_globe_pos.centery = random.randint(0, Haut - 120)

Poisson_papi = pygame.image.load("poisson3.png")
Poisson_papi_pos = Poisson_papi.get_rect()
Poisson_papi_pos.centerx = random.randint(0, Larg - 130)
Poisson_papi_pos.centery = random.randint(0, Haut - 120)

speed = 2
clock = pygame.time.Clock()

#La boucle qui va définir les objets et leurs actions dans la zone exploitable

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    Poisson_chat_pos.x += random.randint(-speed, speed)
    Poisson_chat_pos.y += random.randint(-speed, speed)

    Poisson_globe_pos.x += random.randint(-speed, speed)
    Poisson_globe_pos.y += random.randint(-speed, speed)

    Poisson_papi_pos.x += random.randint(-speed, speed)
    Poisson_papi_pos.y += random.randint(-speed, speed)

    Poisson_chat_pos.x = max(0, min(Poisson_chat_pos.x, Larg - Poisson_chat_pos.width))
    Poisson_chat_pos.y = max(0, min(Poisson_chat_pos.y, Haut - Poisson_chat_pos.height))

    Poisson_globe_pos.x = max(0, min(Poisson_globe_pos.x, Larg - Poisson_globe_pos.width))
    Poisson_globe_pos.y = max(0, min(Poisson_globe_pos.y, Haut - Poisson_globe_pos.height))

    Poisson_papi_pos.x = max(0, min(Poisson_papi_pos.x, Larg - Poisson_papi_pos.width))
    Poisson_papi_pos.y = max(0, min(Poisson_papi_pos.y, Haut - Poisson_papi_pos.height))

    ecran.fill(cyan)
    ecran.blit(Poisson_chat, Poisson_chat_pos)
    ecran.blit(Poisson_globe, Poisson_globe_pos)
    ecran.blit(Poisson_papi, Poisson_papi_pos)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
