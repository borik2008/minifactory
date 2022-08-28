import sys
import pygame
import os

WIDTH = 1920
HEIGHT = 1080
MUSIC_VOLUME = 0.1

main_folder = os.path.dirname(__file__)

fon_image = pygame.image.load(os.path.join(main_folder, "images/Fon.jpg"))
btn_settings_img = pygame.image.load(os.path.join(main_folder, "images/Settings.png"))
btn_start_img = pygame.image.load(os.path.join(main_folder, "images/Start.png"))
btn_sound_off_img = pygame.image.load(os.path.join(main_folder, "images/buttons/soundOFF.png"))
btn_sound_minus_img = pygame.image.load(os.path.join(main_folder, "images/buttons/sound_minus.png"))
btn_sound_plus_img = pygame.image.load(os.path.join(main_folder, "images/buttons/sound_plus.png"))
btn_back_img = pygame.image.load(os.path.join(main_folder, "images/buttons/back.png"))
btn_yes_img = pygame.image.load(os.path.join(main_folder, "images/buttons/yes.png"))
btn_no_img = pygame.image.load(os.path.join(main_folder, "images/buttons/no.png"))
btn_quit_img = pygame.image.load(os.path.join(main_folder, "images/quit.png"))
number_0_img = pygame.image.load(os.path.join(main_folder, "images/numbers/0.png"))
number_10_img = pygame.image.load(os.path.join(main_folder, "images/numbers/10.png"))
number_20_img = pygame.image.load(os.path.join(main_folder, "images/numbers/20.png"))
number_30_img = pygame.image.load(os.path.join(main_folder, "images/numbers/30.png"))
number_40_img = pygame.image.load(os.path.join(main_folder, "images/numbers/40.png"))
number_50_img = pygame.image.load(os.path.join(main_folder, "images/numbers/50.png"))
number_60_img = pygame.image.load(os.path.join(main_folder, "images/numbers/60.png"))
number_70_img = pygame.image.load(os.path.join(main_folder, "images/numbers/70.png"))
number_80_img = pygame.image.load(os.path.join(main_folder, "images/numbers/80.png"))
number_90_img = pygame.image.load(os.path.join(main_folder, "images/numbers/90.png"))
number_100_img = pygame.image.load(os.path.join(main_folder, "images/numbers/100.png"))
fon_game_img = pygame.image.load(os.path.join(main_folder, "images/fon_game.jpeg"))
hud_up_img = pygame.image.load(os.path.join(main_folder, "images/hud/hud_up.png"))
hud_down_img = pygame.image.load(os.path.join(main_folder, "images/hud/hud_down.png"))

numbers_image = [number_0_img, number_10_img, number_20_img, number_30_img, number_40_img, number_50_img, number_60_img, number_70_img, number_80_img, number_90_img, number_100_img]

fon_music = os.path.join(main_folder, 'sounds\\oil_rig_ambience_01.mp3')

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mini Factory")


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def set_img(self, image):
        self.image = image


def settings():
    global MUSIC_VOLUME
    sound_off_btn = Button(btn_sound_off_img, (WIDTH / 2, HEIGHT / 2 + 200))
    sound_minus_btn = Button(btn_sound_minus_img, (WIDTH / 2 - 100, HEIGHT / 2 + 70))
    sound_plus_btn = Button(btn_sound_plus_img, (WIDTH / 2 + 100, HEIGHT / 2 + 70))
    back_to_menu_btn = Button(btn_back_img, (WIDTH / 2, HEIGHT / 2 - 100))
    number = Button(numbers_image[int(MUSIC_VOLUME * 10)], (WIDTH / 2, HEIGHT / 2 + 70))
    buttons = pygame.sprite.Group()
    buttons.add(sound_off_btn, sound_minus_btn, sound_plus_btn, back_to_menu_btn, number)
    settings_process = True
    while settings_process:
        screen.blit(fon_image, fon_image.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_to_menu_btn.rect.collidepoint(mouse_pos):
                    settings_process = False
                if sound_plus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME < 1:
                        MUSIC_VOLUME += 0.1
                        number.set_img(numbers_image[int(MUSIC_VOLUME * 10)])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                if sound_minus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME > 0:
                        MUSIC_VOLUME -= 0.1
                        number.set_img(numbers_image[int(MUSIC_VOLUME * 10)])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                if sound_off_btn.rect.collidepoint(mouse_pos):
                    pygame.mixer.music.set_volume(0)
                    number.set_img(numbers_image[0])
                    MUSIC_VOLUME = 0

        screen.blit(fon_image, fon_image.get_rect())
        buttons.draw(screen)
        pygame.display.flip()


def confrim():
    yes_btn = Button(btn_yes_img, (WIDTH / 2 + 100, HEIGHT / 2))
    no_btn = Button(btn_no_img, (WIDTH / 2 - 100, HEIGHT / 2))
    buttons = pygame.sprite.Group()
    buttons.add(yes_btn, no_btn)
    screen.blit(fon_image, fon_image.get_rect())
    buttons.draw(screen)
    pygame.display.flip()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if yes_btn.rect.collidepoint(mouse_pos):
                    return 1
                if no_btn.rect.collidepoint(mouse_pos):
                    return 0



def menu():
    pygame.mixer.music.load(fon_music)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.play(-1)
    start_btn = Button(btn_start_img, (WIDTH / 2, HEIGHT / 2 - 100))
    settings_btn = Button(btn_settings_img, (WIDTH / 2, HEIGHT / 2 + 100))
    quit_btn = Button(btn_quit_img, (WIDTH / 2, HEIGHT / 2 + 200))
    buttons = pygame.sprite.Group()
    buttons.add(start_btn, settings_btn, quit_btn)
    while True:
        screen.blit(fon_image, fon_image.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if settings_btn.rect.collidepoint(mouse_pos):
                    settings()
                if quit_btn.rect.collidepoint(mouse_pos):
                    if confrim() == 1:
                        sys.exit()
                if start_btn.rect.collidepoint(mouse_pos):
                    game()
        buttons.draw(screen)
        pygame.display.flip()


def game():
    hud_up = Button(hud_up_img, (WIDTH / 2, HEIGHT / 2))
    hud_down = Button(hud_down_img, (WIDTH / 2, HEIGHT / 2))
    buttons = pygame.sprite.Group()
    buttons.add(hud_up, hud_down)
    while True:
        screen.blit(fon_game_img, fon_game_img.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        return 0
        buttons.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    menu()
