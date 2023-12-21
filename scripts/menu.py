import pygame
import sys
from buttons import CreateButton

pygame.init()

WIDTH, HEIGHT = 1920, 1080
MAX_FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Menu")
background = pygame.image.load("images/menu_sprites/back.png")


def main_menu():
    start_button = CreateButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Start mission", "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png")
    settings_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Settings", "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                                  "images/menu_sprites/hover_button3.png")
    exit_button = CreateButton(WIDTH / 2 - (252 / 2), 650, 252, 74, "Exit", "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                              "images/menu_sprites/hover_button3.png")
    about_button = CreateButton(WIDTH / 2 - (252 / 2), 550, 252, 74, "About", "images/menu_sprites/DischargePro.ttf","images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png")

    running = True
    while running:
        screen.fill(black)
        screen.blit(background, (0, 0))

        font = pygame.font.Font("images/menu_sprites/DischargePro.ttf", 100)
        text_surface = font.render("Menu", True, white)
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

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
    audio_button = CreateButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Audio", "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                               "images/menu_sprites/hover_button3.png")
    back_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Back to menu", "images/menu_sprites/DischargePro.ttf","images/menu_sprites/button3.png",
                              "images/menu_sprites/hover_button3.png")

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

        for btn in [audio_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def about_menu():
    back_button = CreateButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Back to menu", "images/menu_sprites/DischargePro.ttf", "images/menu_sprites/button3.png",
                              "images/menu_sprites/hover_button3.png")

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
    screen.fill(black)


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