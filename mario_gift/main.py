#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame

import cam
import level
import player

# Объявляем переменные
# TODO: продумать необходимые константы
TITLE = "МАРИО. ИЛИ ВЫЖИТЬ!"

BG_DIR = "levels/bg.gif"


def main():
    # TODO: реализовать работу приложения
    pygame.init()
    screen = pygame.display.set_mode(cam.DISPLAY)
    pygame.display.set_caption(TITLE)
    bg = pygame.image.load(BG_DIR)
    level1 = level.Level()
    level1.getPlatform()
    entities = pygame.sprite.Group()
    for pf in level1.platforms:
        entities.add(pf)
    hero = player.Player(55, 55)
    timer = pygame.time.Clock()
    entities.add(hero)
    main_camera = cam.Camera(len(level1.lines_of_level[0]),
                             len(level1.lines_of_level))

    anim_entities = pygame.sprite.Group()

    level1.get_pr(entities, anim_entities)
    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(1)
            if hero.winner:
                raise SystemExit(1)
            hero.move(event)

        screen.blit(bg, (0, 0))
        # entities.draw(screen)
        hero.update(level1.platforms)
        main_camera.update(hero)
        for e in entities:
            screen.blit(e.image, main_camera.apply(e))
        for e in anim_entities:
            screen.blit(e.image, main_camera.apply(e))


        pygame.display.update()


if __name__ == "__main__":
    main()
