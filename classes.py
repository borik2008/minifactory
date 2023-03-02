from resources import *


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos, rotate_count=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rotate(rotate_count)
        self.rect.center = pos

    def set_img(self, image):
        self.image = image

    def rotate(self, rotate_count):
        self.image = pygame.transform.rotate(self.image, rotate_count * 90)
        self.rect = self.image.get_rect()


"""
класс жила 
id 1 = железная
id 2 = известняковая
id 3 = медная
"""


class Zhila(pygame.sprite.Sprite):
    def __init__(self, id, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = spisok_zhil_image[id - 1]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.id = id

    def set_pos(self, pos):
        self.rect.center = pos

    def get_id(self):
        return self.id

    def update(self, choice, smeshen_x=0, smeshen_y=0):
        if choice == 6:
            self.rect.x = self.rect.x + smeshen_x
            self.rect.y = self.rect.y + smeshen_y
        if choice == 7:
            return (self.rect.x, self.rect.y)


class Ikonka(pygame.sprite.Sprite):
    def __init__(self, image, pos, count, name, text_image=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.count = count
        self.name = name
        self.text_image = text_image

    def get_count(self):
        return self.count

    def update(self, choice):
        if choice == 1:
            return self.get_count()
        if choice == 2:
            return self.name
        if choice == 3:
            return self.text_image


"""
клсс постройка
id 10 = асемблер
id 11 = бур
id 12 = конструктор
id 13 = развзлетлитель
id 14 = соеденитель

self.orentation хранит целое число кол-во поворотов на 90% относительно исходного изобрпжения
"""


class Postroika(pygame.sprite.Sprite):
    def __init__(self, pos, count, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = spisok_postroiki_image[id - 10]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.count = count
        self.text_image = names_rescurces[id + 5]
        self.id = id
        self.na_zhile = 0
        self.napravlenie = 0
        self.cordinates_conveera = [0, 0]
        self.orentation = 0
        self.outputs_diraction = spisok_postroiki_outputs_diraction[id - 10]
        self.spisok_conveerov_up = None
        self.spisok_conveerov_right = None
        self.spisok_conveerov_down = None
        self.spisok_conveerov_left = None
        self.spisok_spiskov_conveera = [
            self.spisok_conveerov_left,
            self.spisok_conveerov_down,
            self.spisok_conveerov_right,
            self.spisok_conveerov_up]

    """
    napravlenie = 0 нет конвеера
    napravlenie = 1 конвеер вверх
    napravlenie = 2 конвеер в право
    napravlenie = 3 нонвеер налево
    napravlenie = 4 конвеер вниз
    """

    def get_conveer(self, diraction):
        if self.spisok_spiskov_conveera[diraction] == None:
            return None
        last_conveer = self.spisok_spiskov_conveera[diraction]
        while last_conveer.next != None:
            last_conveer = last_conveer.next
        return last_conveer

    def get_count(self):
        return self.count

    def get_size(self):
        sizey = (self.rect.bottomleft[1] - self.rect.y)
        sizex = (self.rect.topright[0] - self.rect.x)
        return (sizex, sizey)

    def update(self, choice, smeshen_x=0, smeshen_y=0):
        if choice == 1:
            return self.get_count()
        if choice == 2:
            return self.id
        if choice == 3:
            return self.text_image
        if choice == 4:
            sizex, sizey = self.get_size()
            return ((self.rect.x, self.rect.y), (sizex, sizey))
        if choice == 5:
            return self.na_zhile
        if choice == 6:
            self.rect.x = self.rect.x + smeshen_x
            self.rect.y = self.rect.y + smeshen_y
        if choice == 7:
            return (self.rect.x, self.rect.y)
        if choice == 8:
            return self.orentation
        if choice == 9:
            return self.outputs_diraction

    def get_id(self):
        return self.id

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.orentation += 1
        self.orentation = self.orentation % 4
        self.rect = self.image.get_rect()
        self.outputs_diraction = [self.outputs_diraction[-1]] + self.outputs_diraction[:-1]

    def set_na_zhile(self, na_zhile):
        self.na_zhile = na_zhile

    def get_pos(self):
        return self.rect.center

    def get_cordinates_for_conveer(self):
        return [[self.rect.left - 6, self.rect.center[1]], [self.rect.center[0], self.rect.bottom + 6],
                [self.rect.right + 6, self.rect.center[1]], [self.rect.center[0], self.rect.top - 6]]

    def add_new_conveer(self, strelka):
        conveer = Conveer(strelka.get_type(), self.get_cordinates_for_conveer()[strelka.get_direction()], strelka.get_direction())
        return conveer


class Ikonka_rescurces(pygame.sprite.Sprite):
    def __init__(self, pos, count, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = spisok_rescurces_img[id - 20]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.count = count
        self.text_image = names_rescurces[id - 20]
        self.id = id

    def get_count(self):
        return self.count

    def update(self, choice):
        if choice == 1:
            return self.get_count()
        if choice == 2:
            return self.id
        if choice == 3:
            return self.text_image

    def get_id(self):
        return self.id


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, id):
        pygame.sprite.Sprite.__init__(self)
        if id == 0:
            self.image = spisok_windows_image[0]
        elif 1 <= id <= 3:
            self.image = spisok_windows_image[1]
        elif id == 11:
            self.image = spisok_windows_image[2]
        else:
            self.image = spisok_windows_image[3]
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Strelki(pygame.sprite.Sprite):
    def __init__(self, pos, direction, type, postroika):
        pygame.sprite.Sprite.__init__(self)
        self.image = spisok_strelki_img[type]
        self.rect = self.image.get_rect()
        self.rotate(direction)
        self.direction = direction
        self.postroika = postroika
        self.type = type
        if (direction + 1) % 2 == 0:
            pos[1] = pos[1] + 120 - direction * 60
            pos[0] = pos[0] - 25 + 25 * type
        else:
            pos[0] = pos[0] - 60 + direction * 60
            pos[1] = pos[1] - 25 + 25 * type
        self.rect.center = pos
        if direction > 1:
            if type == 0:
                self.type = 2
            elif type == 2:
                self.type = 0

    def set_img(self, image):
        self.image = image

    def rotate(self, rotate_count):
        self.image = pygame.transform.rotate(self.image, rotate_count * 90)
        if rotate_count == 0:
            self.image = pygame.transform.flip(self.image, False, True)
        elif rotate_count == 1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

    def get_direction(self):
        return self.direction

    def get_type(self):
        return self.type

    def get_pos(self):
        return self.postroika.get_pos()


class Conveer(pygame.sprite.Sprite):
    def __init__(self, type, pos, diraction, previous=None, next=None):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.previous = previous
        self.next = next
        if type == 1:
            self.image = img_conveer_straight
            if diraction == 0 or diraction == 2:
                self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = img_conveer_corner
            if type == 0:
                if diraction == 2:
                    self.image = pygame.transform.rotate(self.image, -90)
                if diraction == 1:
                    self.image = pygame.transform.rotate(self.image, -180)
                if diraction == 0:
                    self.image = pygame.transform.rotate(self.image, -270)
            else:
                if diraction == 3:
                    self.image = pygame.transform.rotate(self.image, -90)
                if diraction == 2:
                    self.image = pygame.transform.rotate(self.image, -180)
                if diraction == 1:
                    self.image = pygame.transform.rotate(self.image, -270)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.diraction = diraction

    def rotate(self, rotate_count):
        self.image = pygame.transform.rotate(self.image, rotate_count * 90)

    def update(self, choice, smeshen_x=0, smeshen_y=0):
        if choice == 7:
            return (self.rect.x, self.rect.y)
        if choice == 6:
            self.rect.x = self.rect.x + smeshen_x
            self.rect.y = self.rect.y + smeshen_y
