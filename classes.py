from resources import *


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def set_img(self, image):
        self.image = image


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
        # не верно na_zhile в game.py
        if choice == 5:
            return self.na_zhile
        if choice == 6:
            self.rect.x = self.rect.x + smeshen_x
            self.rect.y = self.rect.y + smeshen_y
        if choice == 7:
            return (self.rect.x, self.rect.y)

    def get_id(self):
        return self.id

    def rotare(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

    def set_na_zhile(self, na_zhile):
        self.na_zhile = na_zhile



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
