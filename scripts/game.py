import pygame
import data
import player
import renderer

pygame.init()

screen = pygame.display.set_mode(data.screen_size, flags=pygame.NOFRAME)
pygame.display.set_caption("raycasters2005")
# gameIcon = pygame.image.load("images/icon.png")
# pygame.display.set_icon(gameIcon)

game_running = True
game_clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


while game_running:
    player.movement()
    renderer.draw_scene(screen)
    pygame.display.update()
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    game_clock.tick(data.fps)
