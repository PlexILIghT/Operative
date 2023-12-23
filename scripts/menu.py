import pygame
import player
import data
import renderer
from UI import render_all_UI
from data import screen
import sys
from buttons import CreateButton

pygame.init()

sliding = False
WIDTH, HEIGHT = data.screen_width, data.screen_height
MAX_FPS = 60
clock = pygame.time.Clock()
button_width = WIDTH // 5
button_height = HEIGHT // 10
offset_between_buttons = button_height + button_height // 8
bar_width = WIDTH // 4
bar_height = HEIGHT // 30
knob_width = bar_width // 25
knob_height = round(bar_height * 1.5)
pygame.display.set_caption("Menu")
background = pygame.image.load("images/menu_sprites/back4.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.mixer.music.load("images/menu_sprites/menu_theme.mp3")
pygame.mixer.music.play(-1, start=0.0, fade_ms=0)
pygame.mixer.music.set_volume(data.volume)

pygame.display.set_caption("OPERATIVE")
# gameIcon = pygame.image.load("images/icon.png")
# pygame.display.set_icon(gameIcon)

data.load_data()
selected_level = 0

def overlay(font):
    continue_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height, "Continue",
                                   "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                   "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    settings_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + offset_between_buttons, button_width, button_height, "Settings",
                                   "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                   "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    exit_button = CreateButton(WIDTH / 2 - button_width // 2, HEIGHT // 2 + 2 * offset_between_buttons, button_width, button_height, "Back to main menu", "fonts/Disket-Mono-Regular.ttf",
                               "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    player.paused_time = pygame.time.get_ticks()
    pause = True
    while pause:
        pygame.mouse.set_visible(True)
        screen.fill("black")
        screen.blit(background, (0, 0))

        text_surface = font.render("PAUSE", True, "white")
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == continue_button:
                pygame.mouse.set_visible(False)
                pause = False
                player.start_time += pygame.time.get_ticks() - player.paused_time
                fade()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu(data.font2)

            if event.type == pygame.USEREVENT and event.button == exit_button:
                screen.fill('black')
                pygame.mouse.set_visible(True)
                data.mein_menu_flag = True
                pause = False

            for btn in [continue_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [continue_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def dead_menu(font):
    try_again_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height, "Try again",
                                    "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                    "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    back_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + offset_between_buttons, button_width, button_height, "Back to menu",
                               "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    fade()
    running = True
    while running:
        pygame.mouse.set_visible(True)
        screen.fill("black")
        screen.blit(background, (0, 0))

        text_surface = font.render("YOU ARE DEAD", True, "white")
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
                running = False

            if event.type == pygame.USEREVENT and event.button == try_again_button:
                running = False
                player.clear_level(selected_level)
                fade()
                game_run()

        for btn in [try_again_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def main_menu(font):
    start_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height, "Start mission",
                                "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    settings_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + offset_between_buttons, button_width, button_height, "Settings",
                                   "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                   "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    statistics_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 2 * offset_between_buttons, button_width, button_height, "Statistics", "fonts/Disket-Mono-Regular.ttf",
                                "images/menu_sprites/button3.png",
                                "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    exit_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 3 * offset_between_buttons, button_width, button_height, "Exit", "fonts/Disket-Mono-Regular.ttf",
                               "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    running = True
    while running:
        screen.fill("black")
        screen.blit(background, (0, 0))

        text_surface = font.render("OPERATIVE", True, "white")
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT // 3.5))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                fade()
                #player.clear_level(selected_level)
                choosing_level_menu(data.font2)
                if data.back_flag:
                    data.back_flag = False
                else:
                    game_run()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu(data.font2)

            if event.type == pygame.USEREVENT and event.button == statistics_button:
                fade()
                about_menu(data.font2)

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button, statistics_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button, statistics_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def choosing_level_menu(font):
    global selected_level
    mission_button_lvl_1 = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 2 * offset_between_buttons, button_width, button_height,
                                        "LVL 1",
                                        "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                        "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    mission_button_lvl_2 = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 - offset_between_buttons, button_width,
                                        button_height,
                                        "LVL 2",
                                        "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                        "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    mission_button_lvl_3 = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width,
                                        button_height,
                                        "LVL 3",
                                        "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                                        "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    back_button = CreateButton(WIDTH // 2 - button_width // 2,
                               HEIGHT // 2 + 2 * offset_between_buttons, button_width,
                               button_height, "Back to menu",
                               "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    running = True
    while running:

        screen.fill("black")
        screen.blit(background, (0, 0))


        text_surface = font.render("MISSIONS", True, "white")
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT // 4.5))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for btn in [back_button, mission_button_lvl_1, mission_button_lvl_2, mission_button_lvl_3]:
                btn.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                data.back_flag = True
                fade()

            if event.type == pygame.USEREVENT and event.button == mission_button_lvl_1:
                selected_level = data.map_level_1
                player.clear_level(data.map_level_1)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == mission_button_lvl_2:
                selected_level = data.map_level_2
                player.clear_level(data.map_level_2)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == mission_button_lvl_3:
                selected_level = data.map_level_3
                player.clear_level(data.map_level_3)
                fade()
                running = False

        for btn in [mission_button_lvl_3, mission_button_lvl_2, mission_button_lvl_1, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        for btn in [back_button, mission_button_lvl_1, mission_button_lvl_2, mission_button_lvl_3]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()

def settings_menu(font):
    audio_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height, "Audio", "fonts/Disket-Mono-Regular.ttf",
                                "images/menu_sprites/button3.png",
                                "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")
    back_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + offset_between_buttons, button_width, button_height, "Back to menu",
                               "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    running = True
    while running:
        screen.fill("black")
        screen.blit(background, (0, 0))


        text_surface = font.render("SETTINGS", True, "white")
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
                audio_settings(sliding, data.font2)

        for btn in [audio_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def audio_settings(sliding, font):
    back_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 2 * offset_between_buttons, button_width, button_height, "Back to menu",
                               "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    slider_bar_rect = pygame.Rect(WIDTH // 2 - bar_width // 2, HEIGHT // 2 - bar_height // 2, bar_width, bar_height)
    slider_knob_rect = pygame.Rect(WIDTH // 2 + data.volume * bar_width - bar_width // 2, HEIGHT // 2 - knob_height // 2, knob_width, knob_height)

    running = True
    while running:
        screen.fill("black")
        screen.blit(background, (0, 0))

        text_surface = font.render("AUDIO SETTINGS", True, "white")
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
                if slider_knob_rect.x > WIDTH // 2 + bar_width // 2:
                    slider_knob_rect.x = WIDTH // 2 + bar_width // 2
                if slider_knob_rect.x < WIDTH // 2 - bar_width // 2:
                    slider_knob_rect.x = WIDTH // 2 - bar_width // 2
                data.volume = (slider_knob_rect.x - WIDTH / 2 + bar_width / 2) / bar_width
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

        pygame.draw.rect(screen, "white", slider_bar_rect)
        pygame.draw.rect(screen, "gray", slider_knob_rect)
        sound_font = pygame.font.Font("fonts/Disket-Mono-Regular.ttf", 24)
        sound_text = sound_font.render("Volume: " + str(int(data.volume * 100)) + "%", True, (255, 255, 255))
        screen.blit(sound_text, (WIDTH // 2 - bar_width // 2, HEIGHT // 2 - bar_height * 2))

        pygame.display.flip()


def about_menu(font):
    back_button = CreateButton(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height, "Back to menu",
                               "fonts/Disket-Mono-Regular.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png", "images/menu_sprites/click.mp3")

    running = True
    while running:
        screen.fill("black")
        screen.blit(background, (0, 0))

        font = pygame.font.Font("fonts/Lazer-Game-Zone.ttf", 100)
        text_surface = font.render("STATISTICS", True, "white")
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("fonts/Disket-Mono-Regular.ttf", 42)
        text_surface = font.render("*statistics*", True, "white")
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
    player.flag_time = True
    player.start_time = pygame.time.get_ticks()
    while game_running:
        if player.flag_time:
            player.start_time = pygame.time.get_ticks()
            player.flag_time = False
        player.movement()

        print(player.start_time, player.paused_time)
        renderer.draw_scene(screen)
        player.blood_animation()
        render_all_UI(player.health, player.start_time)

        pygame.display.update()
        screen.fill("black")

        renderer.animation_frame = pygame.time.get_ticks() // 60

        for event in pygame.event.get():
            if player.health < 0:
                dead_menu(data.font2)
                game_running = False

            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    overlay(data.font2)
                    if data.mein_menu_flag:
                        game_running = False
                        data.mein_menu_flag = False

        data.game_clock.tick(data.fps)


def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill("black")
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)


main_menu(data.font2)
