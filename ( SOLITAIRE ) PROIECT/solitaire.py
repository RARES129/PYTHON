import pygame
import sys
import random
import os

pygame.init()
width, height = 1000, 600
pygame.display.set_caption("Solitaire")
window = pygame.display.set_mode((width, height))
background_color = (0, 128, 0)  # RGB value for dark green


pygame.display.update()


def UploadImage(image_path, width, height):
    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, (width, height))
    return scaled_image


# ---------------------------CARTI DE JOC---------------------------
class Card:
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

    def draw(self, x, y):
        window.blit(self.imageShow, (x, y))

    def get_colour(self):
        return self.color

    def flip(self):
        self.faceup = not self.faceup
        if self.faceup:
            self.imageShow = self.image
        else:
            self.imageShow = self.cardBack

    def set_border(self):
        self.has_border = not self.has_border

    def isOppositeColour(self, other_card):
        if self.color == "red" and other_card.color == "black":
            return True
        elif self.color == "black" and other_card.color == "red":
            return True
        else:
            return False

    def IsOneLessThan(self, other_card):
        if self.number == other_card.number - 1:
            return True
        else:
            return False


# ---------------------------PACHETE DE CARTI PRINCIPALE---------------------------
class Deck:
    SpaceBetweenCards = 25
    SpaceBetweenDecks = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cards = []
        self.emptyDeckImage = UploadImage("PNG-cards/empty_pile_slot.png", 66, 100)

    def add_card(self, card):
        self.cards.append(card)

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

    def get_top_card(self):
        if self.cards:
            return self.cards[-1]
        else:
            return None

    def remove_top_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def remove_cards(self):
        self.cards.clear()


# ---------------------------PACHET DE CARTI DE REZERVA---------------------------
class ReserveDeck(Deck):
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

    def remove_top_card(self):
        if self.cards:
            card = self.cards.pop()
            card.flip()
            return card
        else:
            return None


# ---------------------------PACHETE DE CARTI FINALE---------------------------
class FoundationDeck(Deck):
    def __init__(self, x, y, suit):
        super().__init__(x, y)
        self.suit = suit
        self.emptyDeckImage = UploadImage(f"PNG-cards/{suit}_slot.png", 66, 100)

    def add_card(self, card):
        if card.suit == self.suit:
            if self.cards:
                if card.number == self.cards[-1].number + 1 or card.number == 1:
                    self.cards.append(card)
                    return True
            else:
                if card.number == 1:
                    self.cards.append(card)
                    return True
        return False

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


# ---------------------------CARTILE TRASE DIN PACHETUL DE REZERVA---------------------------
class WasteDeck(Deck):
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


# ---------------------------PACHET PENTRU MUTARI---------------------------


class MoveDeck(Deck):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.active = False

    def add_card(self, card):
        self.cards.append(card)
        card.set_border()
        self.active = True

    def remove_cards(self):
        for card in self.cards:
            card.set_border()
        self.cards.clear()
        self.active = False


# ---------------------------BUTON RESET---------------------------
class ResetButton:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = UploadImage("PNG-cards/reset.png", width, height)

    def draw(self):
        window.blit(self.image, (self.x, self.y))

    def IsClicked(self):
        MousePosX, MousePosY = pygame.mouse.get_pos()
        if (
            self.x <= MousePosX <= self.x + self.width
            and self.y <= MousePosY <= self.y + self.height
        ):
            return True
        else:
            return False


# ---------------------------LOOP-UL PRINCIPAL AL JOCULUI---------------------------
running = True
reset = True
game_won = False
game_active = True
wasteDeck = WasteDeck(50, 140)
reserveDeck = ReserveDeck(50, 20)
moveDeck = MoveDeck(0, 0)

while running:
    # --------------------------------Constuim elementele jocului
    if reset:
        # Cream pachetul de carti
        deck = []
        foundationDeck = []
        MainDeck = []
        reserveDeck.remove_cards()
        wasteDeck.remove_cards()
        moveDeck.remove_cards()
        for number in range(1, 14):
            for suit in ["hearts", "diamonds"]:
                card = Card("red", suit, number)
                deck.append(card)
            for suit in ["clubs", "spades"]:
                card = Card("black", suit, number)
                deck.append(card)
        random.shuffle(deck)

        # Cream pachetele de carti principale
        numberOfCards = 1
        for i in range(7):
            newMainDeck = Deck(250 + i * Deck.SpaceBetweenDecks, 20)
            for j in range(numberOfCards):
                card = deck.pop()
                if j == numberOfCards - 1:
                    card.flip()
                newMainDeck.add_card(card)
            MainDeck.append(newMainDeck)
            numberOfCards += 1

        # Cream pachetul de carti de rezerva
        for i in range(len(deck)):
            card = deck.pop()
            reserveDeck.add_card(card)

        # Cream pachetele de carti finale
        for i, suit in enumerate(["hearts", "spades", "diamonds", "clubs"]):
            newFoundationDeck = FoundationDeck(
                50 + i * Deck.SpaceBetweenDecks, height - 150, suit
            )
            foundationDeck.append(newFoundationDeck)

        reset = False

    # Verificam daca jocul a fost castigat
    if all(len(deck.cards) == 13 for deck in foundationDeck):
        game_won = True

    # --------------------------------Gestionam evenimentele
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Reset.IsClicked():
                # --------------------------------Evenimentele cand nu avem carti selectate
                reset = True
        if event.type == pygame.MOUSEBUTTONDOWN and game_active and not moveDeck.active:
            MousePosX, MousePosY = pygame.mouse.get_pos()

            # Verificam daca am dat click pe pachetul de carti de rezerva
            if (
                reserveDeck.x <= MousePosX <= reserveDeck.x + 66
                and reserveDeck.y <= MousePosY <= reserveDeck.y + 100
            ):
                if not reserveDeck.cards:
                    for i in range(len(wasteDeck.cards)):
                        card = wasteDeck.remove_top_card()
                        card.flip()
                        reserveDeck.add_card(card)
                else:
                    card = reserveDeck.remove_top_card()
                    wasteDeck.add_card(card)

            # Verificam daca am dat click pe pachetul de carti trase din pachetul de rezerva
            if (wasteDeck.x <= MousePosX <= wasteDeck.x + 66) and (
                wasteDeck.y <= MousePosY <= wasteDeck.y + 100
            ):
                if wasteDeck.cards:
                    card = wasteDeck.remove_top_card()
                    wasteDeck.add_card(card)
                    moveDeck.add_card(card)

            # Verificam daca am dat click pe unul dintre pachetele de carti principale
            for deck in MainDeck:
                for i, card in enumerate(deck.cards):
                    if (
                        i == len(deck.cards) - 1
                        and deck.x <= MousePosX < deck.x + 66
                        and deck.y + i * Deck.SpaceBetweenCards
                        <= MousePosY
                        < deck.y + i * Deck.SpaceBetweenCards + 100
                    ):
                        if card.faceup:
                            for card in deck.cards[i:]:
                                moveDeck.add_card(card)
                    elif (
                        deck.x <= MousePosX < deck.x + 66
                        and deck.y + i * Deck.SpaceBetweenCards
                        <= MousePosY
                        < deck.y + (i + 1) * Deck.SpaceBetweenCards
                    ):
                        if card.faceup:
                            for card in deck.cards[i:]:
                                moveDeck.add_card(card)

            # Verificam daca am dat click pe unul dintre pachetele de carti finale
            for deck in foundationDeck:
                if (
                    deck.x <= MousePosX <= deck.x + 66
                    and deck.y <= MousePosY <= deck.y + 100
                ):
                    if deck.cards:
                        card = deck.remove_top_card()
                        deck.add_card(card)
                        moveDeck.add_card(card)

        # --------------------------------Evenimentele cand avem carti selectate
        elif event.type == pygame.MOUSEBUTTONDOWN and game_active and moveDeck.active:
            MousePosX, MousePosY = pygame.mouse.get_pos()
            for deck in foundationDeck:
                if (
                    deck.x <= MousePosX <= deck.x + 66
                    and deck.y <= MousePosY <= deck.y + 100
                ):
                    if len(moveDeck.cards) == 1:
                        card = moveDeck.get_top_card()
                        if deck.add_card(card):
                            moveDeck.remove_cards()
                            for main_deck in MainDeck:
                                if card in main_deck.cards:
                                    main_deck.cards.remove(card)
                                    if (
                                        len(main_deck.cards) > 0
                                        and not main_deck.cards[-1].faceup
                                    ):
                                        main_deck.cards[-1].flip()
                            if card in wasteDeck.cards:
                                wasteDeck.cards.remove(card)

            for deck in MainDeck:
                if (deck.x <= MousePosX <= deck.x + 66) and (
                    deck.y + (len(deck.cards) - 1) * Deck.SpaceBetweenCards
                    <= MousePosY
                    <= deck.y + (len(deck.cards) - 1) * Deck.SpaceBetweenCards + 100
                ):
                    if len(deck.cards) == 0:
                        if moveDeck.cards[0].number == 13:
                            for card in moveDeck.cards:
                                for main_deck in MainDeck:
                                    if card in main_deck.cards:
                                        main_deck.cards.remove(card)
                                        if (
                                            len(main_deck.cards) > 0
                                            and not main_deck.cards[-1].faceup
                                        ):
                                            main_deck.cards[-1].flip()
                                    if card in wasteDeck.cards:
                                        wasteDeck.cards.remove(card)
                                    for foundation_deck in foundationDeck:
                                        if card in foundation_deck.cards:
                                            foundation_deck.cards.remove(card)
                                deck.add_card(card)
                            moveDeck.remove_cards()

                    elif moveDeck.cards[0].isOppositeColour(
                        deck.get_top_card()
                    ) and moveDeck.cards[0].IsOneLessThan(deck.get_top_card()):
                        for card in moveDeck.cards:
                            for main_deck in MainDeck:
                                if card in main_deck.cards:
                                    main_deck.cards.remove(card)
                                    if (
                                        len(main_deck.cards) > 0
                                        and not main_deck.cards[-1].faceup
                                    ):
                                        main_deck.cards[-1].flip()
                                if card in wasteDeck.cards:
                                    wasteDeck.cards.remove(card)
                                for foundation_deck in foundationDeck:
                                    if card in foundation_deck.cards:
                                        foundation_deck.cards.remove(card)
                            deck.add_card(card)

                        moveDeck.remove_cards()

            moveDeck.remove_cards()

    # --------------------------------Randam elementele
    window.fill(background_color)
    for deck in foundationDeck:
        deck.draw()
    for deck in MainDeck:
        deck.draw()
    reserveDeck.draw()
    wasteDeck.draw()
    Reset = ResetButton(width - 150, height - 150, 100, 100)
    Reset.draw()

    # --------------------------------Verificam daca am castigat jocul
    if game_won:
        font = pygame.font.SysFont("comicsans", 100)
        text = font.render("You Won!", 1, (255, 255, 255))
        window.blit(
            text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2)
        )
        game_active = False

    pygame.display.flip()

pygame.quit()
