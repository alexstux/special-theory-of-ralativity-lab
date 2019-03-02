# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 23:48:37 2017

@author: aleks
"""

import pygame
import math

class Watch():
    
    def __init__(self, screen,center_x, center_y, filename):
        self.screen = screen
        #download image of rocket and create rectangle
        self.scale = 1
        self.img = pygame.image.load(filename)
        self.img = self.img.convert_alpha()
        self.img = pygame.transform.scale(self.img, (140, 168))
        self.rect = self.img.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.x = 0 
        self.y = 30
        
    def update(self ,t):
        self.x = 30*math.cos(math.pi/2-math.pi/30*t)
        self.y = 30*math.sin(math.pi/2-math.pi/30*t)
      
    def blitme(self, color):
        #draw watch in her position
        self.screen.blit(self.img, self.rect)
        pygame.draw.line(self.screen, color, (self.rect.centerx, self.rect.centery - 15), 
                        (self.rect.centerx + self.x, self.rect.centery - 15 - self.y), 3)
        