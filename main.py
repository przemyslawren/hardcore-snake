import pygame

pygame.init()

# Setup window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hardcore Snake")

# Setup clock
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, "yellow", (50, 50, 50, 50))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
