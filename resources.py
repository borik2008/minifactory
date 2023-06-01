import pygame
import os

WIDTH = 1920
HEIGHT = 1080
SIZESETKAX = 108
SIZESETKAY = 192
MUSIC_VOLUME = 0
CONVEER_SIZE = 32

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("mini Factory")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

main_folder = os.path.dirname(__file__)

fon_image = pygame.image.load(os.path.join(main_folder, "images/Fon.jpg")).convert_alpha()
btn_settings_img = pygame.image.load(os.path.join(main_folder, "images/Settings.png")).convert_alpha()
btn_start_img = pygame.image.load(os.path.join(main_folder, "images/Start.png")).convert_alpha()
btn_sound_off_img = pygame.image.load(os.path.join(main_folder, "images/buttons/soundOFF.png")).convert_alpha()
btn_sound_minus_img = pygame.image.load(os.path.join(main_folder, "images/buttons/sound_minus.png")).convert_alpha()
btn_sound_plus_img = pygame.image.load(os.path.join(main_folder, "images/buttons/sound_plus.png")).convert_alpha()
btn_back_img = pygame.image.load(os.path.join(main_folder, "images/buttons/back.png")).convert_alpha()
btn_yes_img = pygame.image.load(os.path.join(main_folder, "images/buttons/yes.png")).convert_alpha()
btn_no_img = pygame.image.load(os.path.join(main_folder, "images/buttons/no.png")).convert_alpha()
btn_quit_img = pygame.image.load(os.path.join(main_folder, "images/quit.png")).convert_alpha()
number_0_img = pygame.image.load(os.path.join(main_folder, "images/numbers/0.png")).convert_alpha()
number_10_img = pygame.image.load(os.path.join(main_folder, "images/numbers/10.png")).convert_alpha()
number_20_img = pygame.image.load(os.path.join(main_folder, "images/numbers/20.png")).convert_alpha()
number_30_img = pygame.image.load(os.path.join(main_folder, "images/numbers/30.png")).convert_alpha()
number_40_img = pygame.image.load(os.path.join(main_folder, "images/numbers/40.png")).convert_alpha()
number_50_img = pygame.image.load(os.path.join(main_folder, "images/numbers/50.png")).convert_alpha()
number_60_img = pygame.image.load(os.path.join(main_folder, "images/numbers/60.png")).convert_alpha()
number_70_img = pygame.image.load(os.path.join(main_folder, "images/numbers/70.png")).convert_alpha()
number_80_img = pygame.image.load(os.path.join(main_folder, "images/numbers/80.png")).convert_alpha()
number_90_img = pygame.image.load(os.path.join(main_folder, "images/numbers/90.png")).convert_alpha()
number_100_img = pygame.image.load(os.path.join(main_folder, "images/numbers/100.png")).convert_alpha()
fon_game_img = pygame.image.load(os.path.join(main_folder, "images/fon_game.jpeg")).convert_alpha()
hud_up_img = pygame.image.load(os.path.join(main_folder, "images/hud/hud_up1.png")).convert_alpha()
hud_down_img = pygame.image.load(os.path.join(main_folder, "images/hud/hud_down1.png")).convert_alpha()
zhila_med_img = pygame.image.load(os.path.join(main_folder, "images/med.png")).convert_alpha()
zhila_iron_img = pygame.image.load(os.path.join(main_folder, "images/iron.png")).convert_alpha()
zhila_isvestnyak_img = pygame.image.load(os.path.join(main_folder, "images/isvestnyak.png")).convert_alpha()
ikonka_beton_img = pygame.image.load(os.path.join(main_folder, "images/resources/beton.png")).convert_alpha()
ikonka_iron_img = pygame.image.load(os.path.join(main_folder, "images/resources/iron.png")).convert_alpha()
ikonka_isvestnyak_img = pygame.image.load(os.path.join(main_folder, "images/resources/isvestnyak.png")).convert_alpha()
ikonka_kabel_img = pygame.image.load(os.path.join(main_folder, "images/resources/kabel.png")).convert_alpha()
ikonka_karkas_img = pygame.image.load(os.path.join(main_folder, "images/resources/karkas.png")).convert_alpha()
ikonka_motor_img = pygame.image.load(os.path.join(main_folder, "images/resources/motor.png")).convert_alpha()
ikonka_plastina_img = pygame.image.load(os.path.join(main_folder, "images/resources/plastina.png")).convert_alpha()
ikonka_provolka_img = pygame.image.load(os.path.join(main_folder, "images/resources/provolka.png")).convert_alpha()
ikonka_prut_img = pygame.image.load(os.path.join(main_folder, "images/resources/prut.png")).convert_alpha()
ikonka_rotor_img = pygame.image.load(os.path.join(main_folder, "images/resources/rotor.png")).convert_alpha()
ikonka_startor_img = pygame.image.load(os.path.join(main_folder, "images/resources/startor.png")).convert_alpha()
ikonka_ukr_plastina_img = pygame.image.load(os.path.join(main_folder, "images/resources/ukr_plastina.png")).convert_alpha()
ikonka_vint_img = pygame.image.load(os.path.join(main_folder, "images/resources/vint.png")).convert_alpha()
ikonka_ymnaya_obshivka_img = pygame.image.load(os.path.join(main_folder, "images/resources/ymnaya_obshivka.png")).convert_alpha()
ikonka_med_img = pygame.image.load(os.path.join(main_folder, "images/resources/med.png")).convert_alpha()
hud_next_img = pygame.image.load(os.path.join(main_folder, "images/hud/next.png")).convert_alpha()
hud_previos_img = pygame.image.load(os.path.join(main_folder, "images/hud/previos.png")).convert_alpha()
number_0__img = pygame.image.load(os.path.join(main_folder, "images/numbers/0_.png")).convert_alpha()
number_1__img = pygame.image.load(os.path.join(main_folder, "images/numbers/1.png")).convert_alpha()
ikonka_asembler_image = pygame.image.load(os.path.join(main_folder, "images/asembler_1.png")).convert_alpha()
ikonka_bur_image = pygame.image.load(os.path.join(main_folder, "images/bur_1.png")).convert_alpha()
ikonka_constructor_image = pygame.image.load(os.path.join(main_folder, "images/constructor_1.png")).convert_alpha()
ikonka_soedenitel_image = pygame.image.load(os.path.join(main_folder, "images/soedenitel.png")).convert_alpha()
ikonka_razvetlitel_image = pygame.image.load(os.path.join(main_folder, "images/razvetlitel.png")).convert_alpha()
number__1__img = pygame.image.load(os.path.join(main_folder, "images/numbers/1_.png")).convert_alpha()
number__2__img = pygame.image.load(os.path.join(main_folder, "images/numbers/2_.png")).convert_alpha()
number__3__img = pygame.image.load(os.path.join(main_folder, "images/numbers/3_.png")).convert_alpha()
number__4__img = pygame.image.load(os.path.join(main_folder, "images/numbers/4_.png")).convert_alpha()
number__5__img = pygame.image.load(os.path.join(main_folder, "images/numbers/5_.png")).convert_alpha()
number__6__img = pygame.image.load(os.path.join(main_folder, "images/numbers/6_.png")).convert_alpha()
number__7__img = pygame.image.load(os.path.join(main_folder, "images/numbers/7_.png")).convert_alpha()
number__8__img = pygame.image.load(os.path.join(main_folder, "images/numbers/8_.png")).convert_alpha()
number__9__img = pygame.image.load(os.path.join(main_folder, "images/numbers/9_.png")).convert_alpha()
hud_postroika_right_img = pygame.image.load(os.path.join(main_folder, "images/hud/right_postroika_hud.png")).convert_alpha()
hud_postroika_left_img = pygame.image.load(os.path.join(main_folder, "images/hud/left_postroika_hud.png")).convert_alpha()

ikonka_text_rescurces_beton_image = pygame.image.load(os.path.join(main_folder, "images/names/beton.png")).convert_alpha()
ikonka_text_rescurces_iron_image = pygame.image.load(os.path.join(main_folder, "images/names/iron.png")).convert_alpha()
ikonka_text_rescurces_isvestnyak_image = pygame.image.load(os.path.join(main_folder, "images/names/isvestnyak.png")).convert_alpha()
ikonka_text_rescurces_kabel_image = pygame.image.load(os.path.join(main_folder, "images/names/kabel.png")).convert_alpha()
ikonka_text_rescurces_karkas_image = pygame.image.load(os.path.join(main_folder, "images/names/karkas.png")).convert_alpha()
ikonka_text_rescurces_med_image = pygame.image.load(os.path.join(main_folder, "images/names/med.png")).convert_alpha()
ikonka_text_rescurces_motor_image = pygame.image.load(os.path.join(main_folder, "images/names/motor.png")).convert_alpha()
ikonka_text_rescurces_plastina_image = pygame.image.load(os.path.join(main_folder, "images/names/plastina.png")).convert_alpha()
ikonka_text_rescurces_provolka_image = pygame.image.load(os.path.join(main_folder, "images/names/provolka.png")).convert_alpha()
ikonka_text_rescurces_prut_image = pygame.image.load(os.path.join(main_folder, "images/names/prut.png")).convert_alpha()
ikonka_text_rescurces_rotor_image = pygame.image.load(os.path.join(main_folder, "images/names/rotor.png")).convert_alpha()
ikonka_text_rescurces_startor_image = pygame.image.load(os.path.join(main_folder, "images/names/startor.png")).convert_alpha()
ikonka_text_rescurces_ukr_plastina_image = pygame.image.load(os.path.join(main_folder, "images/names/ukr_plastina.png")).convert_alpha()
ikonka_text_rescurces_vint_image = pygame.image.load(os.path.join(main_folder, "images/names/vint.png")).convert_alpha()
ikonka_text_rescurces_ymnaya_obshivka_image = pygame.image.load(
    os.path.join(main_folder, "images/names/ymnaya_obshivka.png")).convert_alpha()
ikonka_text_postroyka_asembler_image = pygame.image.load(os.path.join(main_folder, "images/names/asembler.png")).convert_alpha()
ikonka_text_postroyka_bur_image = pygame.image.load(os.path.join(main_folder, "images/names/bur.png")).convert_alpha()
ikonka_text_postroyka_konstruktor_image = pygame.image.load(os.path.join(main_folder, "images/names/konstruktor.png")).convert_alpha()
ikonka_text_postroyka_yashik_image = pygame.image.load(os.path.join(main_folder, "images/names/yashik.png")).convert_alpha()
img_no_stroit = pygame.image.load(os.path.join(main_folder, "images/ne_stroit.png")).convert_alpha()
img_close = pygame.image.load(os.path.join(main_folder, "images/hud/close.png")).convert_alpha()
img_left = pygame.image.load(os.path.join(main_folder, "images/hud/left.png")).convert_alpha()
img_top = pygame.image.load(os.path.join(main_folder, "images/hud/top.png")).convert_alpha()
img_right = pygame.image.load(os.path.join(main_folder, "images/hud/right.png")).convert_alpha()
img_conveer_straight = pygame.image.load(os.path.join(main_folder, "images/new_conveer_1.png")).convert_alpha()
img_conveer_corner = pygame.image.load(os.path.join(main_folder, "images/conveer_2.png")).convert_alpha()

img_blue_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/blue_window.png")).convert_alpha()
img_green_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/green_window.png")).convert_alpha()
img_purple_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/purple_window.png")).convert_alpha()
img_red_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/red_window.png")).convert_alpha()
vedelenie_img = pygame.image.load(os.path.join(main_folder, "images/hud/vedelen.png")).convert_alpha()
dell_img = pygame.image.load(os.path.join(main_folder, "images/hud/dell.png"))

# зелёный пустота
# фиолетовый жилы
# синий бур
# красный все остальные постройки
spisok_windows_image = [img_green_window, img_purple_window, img_blue_window, img_red_window]

spisok_zhil_image = [zhila_iron_img, zhila_isvestnyak_img, zhila_med_img]

spisok_postroiki_image = [ikonka_asembler_image, ikonka_bur_image, ikonka_constructor_image, ikonka_razvetlitel_image,
                          ikonka_soedenitel_image]

spisok_strelki_img = [img_left, img_top, img_right]

"""
0 0 1 0 - выход справо
1 0 0 0 - выход слева
0 1 0 0 - выход cнизу
0 0 0 1 - выход сверху
"""
spisok_postroiki_outputs_diraction = [[0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 1]]

"""
assembler - два слева
miner - отсутствуют входные порты
constructor - один справа
splitter - один снизу
connector - подному слева, снизу, справа
"""
spisok_postroiki_input_ports = [
                                [[(0,0), (0,0)], [(0,0), (0,0)], [(0,0), (0,0)], [(0,0), (0,0)]],
                                None,
                                [[(10, 10)], [(-10, -10)], [(-10, -10)], [(-10, -10)]],
                                [[(0, 28)], [(28, 0)], [(0, -28)], [(-28, 0)]],
                                [[(0,0), (0,0), (0,0)], [(0,0), (0,0), (0,0)], [(0,0), (0,0), (0,0)], [(0,0), (0,0), (0,0)]]
                                ]



spisok_rescurces_img = [ikonka_beton_img, ikonka_iron_img, ikonka_isvestnyak_img, ikonka_kabel_img,
                        ikonka_karkas_img,
                        ikonka_med_img, ikonka_motor_img, ikonka_plastina_img, ikonka_provolka_img,
                        ikonka_prut_img,
                        ikonka_rotor_img, ikonka_startor_img, ikonka_ukr_plastina_img, ikonka_vint_img,
                        ikonka_ymnaya_obshivka_img]

names_rescurces = [ikonka_text_rescurces_beton_image, ikonka_text_rescurces_iron_image,
                   ikonka_text_rescurces_isvestnyak_image, ikonka_text_rescurces_kabel_image,
                   ikonka_text_rescurces_karkas_image,
                   ikonka_text_rescurces_med_image, ikonka_text_rescurces_motor_image,
                   ikonka_text_rescurces_plastina_image, ikonka_text_rescurces_provolka_image,
                   ikonka_text_rescurces_prut_image,
                   ikonka_text_rescurces_rotor_image, ikonka_text_rescurces_startor_image,
                   ikonka_text_rescurces_ukr_plastina_image, ikonka_text_rescurces_vint_image,
                   ikonka_text_rescurces_ymnaya_obshivka_image, ikonka_text_postroyka_asembler_image,
                   ikonka_text_postroyka_bur_image, ikonka_text_postroyka_konstruktor_image,
                   ikonka_text_postroyka_yashik_image,
                   ikonka_text_postroyka_yashik_image]

numbers_image_for_sound = [number_0_img, number_10_img, number_20_img, number_30_img, number_40_img, number_50_img,
                           number_60_img, number_70_img, number_80_img, number_90_img, number_100_img]

numbers_image = [number_0__img, number__1__img, number__2__img, number__3__img, number__4__img, number__5__img,
                 number__6__img, number__7__img, number__8__img, number__9__img]

fon_music = os.path.join(main_folder, 'sounds\\oil_rig_ambience_01.mp3')
