import random
from typing import List, Tuple
import cards

class Deck:
    def __init__(self):
        self.cards: List[Tuple[str, int]] = []
        self.create_deck()
    
    def create_deck(self):
        for suit in cards.SUITS:
            for value in cards.VALUES:
                self.cards.append(cards.create_card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self) -> Tuple[str, int]:
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

class PlayerHand:
    def __init__(self):
        self.cards: List[Tuple[str, int]] = []
    
    def add_card(self, card: Tuple[str, int]):
        self.cards.append(card)
    
    def play_card(self) -> Tuple[str, int]:
        if len(self.cards) > 0:
            return self.cards.pop(0)
        return None
    
    def add_cards(self, new_cards: List[Tuple[str, int]]):
        self.cards.extend(new_cards)
    
    def __len__(self) -> int:
        return len(self.cards)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = PlayerHand()
    
    def has_cards(self) -> bool:
        return len(self.hand) > 0
    
    def play_card(self) -> Tuple[str, int]:
        return self.hand.play_card()
    
    def add_cards(self, new_cards: List[Tuple[str, int]]):
        self.hand.add_cards(new_cards) 