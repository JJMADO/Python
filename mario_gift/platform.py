import pygame
import pyganim

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника
ANIMATION_TELEPORT = ["levels/portal1.png,"
                      "portal2.png"]
ANIMATION_DELAY = 1
ANIMATION_PR = ["levels/princess_l.png,"
                "levels/princess_r.png"]


class Platform(pygame.sprite.Sprite):
    # TODO: реализовать класс для платформ

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH,
                                     PLATFORM_HEIGHT))
        # self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("levels/platform.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("levels/dieBlock.png")


class Teleport(Platform):

    def __init__(self, x, y, dx, dy):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

        anim = []
        for a in ANIMATION_TELEPORT:
            anim.append((a, ANIMATION_DELAY))

        self.Anim = pyganim.PygAnimation(anim)
        self.Anim.play()
        self.image.fill(pygame.color("#7686ff"))
        self.Anim.blit(self.image, (0, 0))

    def update(self):
        self.image.fill(pygame.color("#7686ff"))
        self.Anim.blit(self.image, (0, 0))


class Princess(Platform):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image.set_colorkey(pygame.Color(PLATFORM_COLOR))
        anim = []
        for a in ANIMATION_PR:
            anim.append((a, ANIMATION_DELAY))

        self.AnimPr = pyganim.PygAnimation(anim)
        self.AnimPr.play()
        self.AnimPr.blit(self.image, (0, 0))

    def update(self):
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.AnimPr.blit(self.image, (0, 0))
