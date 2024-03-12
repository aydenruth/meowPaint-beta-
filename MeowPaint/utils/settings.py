import pygame
pygame.init()#starts pygame
pygame.font.init()#starts pygame fonts

WHITE = (255,255,255)#rgb vals and constant var
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN =(0, 0, 255)

FPS = 30
WIDTH, HEIGHT = 600, 700 #declare mutiple vars on one line? canvas will be sq w a 100px toolbar


ROWS = COLS = 50 #think snake grid( u should make this higher res somehow)

TOOLBAR_HEIGHT = HEIGHT - WIDTH#remeber hardcoding is bad

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE #add a canvas color changer

DRAW_GRID_LINES = False

def get_font(size):
    return pygame.font.SysFont("comicsnas", size) 
#define a func get_font, returns a font w a specific size