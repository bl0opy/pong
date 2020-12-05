#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:03:08 2020

@author: ayan
"""


import pygame
from random import randint
import time
pygame.init()


# ---- SETTINGS ----
best_out_of = 10
vel = 15   
AJ = 1
g = 0
J = 550
threshold = 16
hitbox = 8
# ------------------

x = 850
x2 = 40
y = 350
y2 = 350
width = 20
height = 150
Cx = randint(300,600)
Cy = randint(200,400)
Cdim = 15
vectors = [randint(-4,4),randint(-4,4)]
points2 = 0
points1 = 0
size = (900,700)
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('freesansbold.ttf', 40)
win = pygame.display.set_mode(size=size)
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()

RUNNING, PAUSE, START = 0, 1, 2
state = START
Ptext = font.render('PAUSED', True, white, black) 
PtextRect = Ptext.get_rect()  
PtextRect.center = (450, 350)
Etext = font.render('GAME OVER', True, white, black) 
EtextRect = Etext.get_rect()  
EtextRect.center = (450, 350)
Stext = font.render('PONG', True, white, black) 
StextRect = Stext.get_rect()  
StextRect.center = (450, 350)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v: 
                state = PAUSE
            if event.key == pygame.K_b: 
                state = RUNNING
            if event.key == pygame.K_SPACE:
                state = RUNNING
    
    if state == RUNNING:
        
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_q] and y2 > vel:
            y2 -= vel
        if keys[pygame.K_a] and y2 < J - width - vel:
            y2 += vel
        
        if keys[pygame.K_o] and y > vel:
            y -= vel
        if keys[pygame.K_l] and y < J - width - vel:
            y += vel
        
        Pcenter1 = (x+(width//2),y+(height//2))
        Pcenter2 = (x2+(width//2),y2+(height//2))
        
        win.fill(black)
        
        
        if (abs(Cx-Pcenter1[0]) <= threshold and abs(Cy-Pcenter1[1]) <= threshold*hitbox) or (abs(Cx-Pcenter2[0]) <= threshold and abs(Cy-Pcenter2[1]) <= threshold*hitbox):
            vectors[0] = -vectors[0]
            # vectors[1] = randint(-8,8)
        if Cy < 25 or Cy > 675:
            vectors[1] = -vectors[1]
            # vectors[0] = randint(4, 8)
        if Cx < 25:
            points1 += 1
            Cx = randint(300,600)
            Cy = randint(200,400)
            time.sleep(0.5)
        if Cx > 875:
            points2 += 1
            Cx = randint(300,600)
            Cy = randint(200,400)
            time.sleep(0.5)
        if points1 == best_out_of or points2 == best_out_of:
            win.blit(Etext, EtextRect)
            pygame.time.delay(1000)
            run = False
        if points1 > g or points2 > g:
            AJ += 0.15
            vel -= 0.75
            g+=1
        
        Cx += AJ*vectors[0]
        Cy += AJ*vectors[1]
        
        text = font.render(f'{points2}', True, white, black) 
        textRect = text.get_rect()  
        textRect.center = (225, 25) 
        text2 = font.render(f'{points1}', True, white, black) 
        textRect2 = text.get_rect()  
        textRect2.center = (675, 25) 
        
        win.blit(text, textRect)
        win.blit(text2, textRect2)
        pygame.draw.circle(win, white, (Cx,Cy), Cdim)
        pygame.draw.rect(win, white, (x,y,width,height))
        pygame.draw.rect(win, white, (x2,y2,width,height))
        pygame.draw.line(win, white, (450,0), (450,700), 5)
        
    elif state == PAUSE:
        win.blit(Ptext, PtextRect)
    else:
        win.blit(Stext, StextRect)
        
    pygame.display.flip()
    clock.tick(60)




pygame.quit()

