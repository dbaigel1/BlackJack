## design objects to represent a deck of cards and implement blackjack
import random #used for generating a random index in the deck of cards to draw
import time #used to simulate dealer drawing cards slowly

class Deck:
	def __init__(self, numSuits, numCards):
		self.cards = []
		self.suits = numSuits
		self.size = numCards #number of cards per suit

		for i in range(self.suits):
			for j in range(1, self.size+1):
				
				self.cards.append(Card(j, i))
	
	#generate a new random card and remove it from the deck
	def draw(self):
		randIndex = random.randint(0, len(self.cards)-1)
		self.cards[randIndex], self.cards[-1] = self.cards[-1], self.cards[randIndex]
		playerCard = self.cards.pop()
		#face cards are worth 10 in blackjack
		if playerCard.value > 10:
			playerCard.value = 10
		#aces are worth 11
		if playerCard.value == 1:
			playerCard.value = 11
		return playerCard

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
		

#create the blackjack game
#game will run once, after a hand is completed, program will terminate
#first, give the dealer 2 random cards, show player one of them
#give player two cards
#the thing about blackjack is that face cards are worth 10 each, while an
#ace card can be worth either 1 or 11
def playBlackJack():
	decision = True
	while decision:
		while True:
			print("starting a new game...\n")
			time.sleep(2)
			deck = Deck(4, 13)
			playerCards = []
			dealerCards = []

			#generate starting cards for dealer and player
			playerCards.append(deck.draw())
			playerCards.append(deck.draw())
			dealerCards.append(deck.draw())
			dealerCards.append(deck.draw())

			playerSum = playerCards[0].value + playerCards[1].value
			dealerSum = dealerCards[0].value

			while playerSum < 21:
				print(f"You: {playerSum}")
				print(f"Dealer: {dealerSum}")
				decision = input("What would you like to do? Type h to hit and s to stay \n")
				#generate another card
				if decision == "h":
					playerCards.append(deck.draw())
					#an ace was drawn
					if playerCards[-1].value == 11:
						if playerSum + 11 > 21:
							playerCards[-1].value = 1
					playerSum += playerCards[-1].value
				#move to dealer
				else:
					break

			print(f"Player sum is: {playerSum} \n")
			
			if playerSum > 21:
				print("player went over 21, dealer wins.")
				break
			
			print("Now it's the dealer's turn...")
			time.sleep(3)
			print("Revealing the dealer's second card...")
			print("-----------------------------------------------")

			dealerSum += dealerCards[-1].value

			while dealerSum < 21:
				print(f"Dealer: {dealerSum}\n")
				print(f"You: {playerSum}")
				print("-----------------------------------------------")
				time.sleep(3)

				#logic for when dealer should hit or stick
				if dealerSum > playerSum:
					break
				elif dealerSum == playerSum and dealerSum > 16:
					break

				else:
					dealerCards.append(deck.draw())
					dealerSum += dealerCards[-1].value


			print(f"Player sum is: {playerSum} \n")
			print(f"Dealer sum is: {dealerSum} \n")
			if playerSum == dealerSum:
				print("Tie game!")
				break
			winner = "player" if playerSum > dealerSum or dealerSum > 21 else "dealer"
			print(f"{winner} wins!")
			break

		decision = input("want to play again? Y or N\n")

		decision = decision.lower()
		if decision == "y":
			decision = True
		else:
			decision = False



		

#TODO:
	#add ability to play multiple rounds
	#add display of card sequence for player and dealer

	#print(f"card: value= {myDeck.cards[i].value} suit= {myDeck.cards[i].suit}")
print("deck of cards has been created, now starting game...")
playBlackJack()
