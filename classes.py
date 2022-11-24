from resources import *

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def set_img(self, image):
        self.image = image

class Zhila(pygame.sprite.Sprite):
    def __init__(self, image_id, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = spisok_zhil_image[image_id]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_pos(self, pos):
        self.rect.center = pos

class Ikonka(pygame.sprite.Sprite):
    def __init__(self, image, pos, count, name, text_image = 0):
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
