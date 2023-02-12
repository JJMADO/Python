#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import pygame
import pyganim as pyganim

import platform

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 1
ANIMATION_RIGHT = ("levels/r1.png", "levels/r2.png",
                   "levels/r3.png", "levels/r4.png", "levels/r5.png")
ANIMATION_LEFT = ("levels/l1.png", "levels/l2.png",
                  "levels/l3.png", "levels/l4.png", "levels/l5.png")
ANIMATION_JUMP = ("levels/j.png", ANIMATION_DELAY)
ANIMATION_JUMP_LEFT = ("levels/jl.png", ANIMATION_DELAY)
ANIMATION_JUMP_RIGHT = ("levels/jr.png", ANIMATION_DELAY)
ANIMATION_STAY = ("levels/0.png", ANIMATION_DELAY)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.winner = False
        # скорость перемещения. 0 - стоять на месте
        self.xvel = 0
        # скорость вертикального перемещения
        self.yvel = 0
        # Начальная позиция Х
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        # self.image.fill(pygame.Color(COLOR))
        self.image.set_colorkey(pygame.Color(COLOR))
        anim = []
        for a in ANIMATION_RIGHT:
            anim.append((a, ANIMATION_DELAY))
        self.anim_right = pyganim.PygAnimation(anim)
        self.anim_right.play()
        anim = []
        for a in ANIMATION_LEFT:
            anim.append((a, ANIMATION_DELAY))
        self.anim_left = pyganim.PygAnimation(anim)
        self.anim_left.play()

        self.anim_jump = pyganim.PygAnimation([ANIMATION_JUMP])
        self.anim_jump.play()

        self.anim_jump_left = pyganim.PygAnimation([ANIMATION_JUMP_LEFT])
        self.anim_jump_left.play()

        self.anim_jump_right = pyganim.PygAnimation([ANIMATION_JUMP_RIGHT])
        self.anim_jump_right.play()

        self.anim_stay = pyganim.PygAnimation([ANIMATION_STAY])
        self.anim_stay.play()
        self.anim_stay.blit(self.image, (0, 0))

        # прямоугольный объект
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.left = False
        self.right = False
        self.up = False
        self.onGround = False  # На земле ли я?

    def update(self, platforms):
        if self.left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            if self.up and not self.onGround:
                self.anim_jump_left.blit(self.image, (0, 0))
            else:
                self.anim_left.blit(self.image, (0, 0))

        if self.right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            if self.up and not self.onGround:
                self.anim_jump_right.blit(self.image, (0, 0))
            else:
                self.anim_right.blit(self.image, (0, 0))

        # стоим, когда нет указаний идти
        if not (self.left or self.right):
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.anim_stay.blit(self.image, (0, 0))

        if self.up:
            # прыгаем, только когда можем оттолкнуться от земли
            if self.onGround:
                self.yvel = -JUMP_POWER
            if not self.left and not self.right:
                self.image.fill(pygame.Color(COLOR))
                self.anim_jump.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        # Мы не знаем, когда мы на земле
        self.onGround = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, platform.BlockDie):
                    self.die()

                if isinstance(p, platform.Teleport):
                    self.teleporting(random.randint(55, 745),
                                     random.randint(55, 745))

                if isinstance(p, platform.Princess):
                    self.winner = True

                if xvel > 0:  # если движется вправо
                    # то не движется вправо
                    self.rect.right = p.rect.left

                if xvel < 0:  # если движется влево
                    # то не движется влево
                    self.rect.left = p.rect.right

                if yvel > 0:  # если падает вниз
                    # то не падает вниз
                    self.rect.bottom = p.rect.top
                    # и становится на что-то твердое
                    self.onGround = True
                    # и энергия падения пропадает
                    self.yvel = 0

                if yvel < 0:  # если движется вверх
                    # то не движется вверх
                    self.rect.top = p.rect.bottom
                    # и энергия прыжка пропадает
                    self.yvel = 0

    def move(self, event):
        # TODO: реализовать обработку событий
        if event.type == pygame.KEYDOWN and \
                (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
            self.right = True
        if event.type == pygame.KEYUP and \
                (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
            self.right = False
        if event.type == pygame.KEYDOWN and \
                (event.key == pygame.K_a or event.key == pygame.K_LEFT):
            self.left = True
        if event.type == pygame.KEYUP and \
                (event.key == pygame.K_a or event.key == pygame.K_LEFT):
            self.left = False
        if event.type == pygame.KEYDOWN \
                and (event.key == pygame.K_w or event.key == pygame.K_SPACE):
            self.up = True
        if event.type == pygame.KEYUP \
                and (event.key == pygame.K_w or event.key == pygame.K_SPACE):
            self.up = False

    def die(self):
        pygame.time.wait(500)
        self.teleporting(55, 55)

    def teleporting(self, x, y):
        self.rect.x = x
        self.rect.y = y
