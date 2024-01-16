import pygame
import random

"""--------------------------------Initializam libraria Pygame si setam dimensiunile ferestrei""" ""
pygame.init()
width, height = 1000, 600
pygame.display.set_caption("Solitaire")
window = pygame.display.set_mode((width, height))
background_color = (0, 128, 0)  # RGB value for dark green

pygame.display.flip()


""" Functie pentru a incarca o imagine si a o scala la dimensiunile dorite """


def UploadImage(image_path, width, height):
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (width, height))
    return scaled_image
