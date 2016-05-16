#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import time
from datetime import datetime, timedelta

screen_width = 500
screen_height = 200
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("metronome_rect")
start_time = datetime.today()

count = 0
rect_color = white

while True:
	d = datetime.today()
	if d > start_time + timedelta(microseconds = 750000):
		if count == 0:
			rect_color = red
		else:
			rect_color = white
		count += 1
		if count == 4:
			count = 0
		start_time += timedelta(microseconds = 750000)

	s = (d - start_time).microseconds

	screen.fill(black)
	if s > 600000:
		pygame.draw.rect(screen, rect_color, Rect(0,0,screen_width,screen_height))

	pygame.display.update()