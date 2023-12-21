import pygame
import player
import data
import renderer
from UI import render_all_UI
from data import screen
pygame.init()

pygame.display.set_caption("raycasters2005")
# gameIcon = pygame.image.load("images/icon.png")
# pygame.display.set_icon(gameIcon)

game_running = True
pygame.mouse.set_visible(False)


while game_running:
    player.movement()
    renderer.draw_scene(screen)
    render_all_UI(player.health)


    pygame.display.update()
    screen.fill("black")

    renderer.animation_frame = pygame.time.get_ticks() // 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    data.game_clock.tick(data.fps)
