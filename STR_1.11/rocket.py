# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 18:18:03 2017

@author: aleks
"""
import pygame
import math

class Rocket():
    
    def __init__(self, screen, center_x, center_y, global_l):
        self.screen = screen
        #download image of rocket and create rectangle
        self.scale = 1
        
        self.img_rocket = pygame.image.load('images/rocket.png')
        self.img_rocket = pygame.transform.scale(self.img_rocket, (int(global_l/self.scale), int(global_l*0.411)))
        self.img_rocket = self.img_rocket.convert_alpha()
        self.img1 = self.img_rocket
        
        self.fire1 = pygame.image.load('images/fire1.png')
        self.fire1 = self.fire1.convert_alpha()
        self.img2 = self.fire1
        self.fire2 = pygame.image.load('images/fire2.png')
        self.fire2 = self.fire2.convert_alpha()
        self.img3 = self.fire2
        self.fire3 = pygame.image.load('images/fire3.png')
        self.fire3 = self.fire3.convert_alpha()
        self.img4 = self.fire3
        self.rect_fire = self.fire1.get_rect()
        
        self.rect = self.img_rocket.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.k = 1
        self.global_rocket_x = 0
        self.global_rocket_x_start = 0
        self.global_rocket_t_start = 0
        self.firestop = True

    def blitme(self,frame_count):
        #draw rocket in her position
        self.screen.blit(self.img_rocket, (self.rect))
        
        if self.firestop == True:
            if frame_count%3 == 0:
                self.screen.blit(self.fire1, (self.rect.left - self.rect_fire.right + 3, self.rect.centery - 35))
                self.screen.blit(self.fire2, (self.rect.left - self.rect_fire.right + 3, self.rect.centery - 10))
            elif frame_count%3 == 1:
                self.screen.blit(self.fire2, (self.rect.left - self.rect_fire.right + 3, self.rect.centery - 35))
                self.screen.blit(self.fire3, (self.rect.left - self.rect_fire.right + 3, self.rect.centery - 10))
            elif frame_count%3 == 2:
                self.screen.blit(self.fire3, (self.rect.left - self.rect_fire.right + 3, self.rect.centery - 35))
                self.screen.blit(self.fire1, (self.rect.left - self.rect_fire.right + 3, self.rect.centery - 10))
            
    def update(self, alpha, global_c, global_l,frame1_rocket_length, t, frame1_ind, border):
        self.global_rocket_x = self.global_rocket_x_start + t*alpha*global_c #coordinate of midle rocket 
        self.rect.centerx = self.global_rocket_x - (frame1_ind*4 - 1.5)*global_l + border #coordinate of left rocket in up frame
       
    def Lx_scale(self, alpha, center_y, global_l):
        self.k = math.sqrt(1-alpha*alpha)
        self.scale = 1/self.k
        self.img_rocket = pygame.transform.scale(self.img_rocket, (int(global_l/self.scale), int(global_l*0.411)))
        self.rect = self.img_rocket.get_rect()
        self.rect_fire = self.fire1.get_rect()
        self.rect.centery = center_y
    
    def img_load(self):
        self.img_rocket = self.img1
        self.fire1 = self.img2
        self.fire2 = self.img3
        self.fire3 = self.img4
        self.fire1 = pygame.transform.scale(self.fire1, (int(100//self.scale), 50))
        self.fire2 = pygame.transform.scale(self.fire2, (int(100//self.scale), 50))
        self.fire3 = pygame.transform.scale(self.fire3, (int(100//self.scale), 50))