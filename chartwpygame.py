import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Small Universe")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

num_stars = 100
stars = []

for _ in range (num_stars):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.uniform(0.5, 2)
    stars.append([x, y, speed])

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    for star in stars:
        star[1] += star[2]
        if star[1]> HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = 0
            star[2] = random.uniform(0.5, 2)

    screen.fill(BLACK, None, 0)
    for star in stars:
        pygame.draw.circle(screen, WHITE, (int(star[0]), int(star[1])), 2)
    
    pygame.display.flip()
    clock.tick(60)