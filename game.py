import sys
import pygame
import os
import random

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
zhila_med_img = pygame.image.load(os.path.join(main_folder, "images/med.png"))
zhila_iron_img = pygame.image.load(os.path.join(main_folder, "images/iron.png"))
zhila_isvestnyak_img = pygame.image.load(os.path.join(main_folder, "images/isvestnyak.png"))
ikonka_beton_img = pygame.image.load(os.path.join(main_folder, "images/resources/beton.png"))
ikonka_iron_img = pygame.image.load(os.path.join(main_folder, "images/resources/iron.png"))
ikonka_isvestnyak_img = pygame.image.load(os.path.join(main_folder, "images/resources/isvestnyak.png"))
ikonka_kabel_img = pygame.image.load(os.path.join(main_folder, "images/resources/kabel.png"))
ikonka_karkas_img = pygame.image.load(os.path.join(main_folder, "images/resources/karkas.png"))
ikonka_motor_img = pygame.image.load(os.path.join(main_folder, "images/resources/motor.png"))
ikonka_plastina_img = pygame.image.load(os.path.join(main_folder, "images/resources/plastina.png"))
ikonka_provolka_img = pygame.image.load(os.path.join(main_folder, "images/resources/provolka.png"))
ikonka_prut_img = pygame.image.load(os.path.join(main_folder, "images/resources/prut.png"))
ikonka_rotor_img = pygame.image.load(os.path.join(main_folder, "images/resources/rotor.png"))
ikonka_startor_img = pygame.image.load(os.path.join(main_folder, "images/resources/startor.png"))
ikonka_ukr_plastina_img = pygame.image.load(os.path.join(main_folder, "images/resources/ukr_plastina.png"))
ikonka_vint_img = pygame.image.load(os.path.join(main_folder, "images/resources/vint.png"))
ikonka_ymnaya_obshivka_img = pygame.image.load(os.path.join(main_folder, "images/resources/ymnaya_obshivka.png"))
ikonka_med_img = pygame.image.load(os.path.join(main_folder, "images/resources/med.png"))
hud_next_img = pygame.image.load(os.path.join(main_folder, "images/hud/next.png"))
hud_previos_img = pygame.image.load(os.path.join(main_folder, "images/hud/previos.png"))
number_0__img = pygame.image.load(os.path.join(main_folder, "images/numbers/0_.png"))
number_1__img = pygame.image.load(os.path.join(main_folder, "images/numbers/1.png"))

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

class Zhila(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def set_pos(self, pos):
        self.rect.center = pos

class Ikonka(pygame.sprite.Sprite):
    def __init__(self, image, pos, count):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.count = count

    def move_right(self):
        self.rect.x += 50

    def move_left(self):
        self.rect.x -= 50

    def update(self, index):
        if index == "r":
            self.move_right()
        if index == "l":
            self.move_left()




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
                        number.set_img(numbers_image[int(round(MUSIC_VOLUME * 10))])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                if sound_minus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME > 0:
                        MUSIC_VOLUME -= 0.1
                        number.set_img(numbers_image[int(round(MUSIC_VOLUME * 10))])
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
    allSpites = pygame.sprite.Group()
    for i in range(3):
        zhila_med = Zhila(zhila_med_img, (random.randint(30, WIDTH - 30),random.randint(30, HEIGHT - 30)))
        while pygame.sprite.spritecollide(zhila_med, allSpites, False):
            zhila_med.set_pos((random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)))
        allSpites.add(zhila_med)

        zhila_iron = Zhila(zhila_iron_img, (random.randint(30, WIDTH - 30),random.randint(30, HEIGHT - 30)))
        while pygame.sprite.spritecollide(zhila_iron, allSpites, False):
            zhila_iron.set_pos((random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)))
        allSpites.add(zhila_iron)

        zhila_isvestnyak = Zhila(zhila_isvestnyak_img, (random.randint(30, WIDTH - 30),random.randint(30, HEIGHT - 30)))
        while pygame.sprite.spritecollide(zhila_isvestnyak, allSpites, False):
            zhila_isvestnyak.set_pos((random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)))
        allSpites.add(zhila_isvestnyak)

    ikonka_rotor = Ikonka(ikonka_rotor_img, (WIDTH / 2, 70), 1)
    ikonka_med = Ikonka(ikonka_med_img, (WIDTH / 2 - 50, 70), 1)
    ikonka_iron = Ikonka(ikonka_iron_img, (WIDTH / 2 + 50, 70), 1)

    hud_up = Button(hud_up_img, (WIDTH / 2, HEIGHT / 2))
    hud_down = Button(hud_down_img, (WIDTH / 2, HEIGHT / 2))
    next_btn = Button(hud_next_img, (WIDTH - 262, 70))
    previos_btn = Button(hud_previos_img, (265, 70))

    ikonki = pygame.sprite.Group()
    ikonki.add(ikonka_rotor, ikonka_med, ikonka_iron)
    allSpites.add(hud_up, hud_down, ikonka_rotor, ikonka_med, ikonka_iron, next_btn, previos_btn)
    while True:
        screen.blit(fon_game_img, fon_game_img.get_rect())
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if next_btn.rect.collidepoint(mouse_pos):
                    ikonki.update("r")
                if previos_btn.rect.collidepoint(mouse_pos):
                    ikonki.update("l")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        return 0
        allSpites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    menu()
