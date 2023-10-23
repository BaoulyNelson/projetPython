import pygame
import random
import time

# mwen inisyalize pygame
pygame.init()

# mw defini tay ekran
laje, ote = 400, 600
fenet = pygame.display.set_mode((laje, ote))

wuj = (255, 0, 0)  # mw bayo couleur
blan = (255, 255, 255)


# klas obstak la
class Obstak:
    def __init__(self):
        self.laje = 50
        self.ote = 20
        self.x = random.randint(0, laje - self.laje)
        self.y = 0

    def desann(self):
        self.y += 1

    def afiche(self):
        pygame.draw.rect(fenet, wuj, (self.x, self.y, self.laje, self.ote))


obstacles = []

# Bouk prensipal
kontinye = True
oloj = pygame.time.Clock()

while kontinye:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kontinye = False

    # ann kyeye 1lot obstak ka pa aza
    if random.random() < 0.01:
        obstacles.append(Obstak())

    # efase ekran
    fenet.fill(blan)

    # Afiche ak fe obtak yo desann
    for obstacle in obstacles:
        obstacle.desann()
        obstacle.afiche()
        if obstacle.y > ote:
            obstacles.remove(obstacle)

    # Mete afichaj la a jou
    pygame.display.update()

    oloj.tick(60)  # nap limite l

# nou soti nn pygame lan
pygame.quit()
