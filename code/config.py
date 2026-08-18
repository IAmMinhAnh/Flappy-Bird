import pygame
import random
import sys

#SCREEN
WIDTH = 960
HEIGHT = 640

gravity = -20
fall = 25
jump = 20

#GROUND
ground_w = WIDTH
ground_h = 100

ground_x = 0
ground_y = HEIGHT - ground_h

#BIRD
bird_w = 34
bird_h = 24

bird_x = 200
bird_y = HEIGHT / 2

#PIPES
pipe_gap = 160
pipe_min_h = 100
pipe_max_h = 440 - ground_h 
pipe_w = 52

pipe_speed = 170
pipe_time = 1500

