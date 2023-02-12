import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


class Camera:

    def __init__(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)
        self.camera_move = self.camera_settings

    def update(self, hero):
        self.state = self.camera_move(self.state, hero.rect)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    @staticmethod
    def camera_settings(camera, hero_rect):
        _, _, w, h = camera
        x, y,_, _ = hero_rect

        x = -x + WIN_WIDTH / 2
        y = -y + WIN_HEIGHT / 2

        x = min(0, x)
        x = max((camera.width - WIN_WIDTH/2.5), x)

        y = min(0, y)
        y = max((camera.height - WIN_HEIGHT/2.5), y)

        return pygame.Rect(x, y, w, h)