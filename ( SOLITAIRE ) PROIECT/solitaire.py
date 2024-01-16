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


# ---------------------------CARTI DE JOC---------------------------
""" Clasa pentru cartile de joc."""


class Card:
    """Constructorul clasei"""

    def __init__(self, color, suit, number):
        self.color = color
        self.suit = suit
        self.number = number
        self.faceup = False
        self.image = UploadImage(
            "PNG-cards/" + str(number) + "_of_" + suit + ".png", 66, 100
        )
        self.cardBack = UploadImage("PNG-cards/cardback.png", 66, 100)
        self.imageShow = self.cardBack
        self.border_color = (255, 0, 0)
        self.has_border = False

    """Metoda pentru a desena cartea de joc"""

    def draw(self, x, y):
        window.blit(self.imageShow, (x, y))

    """Metoda pentru a obtine culoarea cartii"""

    def get_colour(self):
        return self.color

    """Metoda pentru a intoarce cartea de joc"""

    def flip(self):
        self.faceup = not self.faceup
        if self.faceup:
            self.imageShow = self.image
        else:
            self.imageShow = self.cardBack

    """Metoda pentru a adauga sau elimina bordura cartii de joc"""

    def set_border(self):
        self.has_border = not self.has_border

    """Metoda pentru a verifica daca cartea este de culoare opusa cu cartea data ca parametru"""

    def isOppositeColour(self, other_card):
        if self.color == "red" and other_card.color == "black":
            return True
        elif self.color == "black" and other_card.color == "red":
            return True
        else:
            return False

    """Metoda pentru a verifica daca cartea este cu un numar mai mica decat cartea data ca parametru"""

    def IsOneLessThan(self, other_card):
        if self.number == other_card.number - 1:
            return True
        else:
            return False


# ---------------------------PACHETE DE CARTI PRINCIPALE---------------------------
""" Clasa pentru pachetele de carti principale."""


class Deck:
    SpaceBetweenCards = 25
    SpaceBetweenDecks = 100

    """"Constructorul clasei"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cards = []
        self.emptyDeckImage = UploadImage("PNG-cards/empty_pile_slot.png", 66, 100)

    """Metoda pentru a adauga o carte in pachetul de carti principale"""

    def add_card(self, card):
        self.cards.append(card)

    """Metoda pentru a desena pachetul de carti principale"""

    def draw(self):
        if self.cards:
            for i, card in enumerate(self.cards):
                card.draw(self.x, self.y + i * Deck.SpaceBetweenCards)
                if card.has_border:
                    pygame.draw.rect(
                        window,
                        card.border_color,
                        (self.x - 1, self.y + i * Deck.SpaceBetweenCards - 1, 68, 102),
                        3,
                    )
        else:
            window.blit(self.emptyDeckImage, (self.x, self.y))

    """Metoda pentru a vizualiza cartea de sus din pachetul de carti principale"""

    def get_top_card(self):
        if self.cards:
            return self.cards[-1]
        else:
            return None

    """Metoda pentru a elimina cartea de sus din pachetul de carti principale"""

    def remove_top_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

    """Metoda pentru a elimina toate cartile"""

    def remove_cards(self):
        self.cards.clear()


# ---------------------------PACHET DE CARTI DE REZERVA---------------------------
""" Clasa pentru pachetul de carti de rezerva."""


class ReserveDeck(Deck):
    """Metoda pentru a desena pachetul de carti de rezerva"""

    def draw(self):
        if self.cards:
            for i, card in enumerate(self.cards):
                card.draw(self.x, self.y)
                if card.has_border:
                    pygame.draw.rect(
                        window,
                        card.border_color,
                        (self.x - 1, self.y - 1, 68, 102),
                        3,
                    )
        else:
            window.blit(self.emptyDeckImage, (self.x, self.y))

    """Metoda pentru a elimina cartea de sus din pachetul de carti de rezerva"""

    def remove_top_card(self):
        if self.cards:
            card = self.cards.pop()
            card.flip()
            return card
        else:
            return None

