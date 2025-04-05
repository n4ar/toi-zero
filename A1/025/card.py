rank_map = {
    'A': 'ace',
    'J': 'jack',
    'Q': 'queen',
    'K': 'king',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10'
}

suit_map = {
    'S': 'spades',
    'H': 'hearts',
    'D': 'diamonds',
    'C': 'clubs'
}

card = input().upper().strip()

if len(card) == 3:
    rank = card[:2]
    suit = card[2]
else:
    rank = card[0]
    suit = card[1]

print(f"{rank_map[rank]} of {suit_map[suit]}")
