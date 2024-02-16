"""
Pygame - úvod
Instalace pygame: py -m pip install pygame

Pygame - modul pro Pythonu, který slouží k tvorbě her

"""

import pygame
pygame.init() #inicializace Pygame
screen = pygame.display.set_mode((800, 600)) #vytvoříme okno s výškou a šířkou
running = True #proměnná pro cyklus, abychom zjistili, zda stále běží program
clock = pygame.time.Clock() #hodiny pro nastavení obnovovací frekvence
player_x = 400
player_y = 300

while running: #nekonečný cyklus, který bude aktualizovat naše okno
    pressed = pygame.key.get_pressed() #funkce, která nám bere zmáčknutou klávesu
    if pressed[pygame.K_w]: #pohyb - zjistíme, zda byla zmáčknuta daná klávesa = změníme pozici
        player_y -= 10
    if pressed[pygame.K_a]:
        player_x -= 10
    if pressed[pygame.K_s]:
        player_y += 10
    if pressed[pygame.K_d]:
        player_x += 10
    for event in pygame.event.get(): #zjištění eventů, které mohou nastat
        if event.type == pygame.QUIT: #je potřeba registrovat event vypnutí křížkem, jinak hra nepůjde vypnout
            running = False
    screen.fill("black") #pro každý cyklus vyplníme celé okno barvou - resetujeme původní verzi okna
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 88) #vykreslení kruhu - barva, souřadnice, radius
    pygame.draw.rect(screen, (176, 0, 181), pygame.Rect(10, 10, 100, 200)) #vykreslení obdélníku - barva, počáteční souřadnice, koncové souřadnice
    pygame.display.flip() #nastavíme, že se nám okno bude aktualizovat
    clock.tick(120) #nastavíme obnovovací frekvenci okna - nutno použít 30, 60 nebo 120 (při těchto frekvencích lidské oko nezaznamená problikávání)