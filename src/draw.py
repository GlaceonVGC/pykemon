import pygame
import color

fgc = color.BLACK
bgc = color.WHITE

def FGC(color: color.Color) -> color.Color:
    return fgc if color is None else color

def BGC(color: color.Color) -> color.Color:
    return bgc if color is None else color

def set_colors(*colors: tuple) -> None:
    global fgc, bgc
    fgc, bgc = colors
