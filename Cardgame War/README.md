# Kartenspiel War

Eine einfache Python-Implementation des klassischen Kartenspiels "War" (Krieg).

## Beschreibung

Dieses Projekt implementiert eine textbasierte Version des Kartenspiels War. Das Spiel wird zwischen zwei Spielern gespielt, wobei jeder Spieler die Hälfte eines gemischten Kartendecks erhält. In jeder Runde spielen beide Spieler eine Karte aus, und der Spieler mit der höheren Karte gewinnt beide Karten. Bei gleichen Karten kommt es zum "Krieg".

## Projektstruktur

- `cards.py`: Enthält die Kartenfunktionalität und Konstanten
- `war_game.py`: Implementiert die Spielerklassen und das Deck
- `game.py`: Enthält die Hauptspiellogik

## Installation

1. Klone das Repository
2. Stelle sicher, dass Python 3.x installiert ist
3. Führe das Spiel aus:
```bash
python game.py
```

## Spielregeln

- Jeder Spieler erhält zu Beginn die Hälfte des Decks
- In jeder Runde spielt jeder Spieler eine Karte
- Der Spieler mit der höheren Karte gewinnt beide Karten
- Bei gleichen Karten kommt es zum "Krieg":
  - Jeder Spieler legt 3 Karten verdeckt
  - Eine vierte Karte wird aufgedeckt
  - Der Gewinner erhält alle Karten
- Das Spiel endet, wenn ein Spieler keine Karten mehr hat 