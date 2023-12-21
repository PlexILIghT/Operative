import data
from player import health
from weapon import selector, m4, pistol


def render_hp(health):
    text = data.font.render(f"HEALTH: {health}", True, "white")
    data.screen.blit(text, (data.screen_width * 0.8, data.screen_height * 0.9))


def render_ammo():
    if selector.selectionFlag:
        max_ammo = pistol.maxAmmo
        cur_ammo = pistol.maxAmmo - pistol.ammo
    else:
        max_ammo = m4.maxAmmo
        cur_ammo = m4.maxAmmo - m4.ammo

    text = data.font.render(f"{cur_ammo} / {max_ammo}", True, "white")
    data.screen.blit(text, (data.screen_width * 0.8, data.screen_height * 0.8))


def render_all(health):
    render_hp(health)
    render_ammo()