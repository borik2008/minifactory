import time
from classes import *
import sys
import random

# Функция описываюшея работу меню настроек
def settings():
    # подключаем глобальную переменнаю по уровню громкости музыки
    global MUSIC_VOLUME
    # создаём спрайты интерфейса управления данного меню
    sound_off_btn = Button(btn_sound_off_img, (WIDTH / 2, HEIGHT / 2 + 200))
    sound_minus_btn = Button(btn_sound_minus_img, (WIDTH / 2 - 100, HEIGHT / 2 + 70))
    sound_plus_btn = Button(btn_sound_plus_img, (WIDTH / 2 + 100, HEIGHT / 2 + 70))
    back_to_menu_btn = Button(btn_back_img, (WIDTH / 2, HEIGHT / 2 - 100))
    number = Button(numbers_image_for_sound[int(MUSIC_VOLUME * 10)], (WIDTH / 2, HEIGHT / 2 + 70))
    # создаём группу для всех элементов управления
    buttons = pygame.sprite.Group()
    buttons.add(sound_off_btn, sound_minus_btn, sound_plus_btn, back_to_menu_btn, number)
    while True:
        # отслеживаем нажатые пользователем клавиши
        for event in pygame.event.get():
            # обрабатываем случай если пользователь нажал ESC, вызываем меню подтвержения(выходим/остаёмся)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        sys.exit()
            # обрабатываем случай если пользователь нажал лкм
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # если пользаватель нажал назад то возвзращаемся назад
                if back_to_menu_btn.rect.collidepoint(mouse_pos):
                    return
                # если пользователь нажал прибавить громкость то увеличиваем громкость и меняем изображения громкости
                if sound_plus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME < 1:
                        MUSIC_VOLUME += 0.1
                        number.set_img(numbers_image_for_sound[int(round(MUSIC_VOLUME * 10))])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                # если пользователь нажал уменьшить громкость то уменьшаем громкость и меняем изображения громкости
                if sound_minus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME > 0:
                        MUSIC_VOLUME -= 0.1
                        number.set_img(numbers_image_for_sound[int(round(MUSIC_VOLUME * 10))])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                # если пользователь нажал отключить громкость то отключаем громкость и меняем изображения громкости
                if sound_off_btn.rect.collidepoint(mouse_pos):
                    pygame.mixer.music.set_volume(0)
                    number.set_img(numbers_image_for_sound[0])
                    MUSIC_VOLUME = 0

        # перекрываем поверх всех элементов фоновое изображение
        screen.blit(fon_image, fon_image.get_rect())
        # отрисовываем кнопки на экране
        buttons.draw(screen)
        # обновляем сформировонаё изображение экрана
        pygame.display.flip()


def confrim():
    # создаём спрайты
    yes_btn = Button(btn_yes_img, (WIDTH / 2 + 100, HEIGHT / 2))
    no_btn = Button(btn_no_img, (WIDTH / 2 - 100, HEIGHT / 2))
    # создаём группу спрайтов
    buttons = pygame.sprite.Group()
    buttons.add(yes_btn, no_btn)
    # формируем изображения подтвержения
    screen.blit(fon_image, fon_image.get_rect())
    buttons.draw(screen)
    pygame.display.flip()
    while True:
        # проверяем нажал ли пользователь на (yes/no) и выходим из функции
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
    # создаём спрайты
    start_btn = Button(btn_start_img, (WIDTH / 2, HEIGHT / 2 - 100))
    settings_btn = Button(btn_settings_img, (WIDTH / 2, HEIGHT / 2 + 100))
    quit_btn = Button(btn_quit_img, (WIDTH / 2, HEIGHT / 2 + 200))
    # создаём группу для спрайтов
    buttons = pygame.sprite.Group()
    buttons.add(start_btn, settings_btn, quit_btn)
    while True:
        for event in pygame.event.get():
            # проверяем надал ли пользователь лкм
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # если пользователь нажал настройки то открывается меню настроек
                if settings_btn.rect.collidepoint(mouse_pos):
                    settings()
                # если пользователь нажал выход то открывается меню подтверждения выхода из игры
                if quit_btn.rect.collidepoint(mouse_pos):
                    if confrim() == 1:
                        sys.exit()
                # если пользователь нажал старт то открываается игра
                if start_btn.rect.collidepoint(mouse_pos):
                    game()

        # формируем изображение меню
        screen.blit(fon_image, fon_image.get_rect())
        buttons.draw(screen)
        pygame.display.flip()


def game():
    # создаём группу спрайтов
    objects = pygame.sprite.Group()
    zhil_group = pygame.sprite.Group()
    allSpites = pygame.sprite.Group()

    # создаём сетку размером 115 на 115 для размещения жил
    setka_zhil = [0] * 10
    for i in range(10):
        setka_zhil[i] = [0] * 17

    # размещение жил по сетке
    for i in range(0, 3):
        numbers = 0
        peremennaya = 0
        while True:
            num1 = random.randint(1, 8)
            num2 = random.randint(0, 15)
            if setka_zhil[num1 + 1][num2] != 0 or setka_zhil[num1 - 1][num2] != 0 or setka_zhil[num1][
                num2 + 1] != 0 or num2 - 1 >= 0 and setka_zhil[num1][num2 - 1] != 0:
                continue
            if setka_zhil[num1][num2] == 0:
                zhila = Zhila(i + 1, (num2 * 115, num1 * 115))
                setka_zhil[num1][num2] = zhila.get_id()
                numbers += 1
                objects.add(zhila)
                zhil_group.add(zhila)
            peremennaya += 1
            if numbers == 3:
                break

    # создаём спрайты построек, интерфейса
    ikonka_count_resources_001 = Button(numbers_image[0], (WIDTH / 2 - 400, 70))
    ikonka_count_resources_010 = Button(numbers_image[0], (WIDTH / 2 - 420, 70))
    ikonka_count_resources_100 = Button(numbers_image[0], (WIDTH / 2 - 440, 70))
    ikonki_rescurces = pygame.sprite.Group()
    ikonki_postroek = pygame.sprite.Group()
    for i in range(15):
        ikonka_rescurce = Ikonka_rescurces((WIDTH / 2 - 350 + i * 50, 70), 10, i + 20)
        ikonki_rescurces.add(ikonka_rescurce)
    for i in range(5):
        ikonka_postroek = Postroika((WIDTH / 2 - 200 + i * 100, HEIGHT - 70), 1, 10 + i)
        ikonki_rescurces.add(ikonka_postroek)
        ikonki_postroek.add(ikonka_postroek)
    ikonka_name = Button(names_rescurces[0], (WIDTH / 2 - 630, 70))

    hud_up = Button(hud_up_img, (WIDTH / 2, HEIGHT / 2))
    hud_down = Button(hud_down_img, (WIDTH / 2, HEIGHT / 2))
    group_postroek = pygame.sprite.Group()
    group_hud = pygame.sprite.Group()
    input_ports_group = pygame.sprite.Group()
    strelki_group = pygame.sprite.Group()
    # добовляем в группы спрайтов спрайты
    allSpites.add(hud_up, hud_down, ikonka_count_resources_001, ikonka_count_resources_010, ikonka_count_resources_100,
                  ikonka_name)
    # создаём переменнаю для проверки привязанна ли расположение постройки к расположению мышки
    captured = False
    timer = time.time()
    first_position_for_movement = (0, 0)
    move_map = False
    hud = False
    vedelenie = None
    is_template_conveer = False

    while True:
        if time.time() - timer > 1:
            timer = time.time()
            for building in group_postroek:
                print(building.id, building.resources)
                building.update(12)
        for building in group_postroek:
            building.update(11)

        # print(len(prtroek) + len(group_hud) + len(allSpites) + len(ikonki_rescurces) + len(ikonki_postroek))
        screen.blit(fon_game_img, fon_game_img.get_rect())
        # отображаем кол-во ресурсов для предмета на который мы навелись
        mouse_pos = pygame.mouse.get_pos()
        for i in ikonki_rescurces:
            if pygame.Rect.collidepoint(i.rect, mouse_pos):
                ikonka_name.set_img(i.update(3))
                ikonka_count_resources_001.set_img(numbers_image[i.update(1) % 10])
                ikonka_count_resources_010.set_img(numbers_image[i.update(1) % 100 // 10])
                ikonka_count_resources_100.set_img(numbers_image[i.update(1) // 100])
        current_events = pygame.event.get()
        if hud and pygame.MOUSEBUTTONDOWN not in current_events:
            if is_template_conveer and conveer_teamplate is not None:
                conveer_teamplate.kill()
                conveer_teamplate = None
            for strelka in strelki_group:
                if strelka.rect.collidepoint(mouse_pos):
                    strelka_type = strelka.get_type()
                    diraction = strelka.get_direction()
                    last_conveer = vedelenaya_postroika.get_conveer(diraction)
                    cordinates = vedelenaya_postroika.get_cordinates_for_conveer(diraction, strelka_type)
                    if cordinates is None:
                        break
                    conveer_teamplate = Conveer(strelka_type, cordinates, diraction, last_conveer, True)
                    objects.add(conveer_teamplate)
                    is_template_conveer = True
        # проверяем нажата ли какая нибудь кнопка
        for event in current_events:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and captured:
                selected_building.rotate()
            # отрисовывать сдесь меню постройки
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and not hud and not captured:


                for postroika in group_postroek:
                    if pygame.Rect.collidepoint(postroika.rect, mouse_pos) and isinstance(postroika, Postroika):
                        hud = True
                        vedelenaya_postroika = postroika
                        vedelenie = Button(vedelenie_img, postroika.rect.center)
                        objects.add(vedelenie)
                        id = postroika.update(2)
                        rotate_count = postroika.update(8)

                if hud:
                    hud_x, hud_image = get_x_conrdinate_hud(mouse_pos)
                    hud_postroika = Button(hud_image, (hud_x, 540))
                    group_hud.add(hud_postroika)
                    draw_arrows(vedelenaya_postroika, strelki_group, hud_x)
                    postroika_na_hud = Button(spisok_postroiki_image[id - 10], (hud_x, 540), rotate_count)
                    group_hud.add(postroika_na_hud, vedelenie)
                    show_ports(group_postroek, group_hud)
                    close_button = Button(img_close, (hud_x, 100))
                    group_hud.add(close_button)

            elif hud and pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                for object in strelki_group:
                    object.kill()
                for object in group_hud:
                    object.kill()
                hud = False
            # если пользователь нажал клавишу мышки
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # создаём спрайт постройки исли пользователь выбрал одну из них
                for i in ikonki_postroek:
                    if pygame.Rect.collidepoint(i.rect, mouse_pos):
                        selected_building = Postroika(mouse_pos, 1, i.update(2))
                        captured = True
                        objects.add(selected_building)
            if event.type == pygame.MOUSEBUTTONDOWN:
                strelka = strelka_press(mouse_pos, strelki_group)
                if strelka:
                    if strelka.get_type() != 4:
                        conveer = vedelenaya_postroika.add_new_conveer(strelka, group_postroek, input_ports_group)
                        if conveer is not None:
                            group_postroek.add(conveer)
                            objects.add(conveer)

                    else:
                        vedelenaya_postroika.delit_conveer(strelka)

            # отслеживаем решил ли пользователь переместится по карте
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1] and move_map == False:
                first_position_for_movement = mouse_pos
                move_map = True
            # отрисовываем новое положение карты
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[1] == False and move_map:
                move_map = False
                moving_map(objects, zhila, mouse_pos, first_position_for_movement)

            # если клавиша мышки отпущена после нажатия и до этого была выбрана постройка для размещения
            # пытаемся разместить обект по сетке
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == False and captured:
                captured = False
                try_to_place(selected_building, group_postroek, zhil_group, input_ports_group)

            # когда пользователь нажмёт ESC то появится окно (yes/no) для выхода
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        return 0
        # в кординаты выбранной постройки передаём mouse_pos
        if 'selected_building' in locals() and captured:
            selected_building.rect.x = mouse_pos[0]
            selected_building.rect.y = mouse_pos[1]

        # формируем изображение игры

        objects.draw(screen)
        allSpites.draw(screen)
        ikonki_rescurces.draw(screen)
        group_hud.draw(screen)
        strelki_group.draw(screen)
        pygame.display.flip()


def moving_map(objects, zhila, mouse_pos, first_position_for_movement):
    # ищем минимальные кординаты x и y для определения границ смещения всех объектов
    object_pos = zhila.update(7)
    min_x = object_pos[0]
    min_y = object_pos[1]
    for i in objects:
        x = i.update(7)[0]
        y = i.update(7)[1]
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    # вычесляем смещение с учётом определённых границ
    x_move = first_position_for_movement[0] - mouse_pos[0]
    y_move = first_position_for_movement[1] - mouse_pos[1]
    if min_x + x_move < 0:
        x_move = x_move - (min_x + x_move)
    if min_y + y_move < 0:
        y_move = y_move - (min_y + y_move)

    # смещаем объекты
    for i in objects:
        i.update(6, x_move, y_move)


def get_x_conrdinate_hud(mouse_pos):
    if 1920 / 2 < mouse_pos[0]:
        hud_image = hud_postroika_left_img
        hud_x = 214

    elif 1920 / 2 > mouse_pos[0]:
        hud_image = hud_postroika_right_img
        hud_x = 1920 - 214
    return hud_x, hud_image


def draw_arrows(postroika, strelki_group, hud_x):
    spisok_napravlenie = postroika.update(9)
    for i in range(4):
        if spisok_napravlenie[i] == 1:
            strelki_group.add(Strelki([hud_x, 540], i, 0, postroika))
            strelki_group.add(Strelki([hud_x, 540], i, 1, postroika))
            strelki_group.add(Strelki([hud_x, 540], i, 2, postroika))
            strelki_group.add(Strelki([hud_x, 540], i, 1, postroika, 40))

def try_to_place(selected_building, group_postroek, zhil_group, input_ports_group):
    new_pos = selected_building.rect.center
    selected_building.rect.x = new_pos[0] // 32 * 32
    selected_building.rect.y = new_pos[1] // 32 * 32
    if selected_building.get_id() == 11:
        for zhila in zhil_group:
            if pygame.Rect.collidepoint(zhila.rect, selected_building.rect.center):
                if selected_building.rect.x > zhila.rect.x and selected_building.rect.y > zhila.rect.y and selected_building.rect.bottom < zhila.rect.bottom and selected_building.rect.right < zhila.rect.right:
                    selected_building.set_na_zhile(zhila.get_id())
                    group_postroek.add(selected_building)
                    return
        selected_building.kill()
    else:
        if pygame.sprite.spritecollide(selected_building, group_postroek, False) or pygame.sprite.spritecollide(
                selected_building, zhil_group, False):
            selected_building.kill()
            return
        for port in selected_building.set_ports():
            input_ports_group.add(port)
        group_postroek.add(selected_building)


def strelka_press(mouse_pos, strelki_group):
    if pygame.mouse.get_pressed()[0]:
        for i in strelki_group:
            if pygame.Rect.collidepoint(i.rect, mouse_pos):
                return i
    return False

def show_ports(postroiki, hud_goup):
    spisok_all = []
    for i in postroiki:
        cord = i.update(10)
        if len(cord) != 0:
            spisok_all.extend(cord)
    for cords in spisok_all:
        hud_goup.add(cords)



if __name__ == '__main__':
    menu()
