from resources import *

class Kletka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

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

    def update(self, choice, smeshen_x=0, smeshen_y=0):
        if choice == 6:
            self.rect.x = self.rect.x + smeshen_x
            self.rect.y = self.rect.y + smeshen_y
        if choice == 7:
            return (self.rect.x, self.rect.y)


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
        self.spisok_spiskov_conveera = [None, None, None, None]
        self.is_posible_build_conveer = [True, True, True, True]
        self.input_ports = [True, True, True, True]
        self.resources = 0
        self.spisok_ports = []

    """
    napravlenie = 0 нет конвеера
    napravlenie = 1 конвеер вверх
    napravlenie = 2 конвеер в право
    napravlenie = 3 нонвеер налево
    napravlenie = 4 конвеер вниз

    direction = 0 конвеер влево
    direction = 1 конвеер вниз
    direction = 2 конвеер вправо
    direction = 3 нонвеер вверх
    """

    def generate_resources(self):
        if self.id == 11:
            self.resources = 1

    def send_resources(self):
        for port in self.spisok_spiskov_conveera:
            if port is not None:
                port.resieve_resources(self.resources)
                if self.resources != 0:
                    print("постройка отправил ресурс:", self.resources)
                self.resources = 0


    def resieve_resources(self, resources):
        self.resources += resources
        if resources != 0:
            print("постройка получил ресурс:", resources, "всего:", self.resources)

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
        if choice == 10:
            return self.get_ports()
        if choice == 11:
            self.send_resources()
        if choice == 12:
            self.generate_resources()

    def get_count(self):
        return self.count

    def get_size(self):
        sizey = (self.rect.bottomleft[1] - self.rect.y)
        sizex = (self.rect.topright[0] - self.rect.x)
        return (sizex, sizey)

    def get_id(self):
        return self.id

    def get_ports(self):
        ports = spisok_postroiki_input_ports[self.id - 10]
        if ports is not None:
            for i in ports[self.orentation]:
                self.spisok_ports.append(Port((i[0] + self.rect.center[0], i[1] + self.rect.center[1]), self))
        return self.spisok_ports

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

    def get_init_coord_for_conveer(self, direction, type):
        size = CONVEER_SIZE
        if type == 1:
            size /= 2
        cordinates_init_for_conveer = [[self.rect.left - size / 2, self.rect.center[1]],
                                       [self.rect.center[0], self.rect.bottom + size / 2],
                                       [self.rect.right + size / 2, self.rect.center[1]],
                                       [self.rect.center[0], self.rect.top - size / 2]]
        return cordinates_init_for_conveer[direction]

    def get_adit_coord_for_conveer(self, last_conveer, type):
        size = CONVEER_SIZE

        if last_conveer.get_type() == 1 and type == 1:
            size /= 2
        elif last_conveer.get_type() == 1 or type == 1:
            size = size / 2 + 8
        x = last_conveer.get_coord()[0]
        y = last_conveer.get_coord()[1]
        if last_conveer.get_output_diraction() == 0:
            x = x - size
        elif last_conveer.get_output_diraction() == 1:
            y = y + size
        elif last_conveer.get_output_diraction() == 2:
            x = x + size
        else:
            y = y - size
        return [x, y]

    def get_conveer(self, diraction):
        if self.spisok_spiskov_conveera[diraction] is None:
            return None
        last_conveer = self.spisok_spiskov_conveera[diraction]
        while last_conveer.get_next() is not None:
            last_conveer = last_conveer.get_next()
        return last_conveer

    def set_ports(self):
        ports = spisok_postroiki_input_ports[self.id - 10]
        if ports is not None:
            for i in ports[self.orentation]:
                self.spisok_ports.append(Port((i[0] + self.rect.center[0], i[1] + self.rect.center[1]), self))
        return self.spisok_ports


    def get_cordinates_for_conveer(self, direction, type):
        last_conveer = self.get_conveer(direction)

        if last_conveer is None:
            return self.get_init_coord_for_conveer(direction, type)
        if isinstance(last_conveer, Conveer):
            return self.get_adit_coord_for_conveer(last_conveer, type)
        return None


    def add_conveer_to_spisok(self, direction, conveer):
        last_conveer = self.get_conveer(direction)
        if last_conveer is None:
            self.spisok_spiskov_conveera[direction] = conveer
        else:
            last_conveer.next = conveer

    def add_new_conveer(self, strelka, objects, input_ports_group):
        direction = strelka.get_direction()
        if not self.is_posible_build_conveer[direction]:
            return None
        type = strelka.get_type()
        last_conveer = self.get_conveer(direction)
        coordinates = self.get_cordinates_for_conveer(direction, type)

        conveer = Conveer(type, coordinates, direction, last_conveer)
        if pygame.sprite.spritecollide(conveer, objects, False):
            conveer.kill()
            return None
        front_edge = conveer.get_coord()
        conveer_dir = conveer.get_output_diraction()
        size = CONVEER_SIZE / 2
        if conveer.type == 1:
            size = CONVEER_SIZE / 4

        if conveer_dir == 3:
            front_edge = front_edge[0], front_edge[1] - size
        if conveer_dir == 2:
            front_edge = front_edge[0] + size, front_edge[1]
        if conveer_dir == 1:
            front_edge = front_edge[0], front_edge[1] + size
        if conveer_dir == 0:
            front_edge = front_edge[0] - size, front_edge[1]

        for port in input_ports_group:
            if port.rect.collidepoint(front_edge):
                potrebitel = port.get_owner()
                conveer.next = potrebitel
                print("есть подкл")
                self.is_posible_build_conveer[direction] = False
        self.add_conveer_to_spisok(direction, conveer)

        return conveer


    def delit_conveer(self, strelka):
        dir = strelka.get_direction()
        conveer = self.spisok_spiskov_conveera[dir]
        while conveer is not None:
            kill_conveer = conveer
            conveer = conveer.get_next()
            kill_conveer.kill()
        self.spisok_spiskov_conveera[dir] = None

    def get_next(self):
        return None


class Port(pygame.sprite.Sprite):
    def __init__(self, pos, owner):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.owner = owner

    def get_owner(self):
        return self.owner




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
    def __init__(self, pos, direction, type, postroika, delit=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = spisok_strelki_img[type]
        self.rect = self.image.get_rect()
        self.rotate(direction)
        self.direction = direction
        self.postroika = postroika
        self.type = type
        if (direction + 1) % 2 == 0:
            pos[1] = pos[1] + 120 - direction * 60 - (direction // 3) * delit + (direction % 3) * delit
            pos[0] = pos[0] - 25 + 25 * type
        else:
            pos[0] = pos[0] - 60 - delit + direction * 60 + direction * delit
            pos[1] = pos[1] - 25 + 25 * type
        self.rect.center = pos
        if direction > 1:
            if type == 0:
                self.type = 2
            elif type == 2:
                self.type = 0
        if delit != 0:
            self.image = dell_img
            self.type = 4

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
    def __init__(self, type, pos, diraction, previous=None, template=False, next=None):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.id = 0
        self.previous = previous
        self.next = next
        if previous is not None:
            diraction = previous.get_output_diraction()
        if type == 1:
            self.image = img_conveer_straight
            if template:
                self.image = conveer_1_template_img
            self.output_diraction = diraction
            if diraction == 0 or diraction == 2:
                self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = img_conveer_corner
            if template:
                self.image = conveer_2_template_img
            if type == 0:
                if diraction == 2:
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.output_diraction = 1
                elif diraction == 1:
                    self.image = pygame.transform.rotate(self.image, -180)
                    self.output_diraction = 0
                elif diraction == 0:
                    self.image = pygame.transform.rotate(self.image, -270)
                    self.output_diraction = 3
                else:
                    self.output_diraction = 2
            else:
                if diraction == 3:
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.output_diraction = 0
                elif diraction == 2:
                    self.image = pygame.transform.rotate(self.image, -180)
                    self.output_diraction = 3
                elif diraction == 1:
                    self.image = pygame.transform.rotate(self.image, -270)
                    self.output_diraction = 2
                else:
                    self.output_diraction = 1
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.diraction = diraction
        self.resources = 0

    """
    direction = 0 конвеер влево
    direction = 1 конвеер вниз
    direction = 2 конвеер вправо
    direction = 3 нонвеер вверх

    type:
    0 - вправо
    1 - прямой
    2 - влево 
    """

    def get_coord(self):
        return self.rect.center

    def get_type(self):
        return self.type

    def get_output_diraction(self):
        return self.output_diraction

    def rotate(self, rotate_count):
        self.image = pygame.transform.rotate(self.image, rotate_count * 90)

    def update(self, choice, smeshen_x=0, smeshen_y=0):
        if choice == 7:
            return (self.rect.x, self.rect.y)
        if choice == 6:
            self.rect.x = self.rect.x + smeshen_x
            self.rect.y = self.rect.y + smeshen_y
        if choice == 10:
            return []
        if choice == 11:
            self.send_resources()

    def __str__(self):
        return "conveer количество ресурсов = " + str(self.resources)

    def send_resources(self):
        if self.next is not None:
            self.next.resieve_resources(self.resources)
            #print("отправил ресурс:", self.resources)
            self.resources = 0


    def resieve_resources(self, resources):
        self.resources = resources
        #print("конвеер получмл ресурс:", resources, "всего русурсов", self.resources)

    def get_next(self):
        return self.next