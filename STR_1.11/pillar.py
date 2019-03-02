# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 03:37:37 2017

@author: aleks
"""

from pygame import *
import math



class Pillar(sprite.Sprite):
    
    def __init__(self, screen, center_x, bottom):
        sprite.Sprite.__init__(self)
        self.screen = screen
        self.count = 1000
        self.x = 0 
        self.y = 25       
        self.pillar_x = 0
        self.pillar_x0 = 0
        self.t0 = 0

    def update_watchup(self, global_time):        
        self.x = 25*math.cos(math.pi/2-math.pi/30*global_time)
        self.y = 25*math.sin(math.pi/2-math.pi/30*global_time)
        
    def update_watchdown(self,  rocket_speed, t, lors, NBOP, gamma):        
       x = 25*gamma*math.cos(math.pi/2-math.pi/30*t)
       y = 25*math.sin(math.pi/2-math.pi/30*t)
        
    def update_move(self,  rocket_speed, t, lors, NBOP, gamma):
        self.rect.centerx = self.count*lors -rocket_speed*(t-self.t0) - self.pillar_x0
        if self.rect.centerx <= 70:
            self.count += NBOP
        if self.rect.centerx >= 2000:
            self.count -= NBOP