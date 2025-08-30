import requests

# Base URL
API_BASE = "https://deckofcardsapi.com/api/deck"

#  Check if site is up
try:
    r = requests.get("https://deckofcardsapi.com/")
    if r.status_code == 200:
        print("Site is up!")
    else:
        print("Site returned:", r.status_code)
        exit()
except Exception as e:
    print("Error:", e)
    exit()

# Get a new shuffled deck
res = requests.get(f"{API_BASE}/new/shuffle/?deck_count=1").json()
deck_id = res["deck_id"]
print("New deck created:", deck_id)

#  Deal 3 cards to each of 2 players
p1 = requests.get(f"{API_BASE}/{deck_id}/draw/?count=3").json()["cards"]
p2 = requests.get(f"{API_BASE}/{deck_id}/draw/?count=3").json()["cards"]

print("\nPlayer 1 cards:", [c["value"] + " of " + c["suit"] for c in p1])
print("Player 2 cards:", [c["value"] + " of " + c["suit"] for c in p2])

#  Check for Blackjack (first 2 cards only)
def is_blackjack(hand):
    if len(hand) < 2:
        return False
    values = [c["value"] for c in hand[:2]]
    return "ACE" in values and any(v in ["10", "JACK", "QUEEN", "KING"] for v in values)

p1_blackjack = is_blackjack(p1)
p2_blackjack = is_blackjack(p2)

print()
if p1_blackjack and p2_blackjack:
    print("Both players have Blackjack!")
elif p1_blackjack:
    print("Player 1 has Blackjack!")
elif p2_blackjack:
    print("Player 2 has Blackjack!")
else:
    print("No Blackjack this round.")