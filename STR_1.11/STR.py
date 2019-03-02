# -*- coding: utf-8 -*-

import pygame
import math
import time
import os

from rocket import Rocket
from watch  import Watch
from button import Start
from button import Stop
from button import Pause
from button import Scroll
from button import Change_velocity
from button import Galileo
from button import Ruseng

def run_game():
    '''initilize pygame'''
    pygame.init()
    
    '''settings of window'''
    video = pygame.display.Info() #объект с разрешением экрана
    # Set title of screen
    image_icon = pygame.image.load("icon.ico")
    pygame.display.set_caption("STR")
    pygame.display.set_icon(image_icon)

    WIDTH = video.current_w
    HEIGHT = video.current_h
    
    if video.current_w < 1600:
        WIDTH = 1200
        HEIGHT = 900
        
    if video.current_w == 1440:
        WIDTH = 1440
        HEIGHT = 900
        
    if video.current_w >= 1600:
        WIDTH = 1600
        HEIGHT = 900
           
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN) #Инициализация окна
    screen_rect = screen.get_rect()  #координаты экрана 
    s = pygame.Surface((WIDTH,HEIGHT))  # the size of your rect
    s.set_alpha(230)                # alpha level
    s.fill((0,0,0))           # this fills the entire surface

    
    '''Constants and verables, flags and constants - big words'''
    global_time = 0.0 #счетчик времени
    if WIDTH == 1440 or WIDTH == 1600: 
        GLOBAL_L = 340  #длина ракеты расстояние между столбами в покое
    if WIDTH == 1200:
        GLOBAL_L = 256
    alpha = 0 # относительная скорость
    GLOBAL_C = 400 # скорость света
    frame_count = 0 #счетчик фреймов
    
    if WIDTH == 1600: 
        border = 70    #граница окон в пикселях
        
    if WIDTH == 1440 or WIDTH == 1200:
        border = 30

    '''Флаги'''
    RUSENG = True         #изменение языка
    GALILEO = True        #преобразования галилео
    DONE = False          #флаг главного цикла
    MOUSE_KLICK = False   #обработка клика мышкой
    LEFT_KLICK = False
    RIGHT_KLICK = False
    MENU = True           #флаг меню
    INSTRUCTION = False
    AUTORS = False
    
    mouse_x = 0 
    mouse_y = 0 
    
    frame_rate = 0.0    

    frame1_ind = 0                 

    frame1_rocket_length = 340     #length of moving rocket

    RED =   (255,  0,  0)
    WHITE = (255,255,255)
    BLACK = (0  ,  0,  0)
    
    #Background and menu
    gerb = pygame.image.load('images/Gerb_MGTU_imeni_Baumana.png')
    gerb = pygame.transform.scale(gerb, (170, 200))
    gerb = gerb.convert_alpha()
    
    selph = pygame.image.load('images/logo.png')
    selph = pygame.transform.scale(selph, (368, 200))
    selph = selph.convert_alpha()
    
    if WIDTH==1440 or WIDTH==1200:
        background = pygame.image.load('images/background_1440.png')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background = background.convert_alpha()
    
        background2 = pygame.image.load('images/background2_1440.png')
        background2 = pygame.transform.scale(background2, (WIDTH, HEIGHT))
        background2 = background2.convert()

    if WIDTH == 1600:
        background = pygame.image.load('images/background.png')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background = background.convert_alpha()
        
        background2 = pygame.image.load('images/background2.png')
        background2 = pygame.transform.scale(background2, (WIDTH, HEIGHT))
        background2 = background2.convert()
    
    back_menu = pygame.image.load('images/menu.jpg')
    back_menu = pygame.transform.scale(back_menu, (WIDTH, HEIGHT))
    back_menu = back_menu.convert()
    
    back_left = pygame.image.load('images/background_left.png')
    back_left = pygame.transform.scale(back_left, (30, HEIGHT))
    back_left = back_left.convert_alpha()
    
    back_centr = pygame.image.load('images/background_centr.png')
    back_centr = pygame.transform.scale(back_centr, (770, HEIGHT))
    back_centr = back_centr.convert_alpha()
    
    back_right = pygame.image.load('images/background_right.png')
    back_right = pygame.transform.scale(back_right, (400, HEIGHT))
    back_right = back_right.convert_alpha()
    
    '''шрифты'''
    font_1 = pygame.font.SysFont("arial", 18, bold=True)
    font_2 = pygame.font.Font('fonts\courbd.ttf', 19)
    font_3 = pygame.font.Font('fonts\mpus.ttf', 22)
    font_4 = pygame.font.Font('fonts\courierstd-bold.otf', 22)
    font_5 = pygame.font.Font('fonts\mpus.ttf', 56)

    
    def text_1(Ttext, Tcolor, Tlocation):
        text = font_1.render(Ttext, True, Tcolor)
        screen.blit(text, Tlocation)
    
    def text_2(Ttext, Tcolor, Tlocation):
        text = font_2.render(Ttext, True, Tcolor)
        screen.blit(text, Tlocation)

    def text_3(Ttext, Tcolor, Tlocation):
        text = font_3.render(Ttext, True, Tcolor)
        screen.blit(text, Tlocation)
        
    def text_4(Ttext, Tcolor, Tlocation):
        text = font_4.render(Ttext, True, Tcolor)
        screen.blit(text, Tlocation)
        
    def text_5(Ttext, Tcolor, Tlocation):
        text = font_5.render(Ttext, True, Tcolor)
        screen.blit(text, Tlocation)
    
    '''buttons from module button, arrows '''
    if WIDTH == 1600:
        bt_1 = Change_velocity(screen , 1135, 270, 'images/speed_change.png','', (200, 100)) #ползунок
        bt_start = Start(screen ,1200 ,420 , 'images/start.png','images/start_light.png', (140, 50))
        bt_pause = Pause(screen ,1350 ,420 , 'images/pause.png','images/pause_light.png', (140, 50))
        bt_stop  =  Stop(screen ,1500 ,420 , 'images/stop.png','images/stop_light.png',   (140, 50))
        bt_left  = Scroll(screen ,1295 ,490 , 'images/bt_scroll_left_light.png','images/bt_scroll_left.png',    (100, 60))
        bt_right = Scroll(screen ,1405 ,490 , 'images/bt_scroll_right_light.png','images/bt_scroll_right.png',  (100, 60))
        bt_galileo = Galileo(screen ,1350 ,790 , 'images/Galileo_off.png','images/Galileo_on.png',  (360, 50))
        bt_ruseng = Ruseng(screen ,WIDTH - 100,HEIGHT - 50, 'images/ruseng.png','images/ruseng2.png',  (50, 25))
        
    if WIDTH == 1440 or WIDTH == 1200:
        bt_1 = Change_velocity(screen , WIDTH-350, 270, 'images/speed_change.png','', (200, 100)) #ползунок
        bt_start = Start(screen ,WIDTH-305 , 420 , 'images/start.png','images/start_light.png', (120, 40))
        bt_pause = Pause(screen ,WIDTH-185 , 420 , 'images/pause.png','images/pause_light.png', (120, 40))
        bt_stop  =  Stop(screen ,WIDTH-65 , 420 , 'images/stop.png','images/stop_light.png',   (120, 40))
        bt_left  = Scroll(screen ,WIDTH-240 , 490 , 'images/bt_scroll_left_light.png','images/bt_scroll_left.png',    (100, 60))
        bt_right = Scroll(screen ,WIDTH-130 , 490 , 'images/bt_scroll_right_light.png','images/bt_scroll_right.png',  (100, 60))
        bt_galileo = Galileo(screen ,WIDTH-190, 790 , 'images/Galileo_off.png','images/Galileo_on.png',  (360, 50))
        bt_ruseng = Ruseng(screen ,WIDTH - 100, HEIGHT - 50, 'images/ruseng.png','images/ruseng2.png',  (50, 25))
        
    '''create objects'''
    #function of pillars-----------------------------------------------------------------
    img_pillar = pygame.image.load('images/pillar3.png')
    img_pillar = pygame.transform.scale(img_pillar, (102, 192))
    img_pillar = img_pillar.convert_alpha()
    img_pillar_2 = img_pillar
    
    rect_pillar = img_pillar.get_rect() #rectangle of image of pillar
    rect_pillar.bottom = 870
    rect_pillar.centerx = 0
    x = 0 #coordinate arrow of pillar watches
    y = 0
    
    def img_load(beta, img_pillar, img_pillar_2):
        scale = 1/beta
        img_pillar = img_pillar_2
        img_pillar = pygame.transform.scale(img_pillar, (int(102/scale), 192))
        rect = img_pillar.get_rect()
        rect.bottom = 870
        return(img_pillar, rect)
        
    def update_watchup(global_time):        
        x = 25*math.cos(math.pi/2-math.pi/30*global_time)
        y = 25*math.sin(math.pi/2-math.pi/30*global_time)
        return(x,y)
        
    def update_watchdown(t, beta):        
       x = 25*beta*math.cos(math.pi/2-math.pi/30*t)
       y = 25*math.sin(math.pi/2-math.pi/30*t)
       return(x,y)
       
    def blitme_pillar(screen, color, img, rect, x, y):
        screen.blit(img, rect)
        pygame.draw.line(screen, color, (rect.centerx,rect.bottom -143), 
                 (rect.centerx + x, rect.bottom -143 - y), 2)
    #--------------------------------------------------------------------------------------------
    
    
    
    if WIDTH==1600:
        watch1 = Watch(screen, 1200, 150, 'images/watch.png') #часы
        watch2 = Watch(screen, 1350, 150, 'images/watch.png')
        watch3 = Watch(screen, 1500, 150, 'images/watch.png')
        watch4 = Watch(screen, 1200, 670, 'images/watch.png')
        watch5 = Watch(screen, 1350, 670, 'images/watch.png')
        watch6 = Watch(screen, 1500, 670, 'images/watch.png')
    
    if WIDTH == 1440 or WIDTH == 1200:
        watch1 = Watch(screen, WIDTH-315, 150, 'images/watch_1440.png') #часы
        watch2 = Watch(screen, WIDTH-190, 150, 'images/watch_1440.png')
        watch3 = Watch(screen, WIDTH- 65, 150, 'images/watch_1440.png')
        watch4 = Watch(screen, WIDTH-315, 670, 'images/watch_1440.png')
        watch5 = Watch(screen, WIDTH-190, 670, 'images/watch_1440.png')
        watch6 = Watch(screen, WIDTH- 65, 670, 'images/watch_1440.png')        
            
    
    rocket_1 = Rocket(screen, border + 1.5*GLOBAL_L, 150, GLOBAL_L) #ракеты
    rocket_2 = Rocket(screen, border + 1.5*GLOBAL_L, 580, GLOBAL_L)
    
    #watches icons----------------------------------------
    img_watchpick = pygame.image.load('images/watchpick.png')
    img_watchpick = pygame.transform.scale(img_watchpick, (20, 20))
    img_watchpick = img_watchpick.convert_alpha()
    img_watchpick2 = img_watchpick
    rect_icon = img_watchpick.get_rect()

    def img_load_icons(beta, img_watchpick, img_watchpick2):
        scale = 1/beta
        img_watchpick = img_watchpick2
        img_watchpick = pygame.transform.scale(img_watchpick, (int(20/scale), 20))
        rect = img_watchpick.get_rect()
        rect.centery = 150
        return(img_watchpick, rect)
    #-----------------------------------------------------------
    img_a = pygame.image.load('images/A.png')
    img_a = pygame.transform.scale(img_a, (40, 40))
    img_a = img_a.convert_alpha()
    
    img_b = pygame.image.load('images/B.png')
    img_b = pygame.transform.scale(img_b, (40, 40))
    img_b = img_b.convert_alpha()
    
    img_c = pygame.image.load('images/C.png')
    img_c = pygame.transform.scale(img_c, (40, 40))
    img_c = img_c.convert_alpha()
    
    
    
    '''timers'''
    clock = pygame.time.Clock()
    timer = pygame.time.Clock()
    timer.tick()
    
    '''function str watch timers'''
    def time_to_string(x):
        if x < 0:
            x += 60*60
        return str(math.floor(x/60)*10+1001)[1:3]+':'+str(math.floor(x%60)*10+1001)[1:3]+':'+str((x-math.floor(x))*1000+1001)[1:3]   
    
    # -------- Main Program Loop -----------
    screen.blit(s, (0,0))
    screen.blit(gerb, (screen_rect.centerx-300, screen_rect.centery-100))
    screen.blit(selph, (screen_rect.centerx, screen_rect.centery-100))
    pygame.display.flip()
    time.sleep(1.5)
    while not DONE:
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        
        '''Events'''
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                DONE = True  # Flag that we are done so we exit this loop 
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    MENU = True
                    global_time = 0.0 
                    rocket_1.global_rocket_x = 0.0
                    rocket_1.global_rocket_x_start = 0
                    rocket_1.global_rocket_t_start = 0
                    bt_pause.pause = True
                    alpha = 0
                    bt_1.bt1_x = bt_1.rect.left
                    rocket_1.img_load()
                    rocket_1.firestop = False
                    rocket_2.firestop = False
                    AUTORS = False
                    
                if event.key == pygame.K_RIGHT:
                    RIGHT_KLICK = True
                    
                if event.key == pygame.K_LEFT:
                    LEFT_KLICK = True
      
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    RIGHT_KLICK = False
                    
                if event.key == pygame.K_LEFT:
                    LEFT_KLICK = False
                    
                if event.key == pygame.K_SPACE:
                    bt_pause.pause = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                MOUSE_KLICK = True
                
            elif event.type == pygame.MOUSEBUTTONUP:
                MOUSE_KLICK = False
            

                
                    
        
                
        
        '''Logic'''
        if not MENU:
            #преобразования галилео
            if bt_galileo.flag:
                GALILEO = True
            else:
                GALILEO = False
            
            frame_count += 1 
            frame_rate = clock.get_time()
            
            # множитель лоренцевых преобразований
            beta = math.sqrt(1 - alpha*alpha)
            
            #////////////////////////////////////////////////////////////////#
                #buttons           
            if bt_pause.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_pause.pause = True
            else:
                rocket_1.firestop = True
                rocket_2.firestop = True
                
            if bt_pause.pause:
                frame_rate = 0
                rocket_1.firestop = False
                rocket_2.firestop = False
                
            if bt_left.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True and bt_pause.pause:
                if global_time > 0:
                    rocket_1.firestop = True
                    rocket_2.firestop = True
                    global_time -= 0.01/(alpha+0.01)
                else:
                    global_time = 0
                    
            if LEFT_KLICK and bt_pause.pause:
                if global_time > 0:
                    rocket_1.firestop = True
                    rocket_2.firestop = True
                    global_time -= 0.0025/(alpha+0.01)
                else:
                    global_time = 0
                    
            if bt_right.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True and bt_pause.pause:
                rocket_1.firestop = True
                rocket_2.firestop = True
                global_time += 0.01/(alpha+0.01)
                
            if RIGHT_KLICK and bt_pause.pause:
                rocket_1.firestop = True
                rocket_2.firestop = True
                global_time += 0.0025/(alpha+0.01)

            
            if bt_start.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_pause.pause = False
                if alpha == 0:
                    alpha = 0.05
                rocket_1.firestop = True
                rocket_2.firestop = True
                
            if bt_1.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True and global_time == 0:
                    bt_1.bt1_x = mouse_x-10
                    frame_rate = 0
                    if  (mouse_x - bt_1.rect.left)/200 > 0.98:
                        alpha = 0.98 
                    else:
                        alpha = ((mouse_x - bt_1.rect.left)/200)
                        rocket_1.img_load()
                        rocket_1.global_rocket_t_start = global_time
                        rocket_1.global_rocket_x_start = rocket_1.global_rocket_x
                    if WIDTH < 1600 and (mouse_x - bt_1.rect.left)/200 > 0.965:
                        alpha = 0.965
                
            if bt_stop.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                rocket_1.global_rocket_x_start = 0
                rocket_1.global_rocket_t_start = 0
                global_time = 0
                bt_pause.pause = True
                alpha = 0
                bt_1.bt1_x = bt_1.rect.left
                rocket_1.img_load()
                rocket_1.firestop = False
                rocket_2.firestop = False
                
            if bt_galileo.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True and bt_galileo.clickflag == True:
                bt_galileo.click()
                rocket_1.img_load()
            else:
                rocket_1.img_load()
                bt_galileo.clickflag == True
                
            if MOUSE_KLICK == False:
                bt_galileo.clickflag = True
                
            #//////////////////////////////////////////////////////////////// 
            # --- Timer going up ---
            # Calculate total seconds
            if frame_rate != 0:
                # global time
                global_time += frame_rate /1000
                
            frame1_rocket_time1 = global_time*beta + alpha*GLOBAL_L*0.5/GLOBAL_C
            frame1_rocket_time2 = global_time*beta
            frame1_rocket_time3 = global_time*beta - alpha*GLOBAL_L*0.5/GLOBAL_C
            
                #rocket_1 scale with alpha
            if not GALILEO:
                rocket_1.Lx_scale(alpha, 150, GLOBAL_L)
            else:
                rocket_1.Lx_scale(0, 150, GLOBAL_L)
            
                #rocket_1 move
            rocket_1.update(alpha, GLOBAL_C, GLOBAL_L, frame1_rocket_length, global_time, frame1_ind, border)
            frame1_ind = math.floor((rocket_1.global_rocket_x + 2*GLOBAL_L)/(4*GLOBAL_L))
            
                #length_of_rocket scale with alpha
            frame1_rocket_length = beta*GLOBAL_L
            
            #update watches
            if not GALILEO:
                watch1.update(frame1_rocket_time1)
                watch2.update(frame1_rocket_time2)
                watch3.update(frame1_rocket_time3)
                watch4.update(global_time)
                watch5.update(global_time)
                watch6.update(global_time)
            else:
                watch1.update(global_time)
                watch2.update(global_time)
                watch3.update(global_time)
                watch4.update(global_time)
                watch5.update(global_time)
                watch6.update(global_time)

        #кнопка переключения языка
        else:
            if bt_ruseng.flag == True:
                RUSENG = True
            else:
                RUSENG = False
            
            if bt_ruseng.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True and bt_ruseng.clickflag == True:
                bt_ruseng.click()
            else:
                bt_ruseng.clickflag == True
                
            if MOUSE_KLICK == False:
                bt_ruseng.clickflag = True
        #*****************************************************************
        #/////////////////////////////////////////////////////////////////
        #*****************************************************************
        '''Draw all'''
        if not MENU:
            screen.blit(background2, screen_rect)

            rocket_1.blitme(frame_count)
            rocket_2.blitme(frame_count)
            if not GALILEO:
                pygame.draw.line(screen, (231, 115, 38), (rocket_1.rect.centerx- 0.5*beta*GLOBAL_L, rocket_1.rect.centery - 60), 
                                (rocket_1.rect.centerx - 0.5*beta*GLOBAL_L, rocket_1.rect.centery))
                pygame.draw.line(screen, (37, 153, 42), (rocket_1.rect.centerx, rocket_1.rect.centery - 60), 
                                (rocket_1.rect.centerx, rocket_1.rect.centery))
                pygame.draw.line(screen, (39, 37, 153), (rocket_1.rect.centerx+ 0.5*beta*GLOBAL_L, rocket_1.rect.centery - 60), 
                                (rocket_1.rect.centerx + 0.5*beta*GLOBAL_L, rocket_1.rect.centery))
            else:
                pygame.draw.line(screen, (231, 115, 38), (rocket_1.rect.centerx- 0.5*GLOBAL_L, rocket_1.rect.centery - 60), 
                                (rocket_1.rect.centerx - 0.5*GLOBAL_L, rocket_1.rect.centery))
                pygame.draw.line(screen, (37, 153, 42), (rocket_1.rect.centerx, rocket_1.rect.centery - 60), 
                                (rocket_1.rect.centerx, rocket_1.rect.centery))
                pygame.draw.line(screen, (39, 37, 153), (rocket_1.rect.centerx+ 0.5*GLOBAL_L, rocket_1.rect.centery - 60), 
                                (rocket_1.rect.centerx + 0.5*GLOBAL_L, rocket_1.rect.centery))
            
            pygame.draw.line(screen, (231, 115, 38), (rocket_2.rect.centerx- 0.5*GLOBAL_L, rocket_2.rect.centery - 60), 
                            (rocket_2.rect.centerx - 0.5*GLOBAL_L, rocket_2.rect.centery))
            pygame.draw.line(screen, (37, 153, 42), (rocket_2.rect.centerx, rocket_2.rect.centery - 60), 
                            (rocket_2.rect.centerx, rocket_2.rect.centery))
            pygame.draw.line(screen, (39, 37, 153), (rocket_2.rect.centerx+ 0.5*GLOBAL_L, rocket_2.rect.centery - 60), 
                            (rocket_2.rect.centerx + 0.5*GLOBAL_L, rocket_2.rect.centery))
            
            #watch icons
            #----------------------------------------------------------------------------------------------------
            screen.blit(img_watchpick2, (rocket_2.rect.centerx - 10, rocket_2.rect.centery - 10))
            screen.blit(img_watchpick2, (rocket_2.rect.centerx - 10 - 0.5*GLOBAL_L, rocket_2.rect.centery - 10))
            screen.blit(img_watchpick2, (rocket_2.rect.centerx - 10 + 0.5*GLOBAL_L, rocket_2.rect.centery - 10))
            if not GALILEO:
                img_watchpick, rect_icon = img_load_icons(beta, img_watchpick, img_watchpick2)
                rect_icon.centerx = rocket_1.rect.centerx
                screen.blit(img_watchpick, rect_icon)
                
                rect_icon.centerx = rocket_1.rect.centerx - 0.5*beta*GLOBAL_L
                screen.blit(img_watchpick, rect_icon)
                
                rect_icon.centerx = rocket_1.rect.centerx + 0.5*beta*GLOBAL_L
                screen.blit(img_watchpick, rect_icon)
                
                screen.blit(img_b, (rocket_1.rect.centerx - 20, rocket_1.rect.centery - 100))
                screen.blit(img_a, (rocket_1.rect.centerx - 20 - 0.5*beta*GLOBAL_L, rocket_1.rect.centery - 100))
                screen.blit(img_c, (rocket_1.rect.centerx - 20 + 0.5*beta*GLOBAL_L, rocket_1.rect.centery - 100))
            else:
                img_watchpick, rect_icon = img_load_icons(1, img_watchpick, img_watchpick2)
                rect_icon.centerx = rocket_1.rect.centerx
                screen.blit(img_watchpick, rect_icon)
                
                rect_icon.centerx = rocket_1.rect.centerx - 0.5*GLOBAL_L
                screen.blit(img_watchpick, rect_icon)
                
                rect_icon.centerx = rocket_1.rect.centerx + 0.5*GLOBAL_L
                screen.blit(img_watchpick, rect_icon)
                
                screen.blit(img_b, (rocket_1.rect.centerx - 20, rocket_1.rect.centery - 100))
                screen.blit(img_a, (rocket_1.rect.centerx - 20 - 0.5*GLOBAL_L, rocket_1.rect.centery - 100))
                screen.blit(img_c, (rocket_1.rect.centerx - 20 + 0.5*GLOBAL_L, rocket_1.rect.centery - 100))
            
            screen.blit(img_b, (rocket_2.rect.centerx - 20, rocket_2.rect.centery - 100))
            screen.blit(img_a, (rocket_2.rect.centerx - 20 - 0.5*GLOBAL_L, rocket_2.rect.centery - 100))
            screen.blit(img_c, (rocket_2.rect.centerx - 20 + 0.5*GLOBAL_L, rocket_2.rect.centery - 100))
            #----------------------------------------------------------------------------------------------------

                        #pillar update and draw
            frame1_pillar1_ind = (frame1_ind)*4 
            frame1_pillar2_ind = (frame1_ind)*4 + 1
            frame1_pillar3_ind = (frame1_ind)*4 + 2
                
            x, y = update_watchup(global_time)
            blitme_pillar(screen, BLACK, img_pillar_2, pygame.Rect(border-51 + GLOBAL_L/2, 248, 102, 192), x, y)
            blitme_pillar(screen, BLACK, img_pillar_2, pygame.Rect(border-51 + 1.5*GLOBAL_L, 248, 102, 192), x, y)
            blitme_pillar(screen, BLACK, img_pillar_2, pygame.Rect(border-51 + 2.5*GLOBAL_L, 248, 102, 192), x, y)
            
            text_1(str(frame1_pillar1_ind%100), BLACK,(border-6 + GLOBAL_L/2, 206))
            text_1(str(frame1_pillar2_ind%100), BLACK,(border-6 + 1.5*GLOBAL_L, 206))
            text_1(str(frame1_pillar3_ind%100), BLACK,(border-6 + 2.5*GLOBAL_L, 206))
            
            str_time = time_to_string(global_time)
            text_1('['+ str_time + ']', BLACK,(border-33 + GLOBAL_L/2, 225))
            text_1('['+ str_time + ']', BLACK,(border-33 + 1.5*GLOBAL_L, 225))
            text_1('['+ str_time + ']', BLACK,(border-33 + 2.5*GLOBAL_L, 225))
                
            if not GALILEO:
                a = math.ceil((-2*GLOBAL_L+alpha*GLOBAL_C*global_time)/beta/GLOBAL_L) #index of pillar
                b = math.floor((2*GLOBAL_L+alpha*GLOBAL_C*global_time)/beta/GLOBAL_L+1)
                img_pillar, rect_pillar = img_load(beta, img_pillar, img_pillar_2)
                
                for ind in range(a, b+1):
                    frame2_pillar_x = beta*(ind-1)*GLOBAL_L-GLOBAL_C*alpha*global_time + 1.5*GLOBAL_L + border
                    frame2_pillar_time = beta*global_time + alpha*GLOBAL_L/GLOBAL_C*(ind - 1)
                    rect_pillar.centerx = frame2_pillar_x
                    x, y = update_watchdown(frame2_pillar_time, beta)
                    blitme_pillar(screen, BLACK, img_pillar, rect_pillar, x, y)
                    text_1(str(ind%1000), BLACK,(rect_pillar.centerx - 6, 636))
                    str_time = time_to_string(frame2_pillar_time)
                    text_1('[' + str_time + ']', BLACK,(rect_pillar.centerx - 33, 655))
            else:
                a = math.ceil((-2*GLOBAL_L+alpha*GLOBAL_C*global_time)/GLOBAL_L) #index of pillar
                b = math.floor((2*GLOBAL_L+alpha*GLOBAL_C*global_time)/GLOBAL_L+1)
                img_pillar, rect_pillar = img_load(1, img_pillar, img_pillar_2)
                
                for ind in range(a, b+1):
                    frame2_pillar_x = (ind-1)*GLOBAL_L-GLOBAL_C*alpha*global_time + 1.5*GLOBAL_L + border
                    frame2_pillar_time = global_time
                    rect_pillar.centerx = frame2_pillar_x
                    x, y = update_watchdown(frame2_pillar_time, beta)
                    blitme_pillar(screen, BLACK, img_pillar, rect_pillar, x, y)
                    text_1(str(ind%1000), BLACK,(rect_pillar.centerx - 6, 636))
                    str_time = time_to_string(frame2_pillar_time)
                    text_1('[' + str_time + ']', BLACK,(rect_pillar.centerx - 33, 655))
                
            #--------------------------------------------------------------------------- 
             
            if WIDTH != 1200:
                screen.blit(background, screen_rect)
            else:
                screen.blit(back_left, (0,0))
                screen.blit(back_centr, (30, 0))
                screen.blit(back_right, (800,0))

            bt_1.blitme()
            if bt_start.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_start.blitme()
            else:
                bt_start.blitmeclick()
                
            if bt_pause.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_pause.blitmeclick()
            else:
                bt_pause.blitme()
            
            if bt_stop.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_stop.blitme()
            else:
                bt_stop.blitmeclick()
                
            if bt_left.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_left.blitme()
            else:
                bt_left.blitmeclick()
                
            if bt_right.rect.collidepoint(mouse_pos) and MOUSE_KLICK == True:
                bt_right.blitme()
            else:
                bt_right.blitmeclick()
                
            if not bt_galileo.flag:
                bt_galileo.blitme()
            else:
                bt_galileo.blitmeclick()
            
            
            watch1.blitme(BLACK)
            watch2.blitme(BLACK)
            watch3.blitme(BLACK)
            watch4.blitme(BLACK)
            watch5.blitme(BLACK)
            watch6.blitme(BLACK)

            #watches text
            if not GALILEO:
                screen.blit(img_a, (watch1.rect.centerx - 20, watch1.rect.centery - 130))
                str_time = time_to_string(frame1_rocket_time1)
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch1.rect.centerx - 43, watch1.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:    
                    text_2(str_time, BLACK, (watch1.rect.centerx - 43, watch1.rect.centery +  48))
                    
                screen.blit(img_b, (watch2.rect.centerx - 20, watch2.rect.centery - 130))
                str_time = time_to_string(frame1_rocket_time2)
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch2.rect.centerx - 43, watch2.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:   
                    text_2(str_time, BLACK, (watch2.rect.centerx - 43, watch2.rect.centery +  48))
                    
                screen.blit(img_c, (watch3.rect.centerx - 20, watch3.rect.centery - 130))
                str_time = time_to_string(frame1_rocket_time3)
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch3.rect.centerx - 43, watch3.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:  
                    text_2(str_time, BLACK, (watch3.rect.centerx - 43, watch3.rect.centery +  48))
                    
                screen.blit(img_a, (watch4.rect.centerx - 20, watch4.rect.centery - 130))
                str_time = time_to_string(global_time)
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch4.rect.centerx - 43, watch4.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch4.rect.centerx - 43, watch4.rect.centery +  48))
                    
                screen.blit(img_b, (watch5.rect.centerx - 20, watch5.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch5.rect.centerx - 43, watch5.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch5.rect.centerx - 43, watch5.rect.centery +  48))
                    
                screen.blit(img_c, (watch6.rect.centerx - 20, watch6.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch6.rect.centerx - 43, watch6.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch6.rect.centerx - 43, watch6.rect.centery +  48))
                    
            else:
                screen.blit(img_a, (watch1.rect.centerx - 20, watch1.rect.centery - 130))
                str_time = time_to_string(global_time)
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch1.rect.centerx - 43, watch1.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch1.rect.centerx - 43, watch1.rect.centery +  48))
                
                screen.blit(img_b, (watch2.rect.centerx - 20, watch2.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch2.rect.centerx - 43, watch2.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch2.rect.centerx - 43, watch2.rect.centery +  48))
                    
                screen.blit(img_c, (watch3.rect.centerx - 20, watch3.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch3.rect.centerx - 43, watch3.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch3.rect.centerx - 43, watch3.rect.centery +  48))
                    
                screen.blit(img_a, (watch4.rect.centerx - 20, watch4.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch4.rect.centerx - 43, watch4.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:
                    text_2(str_time, BLACK, (watch4.rect.centerx - 43, watch4.rect.centery +  48))
                    
                screen.blit(img_b, (watch5.rect.centerx - 20, watch5.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch5.rect.centerx - 43, watch5.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:    
                    text_2(str_time, BLACK, (watch5.rect.centerx - 43, watch5.rect.centery +  48))
                    
                screen.blit(img_c, (watch6.rect.centerx - 20, watch6.rect.centery - 130))
                if WIDTH==1600:
                    text_2(str_time, BLACK, (watch6.rect.centerx - 43, watch6.rect.centery +  53))
                if WIDTH==1440 or WIDTH==1200:    
                    text_2(str_time, BLACK, (watch6.rect.centerx - 43, watch6.rect.centery +  48))
                    
            #текст на кнопках
            if RUSENG:
                text_4("START", BLACK, (bt_start.rect.centerx-30, bt_start.rect.centery-7))
                text_4("PAUSE", BLACK, (bt_pause.rect.centerx-30, bt_pause.rect.centery-7))
                text_4("STOP", BLACK, (bt_stop.rect.centerx-30, bt_stop.rect.centery-7))
                text_2("Galilean", BLACK, (bt_galileo.rect.centerx-168, bt_galileo.rect.centery-18))
                text_2("Transformation", BLACK, (bt_galileo.rect.centerx-168, bt_galileo.rect.centery +3))
                text_2("Lorentz", BLACK, (bt_galileo.rect.centerx + 15, bt_galileo.rect.centery-18))
                text_2("Transformation", BLACK, (bt_galileo.rect.centerx + 15, bt_galileo.rect.centery +3))
            else:
                text_2("СТАРТ", BLACK, (bt_start.rect.centerx-30, bt_start.rect.centery-10))
                text_2("ПАУЗА", BLACK, (bt_pause.rect.centerx-30, bt_pause.rect.centery-10))
                text_2("СТОП", BLACK, (bt_stop.rect.centerx-25, bt_stop.rect.centery-10))
                text_2("Трансформация", BLACK, (bt_galileo.rect.centerx - 165, bt_galileo.rect.centery-18))
                text_2("Галилея", BLACK, (bt_galileo.rect.centerx - 165, bt_galileo.rect.centery))
                text_2("Трансформация", BLACK, (bt_galileo.rect.centerx + 15, bt_galileo.rect.centery-18))
                text_2("Лоренца", BLACK, (bt_galileo.rect.centerx + 15, bt_galileo.rect.centery))
                
                    
            #text
            if RUSENG:
                if WIDTH == 1600:
                    text_4("Velocity:",          BLACK, (1370, 270))
                    text_4(str(round(alpha, 3)), BLACK, (1370, 310))
                    text_4("of light speed",     BLACK, (1370, 350))
                    
                if WIDTH==1440 or WIDTH==1200:
                    text_4("Velocity:",          BLACK, (WIDTH-140, 270))
                    text_4(str(round(alpha, 3)), BLACK, (WIDTH-140, 310))
                    text_4("of light",           BLACK, (WIDTH-140, 350))
            else:
                if WIDTH == 1600:
                    text_1("Скорость:",          BLACK, (1370, 270))
                    text_1(str(round(alpha, 3)), BLACK, (1370, 310))
                    text_1("скорости света",     BLACK, (1370, 350))
                    
                if WIDTH==1440 or WIDTH==1200:
                    text_1("Скорость:",          BLACK, (WIDTH-140, 270))
                    text_1(str(round(alpha, 3)), BLACK, (WIDTH-140, 310))
                    text_1("скорости света",     BLACK, (WIDTH-140, 350))
                
                    
        else:
            screen.blit(back_menu, screen_rect)
            if INSTRUCTION:
                os.startfile(r'STR_laba.pdf')
                INSTRUCTION = False
                
            if RUSENG:
                text_5("New experiment", BLACK,(WIDTH-498,282))
                text_5("New experiment", WHITE,(WIDTH-500,280))
                if mouse_x >= WIDTH-500 and mouse_x <= 1400 and mouse_y >= 280 and mouse_y <= 350:
                    text_5("New experiment", RED,(WIDTH-500,280))
                    if MOUSE_KLICK:
                        MENU = False
                
                text_5("Instruction", BLACK,(WIDTH-498,382))
                text_5("Instruction", WHITE,(WIDTH-500,380))
                if mouse_x >= WIDTH-500 and mouse_x <= 1400 and mouse_y >= 380 and mouse_y <= 450:
                    text_5("Instruction", RED,(WIDTH-500,380))
                    if MOUSE_KLICK:
                        INSTRUCTION = True
                
                text_5("Autors", BLACK,(WIDTH-498,482))
                text_5("Autors", WHITE,(WIDTH-500,480))
                if mouse_x >= WIDTH-500 and mouse_x <= 1400 and mouse_y >= 480 and mouse_y <= 550:
                    text_5("Autors", RED,(WIDTH-500,480))
                    if MOUSE_KLICK:
                        AUTORS = True
                    
                text_5("Quit", BLACK,(WIDTH-498,582))
                text_5("Quit", WHITE,(WIDTH-500,580))
                if mouse_x >= WIDTH-500 and mouse_x <= 1400 and mouse_y >= 580 and mouse_y <= 650:
                    text_5("Quit", RED,(WIDTH-500,580))
                    if MOUSE_KLICK:
                        DONE = True
            else:
                text_5("Новый эксперимент", BLACK,(WIDTH-548,282))
                text_5("Новый эксперимент", WHITE,(WIDTH-550,280))
                if mouse_x >= WIDTH-500 and mouse_x <= 1400 and mouse_y >= 280 and mouse_y <= 350:
                    text_5("Новый эксперимент", RED,(WIDTH-550,280))
                    if MOUSE_KLICK:
                        MENU = False
                
                text_5("Инструкция", BLACK,(WIDTH-548,382))
                text_5("Инструкция", WHITE,(WIDTH-550,380))
                if mouse_x >= WIDTH-550 and mouse_x <= 1400 and mouse_y >= 380 and mouse_y <= 450:
                    text_5("Инструкция", RED,(WIDTH-550,380))
                    if MOUSE_KLICK:
                        INSTRUCTION = True
                
                text_5("Авторы", BLACK,(WIDTH-548,482))
                text_5("Авторы", WHITE,(WIDTH-550,480))
                if mouse_x >= WIDTH-550 and mouse_x <= 1400 and mouse_y >= 480 and mouse_y <= 550:
                    text_5("Авторы", RED,(WIDTH-550,480))
                    if MOUSE_KLICK:
                        AUTORS = True
                    
                text_5("Выход", BLACK,(WIDTH-548,582))
                text_5("Выход", WHITE,(WIDTH-550,580))
                if mouse_x >= WIDTH-550 and mouse_x <= 1400 and mouse_y >= 580 and mouse_y <= 650:
                    text_5("Выход", RED,(WIDTH-550,580))
                    if MOUSE_KLICK:
                        DONE = True
                    
            if bt_ruseng.flag:
                bt_ruseng.blitme()
            else:
                bt_ruseng.blitmeclick()
                
            text_1("РУС", BLACK,(bt_ruseng.rect.centerx-55,bt_ruseng.rect.centery-10))
            text_1("ENG", BLACK,(bt_ruseng.rect.centerx+30,bt_ruseng.rect.centery-10))
            if bt_ruseng.rect.collidepoint(mouse_pos):
                text_1("РУС", RED,(bt_ruseng.rect.centerx-55,bt_ruseng.rect.centery-10))
                text_1("ENG", RED,(bt_ruseng.rect.centerx+30,bt_ruseng.rect.centery-10))

            if AUTORS:
                screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
                if not RUSENG:
                    text_1("Программирование", WHITE, (screen_rect.centerx-50,screen_rect.centery-150))
                    text_3("Кашников Александр МГТУ им. Н.Э. Баумана", WHITE, (screen_rect.centerx-150, screen_rect.centery-120))
                    text_3("Киктенко Евгений МГТУ им. Н.Э. Баумана", WHITE, (screen_rect.centerx-150, screen_rect.centery-90))
                    text_1("Расчеты", WHITE, (screen_rect.centerx-50, screen_rect.centery-60))
                    text_3("Киктенко Евгений", WHITE, (screen_rect.centerx-150, screen_rect.centery-30))
                    text_3("Кашников Александр", WHITE, (screen_rect.centerx-150, screen_rect.centery))
                    text_3("Гусманова Анастасия МГТУ им. Н.Э. Баумана", WHITE, (screen_rect.centerx-150, screen_rect.centery+30))
                    text_1("Графика", WHITE, (screen_rect.centerx-50, screen_rect.centery+60))
                    text_3("Кашников Александр", WHITE, (screen_rect.centerx-150, screen_rect.centery+90))
                else:
                    text_1("programming", WHITE, (screen_rect.centerx-50,screen_rect.centery-150))
                    text_3("Kashnikov Alexander BMSTU", WHITE, (screen_rect.centerx-150, screen_rect.centery-120))
                    text_3("Kiktenko Evgeniy BMSTU", WHITE, (screen_rect.centerx-150, screen_rect.centery-90))
                    text_1("Calculations", WHITE, (screen_rect.centerx-50, screen_rect.centery-60))
                    text_3("Kiktenko Evgeniy", WHITE, (screen_rect.centerx-150, screen_rect.centery-30))
                    text_3("Kashnikov Alexander", WHITE, (screen_rect.centerx-150, screen_rect.centery))
                    text_3("Gusmanova Anastasiya BMSTU", WHITE, (screen_rect.centerx-150, screen_rect.centery+30))
                    text_1("Design", WHITE, (screen_rect.centerx-50, screen_rect.centery+60))
                    text_3("Kashnikov Alexander", WHITE, (screen_rect.centerx-150, screen_rect.centery+90))
                
                
        clock.tick(60)
        '''Go ahead and update the screen with what we've drawn.'''
        pygame.display.flip()

run_game()
pygame.quit()
    
