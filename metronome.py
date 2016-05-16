#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import time
from datetime import datetime, timedelta

screen_width = 600 
screen_height = 200
cir_size = 80
left_end = cir_size + 20 
right_end = screen_width - cir_size - 20
cir_height = screen_height / 2
cir_pos = left_end
cir_dir = 0 #0が右
rect_width = right_end - left_end
rect_height = cir_size * 2
rect_pos = (left_end, cir_height - rect_height / 2)
white = (255, 255, 255)
gray = (100, 100, 100)
cir_color = white
countdown = 40
counttext = ""
mode = "normal"

#pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("metronome")
start_time = datetime.today()

while mode == "normal":
	d = datetime.today()
	if d > start_time + timedelta(microseconds = 750000):
		start_time += timedelta(microseconds = 750000)
		cir_dir = 1 - cir_dir

	s = (d - start_time).microseconds

	if cir_dir:
		cir_pos = right_end - (right_end - left_end) * s / 750000
	else:
		cir_pos = left_end + (right_end - left_end) * s / 750000

	screen.fill((0,0,0))
	pygame.draw.rect(screen, gray, Rect(rect_pos[0],rect_pos[1],rect_width,rect_height))
	pygame.draw.circle(screen, gray, (left_end, cir_height), cir_size)
	pygame.draw.circle(screen, gray, (right_end, cir_height), cir_size)
	pygame.draw.circle(screen, cir_color, (cir_pos, cir_height), cir_size)
	pygame.display.update()

fontsize = 80
myfont = pygame.font.Font("ipag.ttf", fontsize)#フォント
counttext = myfont.render(str(countdown), True, (0,0,0))

while mode == "count":
	d = datetime.today()
	if d > start_time + timedelta(microseconds = 750000):
		if countdown > 0:
			countdown -= 1
			counttext = myfont.render(str(countdown), True, (0,0,0))
		start_time += timedelta(microseconds = 750000)
		cir_dir = 1 - cir_dir

	s = (d - start_time).microseconds

	if cir_dir:
		cir_pos = right_end - (right_end - left_end) * s / 750000
	else:
		cir_pos = left_end + (right_end - left_end) * s / 750000

	screen.fill((0,0,0))
	pygame.draw.rect(screen, gray, Rect(rect_pos[0],rect_pos[1],rect_width,rect_height))
	pygame.draw.circle(screen, gray, (left_end, cir_height), cir_size)
	pygame.draw.circle(screen, gray, (right_end, cir_height), cir_size)
	pygame.draw.circle(screen, cir_color, (cir_pos, cir_height), cir_size)
	screen.blit(counttext, (cir_pos - fontsize / 4, cir_height - fontsize / 2))
	pygame.display.update()