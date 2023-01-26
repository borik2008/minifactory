import pygame
import os

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
hud_up_img = pygame.image.load(os.path.join(main_folder, "images/hud/hud_up1.png"))
hud_down_img = pygame.image.load(os.path.join(main_folder, "images/hud/hud_down1.png"))
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
ikonka_asembler_image = pygame.image.load(os.path.join(main_folder, "images/asembler 1.png"))
ikonka_bur_image = pygame.image.load(os.path.join(main_folder, "images/bur 1.png"))
ikonka_constructor_image = pygame.image.load(os.path.join(main_folder, "images/constructor 1.png"))
ikonka_soedenitel_image = pygame.image.load(os.path.join(main_folder, "images/soedenitel.png"))
ikonka_razvetlitel_image = pygame.image.load(os.path.join(main_folder, "images/razvetlitel.png"))
number__1__img = pygame.image.load(os.path.join(main_folder, "images/numbers/1_.png"))
number__2__img = pygame.image.load(os.path.join(main_folder, "images/numbers/2_.png"))
number__3__img = pygame.image.load(os.path.join(main_folder, "images/numbers/3_.png"))
number__4__img = pygame.image.load(os.path.join(main_folder, "images/numbers/4_.png"))
number__5__img = pygame.image.load(os.path.join(main_folder, "images/numbers/5_.png"))
number__6__img = pygame.image.load(os.path.join(main_folder, "images/numbers/6_.png"))
number__7__img = pygame.image.load(os.path.join(main_folder, "images/numbers/7_.png"))
number__8__img = pygame.image.load(os.path.join(main_folder, "images/numbers/8_.png"))
number__9__img = pygame.image.load(os.path.join(main_folder, "images/numbers/9_.png"))
hud_postroika_right_img = pygame.image.load(os.path.join(main_folder, "images/hud/right_postroika_hud.png"))
hud_postroika_left_img = pygame.image.load(os.path.join(main_folder, "images/hud/left_postroika_hud.png"))

ikonka_text_rescurces_beton_image = pygame.image.load(os.path.join(main_folder, "images/names/beton.png"))
ikonka_text_rescurces_iron_image = pygame.image.load(os.path.join(main_folder, "images/names/iron.png"))
ikonka_text_rescurces_isvestnyak_image = pygame.image.load(os.path.join(main_folder, "images/names/isvestnyak.png"))
ikonka_text_rescurces_kabel_image = pygame.image.load(os.path.join(main_folder, "images/names/kabel.png"))
ikonka_text_rescurces_karkas_image = pygame.image.load(os.path.join(main_folder, "images/names/karkas.png"))
ikonka_text_rescurces_med_image = pygame.image.load(os.path.join(main_folder, "images/names/med.png"))
ikonka_text_rescurces_motor_image = pygame.image.load(os.path.join(main_folder, "images/names/motor.png"))
ikonka_text_rescurces_plastina_image = pygame.image.load(os.path.join(main_folder, "images/names/plastina.png"))
ikonka_text_rescurces_provolka_image = pygame.image.load(os.path.join(main_folder, "images/names/provolka.png"))
ikonka_text_rescurces_prut_image = pygame.image.load(os.path.join(main_folder, "images/names/prut.png"))
ikonka_text_rescurces_rotor_image = pygame.image.load(os.path.join(main_folder, "images/names/rotor.png"))
ikonka_text_rescurces_startor_image = pygame.image.load(os.path.join(main_folder, "images/names/startor.png"))
ikonka_text_rescurces_ukr_plastina_image = pygame.image.load(os.path.join(main_folder, "images/names/ukr_plastina.png"))
ikonka_text_rescurces_vint_image = pygame.image.load(os.path.join(main_folder, "images/names/vint.png"))
ikonka_text_rescurces_ymnaya_obshivka_image = pygame.image.load(
    os.path.join(main_folder, "images/names/ymnaya_obshivka.png"))
ikonka_text_postroyka_asembler_image = pygame.image.load(os.path.join(main_folder, "images/names/asembler.png"))
ikonka_text_postroyka_bur_image = pygame.image.load(os.path.join(main_folder, "images/names/bur.png"))
ikonka_text_postroyka_konstruktor_image = pygame.image.load(os.path.join(main_folder, "images/names/konstruktor.png"))
ikonka_text_postroyka_yashik_image = pygame.image.load(os.path.join(main_folder, "images/names/yashik.png"))
img_no_stroit = pygame.image.load(os.path.join(main_folder, "images/ne_stroit.png"))
img_close = pygame.image.load((os.path.join(main_folder, "images/hud/close.png")))
img_left = pygame.image.load((os.path.join(main_folder, "images/hud/left.png")))
img_top = pygame.image.load((os.path.join(main_folder, "images/hud/top.png")))
img_right = pygame.image.load((os.path.join(main_folder, "images/hud/right.png")))

img_blue_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/blue_window.png"))
img_green_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/green_window.png"))
img_purple_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/purple_window.png"))
img_red_window = pygame.image.load(os.path.join(main_folder, "images/for_setka/red_window.png"))
vedelenie_img = pygame.image.load(os.path.join(main_folder, "images/hud/vedelen.png"))

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
0 1 0 0 - выход сверху
0 0 0 1 - выход снизу
"""
spisok_postroiki_outputs_diraction = [[0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 1]]


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
