import pygame
import player
import data
import renderer
from UI import render_all_UI
from data import screen
import sys
from buttons import CreateButton
from player import health

pygame.init()

sliding = False
WIDTH, HEIGHT = 1920, 1080
MAX_FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Menu")
background = pygame.image.load("images/menu_sprites/back4.png")
pygame.mixer.music.load("images/menu_sprites/menu_theme.mp3")
pygame.mixer.music.play(-1, start=0.0, fade_ms=0)
pygame.mixer.music.set_volume(data.volume)


def overlay():
    continue_button = CreateButton(WIDTH / 2 - (252*3), 450, 252, 74, "Continue",
                                   "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                                   "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    settings_button = CreateButton(WIDTH / 2 - (252 / 2), 550, 252, 74, "Settings",
                                   "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                                   "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    exit_button = CreateButton(WIDTH / 2 - (252 / 2), 650, 252, 74, "Exit", "images/menu_sprites/DischargePro.ttf",
                               "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    pause = True
    while pause:
        pygame.mouse.set_visible(True)
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("Pause", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == continue_button:
                fade()
                pause = False

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [continue_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [continue_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def dead_menu():
    try_again_button = CreateButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Try again",
                                    "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                                    "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    back_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Back to menu",
                               "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    fade()
    running = True
    while running:
        pygame.mouse.set_visible(True)
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("You are dead", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [try_again_button, back_button]:
                btn.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                main_menu()

            if event.type == pygame.USEREVENT and event.button == try_again_button:
                fade()
                player.clear_level()
                game_run()

        for btn in [try_again_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def main_menu():
    start_button = CreateButton(WIDTH / 2 - (252 * 3)+(252 / 2), 350, 252, 74, "Start mission",
                                "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                                "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    settings_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Settings",
                                   "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                                   "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    exit_button = CreateButton(WIDTH / 2 - (252 / 2), 650, 252, 74, "Exit", "images/menu_sprites/DischargePro.ttf",
                               "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    about_button = CreateButton(WIDTH / 2 - (252 / 2), 550, 252, 74, "About", "images/menu_sprites/DischargePro.ttf",
                                "images/menu_sprites/button3.png",
                                "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    running = True
    while running:
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("Street of brocken lanterns", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                fade()
                player.clear_level()
                game_run()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == about_button:
                fade()
                about_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button, about_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button, about_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def settings_menu():
    audio_button = CreateButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Audio", "images/menu_sprites/DischargePro.ttf",
                                "images/menu_sprites/button3.png",
                                "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    back_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Back to menu",
                               "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    running = True
    while running:
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("Settings", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for btn in [audio_button, back_button]:
                btn.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == audio_button:
                fade()
                audio_settings(sliding)

        for btn in [audio_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def audio_settings(sliding):
    back_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Back to menu",
                               "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    slider_bar_rect = pygame.Rect(100, 200, 400, 10)
    slider_knob_rect = pygame.Rect(400*data.volume+100, 180, 20, 40)
    # output = TextBox(screen, WIDTH / 2 - (252 / 2) + 280, 150 + 50, 50, 50, fontSize=30)
    # output.disable()

    running = True
    while running:
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("Audio settings", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and slider_knob_rect.collidepoint(event.pos):
                sliding = True
            if event.type == pygame.MOUSEBUTTONUP:
                sliding = False
            if event.type == pygame.MOUSEMOTION and sliding:
                mouse_pos_x = pygame.mouse.get_pos()[0]
                slider_knob_rect.x = mouse_pos_x - 10
                if slider_knob_rect.x > 500:
                    slider_knob_rect.x = 500
                if slider_knob_rect.x < 100:
                    slider_knob_rect.x = 100
                data.volume = (slider_knob_rect.x - 100) / 400
            pygame.mixer.music.set_volume(data.volume)


            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for btn in [back_button]:
                btn.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.draw.rect(screen, (255, 255, 255), slider_bar_rect)
        pygame.draw.rect(screen, (0, 0, 255), slider_knob_rect)
        sound_font = pygame.font.SysFont(None, 24)
        sound_text = sound_font.render("Volume: " + str(int(data.volume * 100)) + "%", True, (255, 255, 255))
        screen.blit(sound_text, (280, 130))

        pygame.display.flip()


def about_menu():
    back_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Back to menu",
                               "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    running = True
    while running:
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("About", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 42)
        text_surface = font.render("a game made using the pygame library", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 350))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [back_button]:
                btn.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def game_run():
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
            if player.health < 0:
                dead_menu()

            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                overlay()

        data.game_clock.tick(data.fps)


def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(black)
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)


main_menu()
