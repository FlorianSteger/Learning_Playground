from typing import Tuple, Dict

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = range(2, 15)  # 2-14 where 14 is Ace, 11-13 are Jack, Queen, King
VALUE_NAMES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

def create_card(suit: str, value: int) -> Tuple[str, int]:
    """Create a card as a tuple of (suit, value)"""
    return (suit, value)

def get_card_str(card: Tuple[str, int]) -> str:
    """Get string representation of a card"""
    suit, value = card
    card_value = VALUE_NAMES.get(value, str(value))
    return f"{card_value} of {suit}"

def get_card_value(card: Tuple[str, int]) -> int:
    """Get the value of a card"""
    return card[1] 