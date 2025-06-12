from war_game import Deck, Player
import cards
import sys

def play_war():
    print("="*50)
    print("SPIELSTART".center(50))
    print("="*50)
    sys.stdout.flush()

    # Spieler erstellen
    player1 = Player("Spieler 1")
    player2 = Player("Spieler 2")

    # Deck erstellen und mischen
    deck = Deck()
    deck.shuffle()

    # Karten an Spieler verteilen
    while deck.cards:
        player1.hand.add_card(deck.draw_card())
        if deck.cards:  # Check falls ungerade Anzahl an Karten
            player2.hand.add_card(deck.draw_card())
    
    round_num = 0
    
    # Hauptspielschleife
    while player1.has_cards() and player2.has_cards():
        round_num += 1
        # Beide Spieler decken eine Karte auf
        card1 = player1.play_card()
        card2 = player2.play_card()
        
        # Karten vergleichen
        pot = [card1, card2]  # Alle Karten, die in dieser Runde im Spiel sind
        
        while cards.get_card_value(card1) == cards.get_card_value(card2):
            # Prüfen ob beide Spieler genug Karten für Krieg haben
            if len(player1.hand) < 4 or len(player2.hand) < 4:
                # Verbleibende Karten dem anderen Spieler geben
                if len(player1.hand) < 4:
                    player2.add_cards(pot + player1.hand.cards)
                    player1.hand.cards = []
                else:
                    player1.add_cards(pot + player2.hand.cards)
                    player2.hand.cards = []
                break
            
            # Drei verdeckte Karten
            for _ in range(3):
                pot.append(player1.play_card())
                pot.append(player2.play_card())
            
            # Vierte Karte aufgedeckt
            card1 = player1.play_card()
            card2 = player2.play_card()
            pot.extend([card1, card2])
        
        # Gewinner der Runde bestimmen
        if cards.get_card_value(card1) > cards.get_card_value(card2):
            player1.add_cards(pot)
        elif cards.get_card_value(card2) > cards.get_card_value(card1):
            player2.add_cards(pot)
    
    print("\n" + "="*50)
    print("SPIELENDE".center(50))
    print("="*50)
    sys.stdout.flush()
    
    # Ausgabe des Gewinners
    if not player1.has_cards():
        winner = player2.name
    else:
        winner = player1.name
    
    print("\n" + "*"*50)
    print(f"GEWINNER: {winner}".center(50))
    print("*"*50)
    sys.stdout.flush()

    print(f"Anzahl gespielter Runden: {round_num}")

if __name__ == "__main__":
    print("Willkommen zum Kartenspiel Krieg!")
    print("Das Spiel wird gespielt...")
    play_war() 