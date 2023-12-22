import pygame
import player
import data
import renderer
from UI import render_all_UI
pygame.init()

pygame.display.set_caption("raycasters2005")
# gameIcon = pygame.image.load("images/icon.png")
# pygame.display.set_icon(gameIcon)

game_running = True
flag_time = True
pygame.mouse.set_visible(False)

while game_running:
    if flag_time == True:
        start_time = pygame.time.get_ticks()
        flag_time = False
    player.movement()

    renderer.draw_scene(data.screen)
    render_all_UI(player.health, start_time)
    player.blood_animation()

    pygame.display.update()
    data.screen.fill("black")

    renderer.animation_frame = pygame.time.get_ticks() // 60



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    data.game_clock.tick(data.fps)
