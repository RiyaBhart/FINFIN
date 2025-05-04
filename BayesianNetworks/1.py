suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Create full deck of 52 cards
deck = [(rank, suit) for suit in suits for rank in ranks]
total_cards = len(deck)

# 1. Red cards
red_cards = [card for card in deck if card[1] in ["hearts", "diamonds"]]
p_red = len(red_cards) / total_cards

# 2. Heart cards given red
heart_cards = [card for card in red_cards if card[1] == "hearts"]
p_heart_given_red = len(heart_cards) / len(red_cards)

# 3. Diamond face cards
face_cards = [card for card in deck if card[0] in ['Jack', 'Queen', 'King']]
diamond_faces = [card for card in face_cards if card[1] == "diamonds"]
p_diamond_given_face = len(diamond_faces) / len(face_cards)

# 4. Spade face cards or Queens
spade_faces = [card for card in face_cards if card[1] == "spades"]
queens = [card for card in face_cards if card[0] == "Queen"]
# Combine and remove duplicates
spade_or_queen = set(spade_faces + queens)
p_spade_or_queen_given_face = len(spade_or_queen) / len(face_cards)

# Print results
print(f"Probability of drawing a red card: {p_red:.2f}")
print(f"Probability of heart given red card: {p_heart_given_red:.2f}")
print(f"Probability of diamond given face card: {p_diamond_given_face:.2f}")
print(f"Probability of spade or queen given face card: {p_spade_or_queen_given_face:.2f}")
