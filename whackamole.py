import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (32, 32))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x, mole_y = 0, 0

        def draw_grid():
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "dark blue", (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "dark blue", (0, y), (640, y))

        def move_mole():
            nonlocal mole_x, mole_y
            mole_x = random.randrange(0, 20) * 32
            mole_y = random.randrange(0, 16) * 32

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + 32 and mole_y <= mouse_y < mole_y + 32:
                        move_mole()

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
