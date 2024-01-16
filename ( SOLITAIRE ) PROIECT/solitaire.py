import pygame
import random

"""--------------------------------Initializam libraria Pygame si setam dimensiunile ferestrei""" ""
pygame.init()
width, height = 1000, 600
pygame.display.set_caption("Solitaire")
window = pygame.display.set_mode((width, height))
background_color = (0, 128, 0)  # RGB value for dark green


pygame.display.flip()