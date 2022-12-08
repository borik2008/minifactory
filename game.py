import time

from classes import *
import sys
import random


WIDTH = 1920
HEIGHT = 1080
MUSIC_VOLUME = 0


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mini Factory")

#Функция описываюшея работу меню настроек
def settings():
    #подключаем глобальную переменнаю по уровню громкости музыки
    global MUSIC_VOLUME
    #создаём спрайты интерфейса управления данного меню
    sound_off_btn = Button(btn_sound_off_img, (WIDTH / 2, HEIGHT / 2 + 200))
    sound_minus_btn = Button(btn_sound_minus_img, (WIDTH / 2 - 100, HEIGHT / 2 + 70))
    sound_plus_btn = Button(btn_sound_plus_img, (WIDTH / 2 + 100, HEIGHT / 2 + 70))
    back_to_menu_btn = Button(btn_back_img, (WIDTH / 2, HEIGHT / 2 - 100))
    number = Button(numbers_image_for_sound[int(MUSIC_VOLUME * 10)], (WIDTH / 2, HEIGHT / 2 + 70))
    #создаём группу для всех элементов управления
    buttons = pygame.sprite.Group()
    buttons.add(sound_off_btn, sound_minus_btn, sound_plus_btn, back_to_menu_btn, number)
    while True:
        #отслеживаем нажатые пользователем клавиши
        for event in pygame.event.get():
            #обрабатываем случай если пользователь нажал ESC, вызываем меню подтвержения(выходим/остаёмся)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        sys.exit()
            #обрабатываем случай если пользователь нажал лкм
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #если пользаватель нажал назад то возвзращаемся назад
                if back_to_menu_btn.rect.collidepoint(mouse_pos):
                    return
                #если пользователь нажал прибавить громкость то увеличиваем громкость и меняем изображения громкости
                if sound_plus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME < 1:
                        MUSIC_VOLUME += 0.1
                        number.set_img(numbers_image_for_sound[int(round(MUSIC_VOLUME * 10))])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                #если пользователь нажал уменьшить громкость то уменьшаем громкость и меняем изображения громкости
                if sound_minus_btn.rect.collidepoint(mouse_pos):
                    if MUSIC_VOLUME > 0:
                        MUSIC_VOLUME -= 0.1
                        number.set_img(numbers_image_for_sound[int(round(MUSIC_VOLUME * 10))])
                        pygame.mixer.music.set_volume(MUSIC_VOLUME)
                #если пользователь нажал отключить громкость то отключаем громкость и меняем изображения громкости
                if sound_off_btn.rect.collidepoint(mouse_pos):
                    pygame.mixer.music.set_volume(0)
                    number.set_img(numbers_image_for_sound[0])
                    MUSIC_VOLUME = 0

        # перекрываем поверх всех элементов фоновое изображение
        screen.blit(fon_image, fon_image.get_rect())
        #отрисовываем кнопки на экране
        buttons.draw(screen)
        #обновляем сформировонаё изображение экрана
        pygame.display.flip()


def confrim():
    #создаём спрайты
    yes_btn = Button(btn_yes_img, (WIDTH / 2 + 100, HEIGHT / 2))
    no_btn = Button(btn_no_img, (WIDTH / 2 - 100, HEIGHT / 2))
    #создаём группу спрайтов
    buttons = pygame.sprite.Group()
    buttons.add(yes_btn, no_btn)
    # формируем изображения подтвержения
    screen.blit(fon_image, fon_image.get_rect())
    buttons.draw(screen)
    pygame.display.flip()
    while True:
        #проверяем нажал ли пользователь на (yes/no) и выходим из функции
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
    #создаём спрайты
    start_btn = Button(btn_start_img, (WIDTH / 2, HEIGHT / 2 - 100))
    settings_btn = Button(btn_settings_img, (WIDTH / 2, HEIGHT / 2 + 100))
    quit_btn = Button(btn_quit_img, (WIDTH / 2, HEIGHT / 2 + 200))
    #создаём группу для спрайтов
    buttons = pygame.sprite.Group()
    buttons.add(start_btn, settings_btn, quit_btn)
    while True:
        for event in pygame.event.get():
            #проверяем надал ли пользователь лкм
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #если пользователь нажал настройки то открывается меню настроек
                if settings_btn.rect.collidepoint(mouse_pos):
                    settings()
                #если пользователь нажал выход то открывается меню подтверждения выхода из игры
                if quit_btn.rect.collidepoint(mouse_pos):
                    if confrim() == 1:
                        sys.exit()
                #если пользователь нажал старт то открываается игра
                if start_btn.rect.collidepoint(mouse_pos):
                    game()

        #формируем изображение меню
        screen.blit(fon_image, fon_image.get_rect())
        buttons.draw(screen)
        pygame.display.flip()




def game():
    #создаём группу спрайтов
    allSpites = pygame.sprite.Group()

    #создаём сетку размером 115 на 115 для размещения жил
    setka_zhil = [0] * 9
    for i in range(9):
        setka_zhil[i] = [0] * 16

    #создаём сетку размером 10 на 10 для резмещения построек
    setkap = [0] * (192 * 2)
    for i in range(192 * 2):
        setkap[i] = [0] * (109 * 2)

    # размещение жил по сетке
    for i in range(0, 3):
        numbers = 0
        while True:
            num1 = random.randint(1, 8)
            num2 = random.randint(0, 15)
            if setka_zhil[num1][num2] == 0:
                zhila = Zhila(i + 1, (num2 * 115, num1 * 115))
                setka_zhil[num1][num2] = zhila.get_id()
                numbers += 1
                allSpites.add(zhila)
                for q in range(0, 115, 5):
                    for g in range(0, 115, 5):
                        setkap[(num2 * 115 + g) // 5][(num1 * 115 + q) // 5] = zhila.get_id()
            if numbers == 3:
                break

    #создаём спрайты построек, интерфейса
    ikonka_count_resources_001 = Button(numbers_image[0], (WIDTH / 2 - 400, 70))
    ikonka_count_resources_010 = Button(numbers_image[0], (WIDTH / 2 - 420, 70))
    ikonka_count_resources_100 = Button(numbers_image[0], (WIDTH / 2 - 440, 70))
    ikonki = pygame.sprite.Group()
    postroiki = pygame.sprite.Group()
    for i in range(15):
        ikonka_rescurces = Ikonka_rescurces((WIDTH / 2 - 350 + i * 50, 70), 10, i + 20)
        ikonki.add(ikonka_rescurces)
    for i in range(5):
        ikonka_postroek = Postroika((WIDTH / 2 - 200 + i * 100, HEIGHT - 70), 1, 10 + i, 0)
        ikonki.add(ikonka_postroek)
        postroiki.add(ikonka_postroek)
    ikonka_name = Button(names_rescurces[0], (WIDTH / 2 - 630, 70))

    hud_up = Button(hud_up_img, (WIDTH / 2, HEIGHT / 2))
    hud_down = Button(hud_down_img, (WIDTH / 2, HEIGHT / 2))
    group_setka = pygame.sprite.Group()
    group_postroek = pygame.sprite.Group()
    # добовляем в группы спрайтов спрайты
    allSpites.add(hud_up, hud_down, ikonka_count_resources_001, ikonka_count_resources_010, ikonka_count_resources_100, ikonka_name)
    # создаём переменнаю для проверки привязанна ли расположение постройки к расположению мышки
    captured = False
    for i in range(192 * 2):
        for n in range(108 * 2):
            group_setka.add(Block((i * 5, n * 5), setkap[i][n]))
    timer = time.time()
    while True:
        screen.blit(fon_game_img, fon_game_img.get_rect())
        if time.time() - timer > 5:
            for i in group_setka:
                i.kill()
            for i in range(192 * 2):
                for n in range(108 * 2):
                    group_setka.add(Block((i * 5, n * 5), setkap[i][n]))
            timer = time.time()
        #отображаем кол-во ресурсов для предмета на который мы навелись
        mouse_pos = pygame.mouse.get_pos()
        for i in ikonki:
            if pygame.Rect.collidepoint(i.rect, mouse_pos):
                ikonka_name.set_img(i.update(3))
                ikonka_count_resources_001.set_img(numbers_image[i.update(1) % 10])
                ikonka_count_resources_010.set_img(numbers_image[i.update(1) % 100 // 10])
                ikonka_count_resources_100.set_img(numbers_image[i.update(1) // 100])
        #проверяем нажата ли какая нибудь кнопка
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] and captured:
                selected_building.rotare()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
                for i in group_postroek:
                    if pygame.Rect.collidepoint(i.rect, mouse_pos):
                        pos, size = i.update(4)
                        new_id = i.update(5)

                        # текущую ячеку помечаем что там чисто
                        setkap[pos[0] // 5][pos[1] // 5] = 0
                        for q in range(0, size[1], 5):
                            for g in range(0, size[0], 5):
                                # каждую явейку затрагиваемая обектом помечаем как свободную
                                setkap[(pos[0] // 5 * 5 + g) // 5][(pos[1] // 5 * 5 + q) // 5] = new_id

                        i.kill()
            #если пользователь нажал клавишу мышки
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                #создаём спрайт постройки исли пользователь выбрал одну из них
                for i in postroiki:
                    if pygame.Rect.collidepoint(i.rect, mouse_pos):
                        selected_building = Postroika(mouse_pos, 1, i.update(2), setkap[mouse_pos[0] // 5][mouse_pos[1] // 5])
                        captured = True
                        allSpites.add(selected_building)
                        group_postroek.add(selected_building)

            #если клавиша мышки отпущена после нажатия и до этого была выбрана постройка для размещения
            #пытаемся разместить обекто по сетке
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == False and captured:
                captured = False
                #вычисляем размер поcтройки
                sizex, sizey = selected_building.get_size()
                #проверяем ечейку которая соответстует укрсору мышки свободна или нет
                # если ячека занята то is_place_occupied становится true
                is_place_occupied = False
                print(selected_building.get_id())
                print(setkap[mouse_pos[0] // 5][mouse_pos[1] // 5])
                if selected_building.get_id() == 11 and 0 < setkap[mouse_pos[0] // 5][mouse_pos[1] // 5] < 4:
                    #создаём два цикла для проверки размера постройки в той ячейке которую она займёт
                    for q in range(0, sizey, 5):
                        for g in range(0, sizex, 5):
                            #получаем кординаты ячейки постройки
                            numm1 = (mouse_pos[1] // 5 * 5 + q) // 5
                            numm2 = (mouse_pos[0] // 5 * 5 + g) // 5
                            #проверяем пуста ли эта ячейка и если занята то selected_building.kill()
                            if numm1 > 108 * 2 or numm2 > 191 * 2 or setkap[numm2][numm1] > 3 or setkap[numm2][numm1] < 1:
                                is_place_occupied = True
                    if is_place_occupied:
                        selected_building.kill()
                    else:
                        #текущую ячеку помечаем что что-то там есть
                        setkap[mouse_pos[0] // 5][mouse_pos[1] // 5] = selected_building.get_id()
                        #изменяем позицию размещяемого обекта в соответстии с сеткой
                        selected_building.rect.x = mouse_pos[0] // 5 * 5
                        selected_building.rect.y = mouse_pos[1] // 5 * 5
                        for q in range(0, sizey, 5):
                            for g in range(0, sizex, 5):
                                #каждую явейку затрагиваемая обектом помечаем что как занята
                                setkap[(mouse_pos[0] // 5 * 5 + g) // 5][(mouse_pos[1] // 5 * 5 + q) // 5] = selected_building.get_id()

                elif setkap[mouse_pos[0] // 5][mouse_pos[1] // 5] == 0 and selected_building.get_id() != 11:
                    for q in range(0, sizey, 5):
                        for g in range(0, sizex, 5):
                            numm1 = (mouse_pos[1] // 5 * 5 + q) // 5
                            numm2 = (mouse_pos[0] // 5 * 5 + g) // 5
                            if numm1 > 108 * 2 or numm2 > 191 * 2 or setkap[numm2][numm1] != 0:
                                is_place_occupied = True
                    if is_place_occupied:
                        selected_building.kill()
                    else:
                        #текущую ячеку помечаем что что-то там есть
                        setkap[mouse_pos[0] // 5][mouse_pos[1] // 5] = selected_building.get_id()
                        #изменяем позицию размещяемого обекта в соответстии с сеткой
                        selected_building.rect.x = mouse_pos[0] // 5 * 5
                        selected_building.rect.y = mouse_pos[1] // 5 * 5
                        for q in range(0, sizey, 5):
                            for g in range(0, sizex, 5):
                                #каждую явейку затрагиваемая обектом помечаем что как занята
                                setkap[(mouse_pos[0] // 5 * 5 + g) // 5][(mouse_pos[1] // 5 * 5 + q) // 5] = selected_building.get_id()
                else:
                    selected_building.kill()

            #когда пользователь нажмёт ESC то появится окно (yes/no) для выхода
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if confrim() == 1:
                        return 0
        #в кординаты выбранной постройки передаём mouse_pos
        if 'selected_building' in locals() and captured:
            selected_building.rect.x = mouse_pos[0]
            selected_building.rect.y = mouse_pos[1]

        # формируем изображение игры
        allSpites.draw(screen)
        group_setka.draw(screen)
        ikonki.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    menu()
