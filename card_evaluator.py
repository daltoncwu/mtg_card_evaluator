import json
from sklearn import tree
import os
import re
from mtgsdk import Card

GRN_SET_FILE_LOCATION = 'resources/grn_mtg_sdk_data.json'
ALL_CARDS_FILE_LOCATION = 'resources/python_mtg_sdk_data.json'
SIDEBOARD_PREFIX = "SB: "

def getSize(collection1):
	if collection1 is None:
		return 0
	else:
		return len(collection1)

def getCardByName(card_name):
	cards = Card.where(name=card_name).all()
	for card in cards:
		if (card.name == card_name):
			return card
	raise ValueError('No card was found with the name "%s"' % string)

#Handles input if card is a dict or a mtgsdk.Card
def computeFeatures(card):
	if (isinstance(card, dict)):
		features =  (getSize(card["colors"]), card["cmc"], getSize(card["text"]))
	elif (isinstance(card, Card)):
		features = (getSize(card.colors), card.cmc, getSize(card.text))
	else:
		raise TypeError("Card argument was not in an appropriate format.")
	#print("colors: %s, cmc: %s, textLength: %s" % features)
	return features

def getPlayedCards():
	playedCards = set()
	for filename in os.listdir('resources/modern_decks'):
		with open("resources/modern_decks/" + filename) as file:
			content = file.readlines()
			content = [s.strip() for s in content]
			for line in content:
				if (line.startswith(SIDEBOARD_PREFIX)):
					line = line[len(SIDEBOARD_PREFIX):]
				line = re.sub(r'^[0-9]+ ', '', line)
				playedCards.add(line)
	return playedCards

playedCards = getPlayedCards()

with open(GRN_SET_FILE_LOCATION, 'r', encoding='utf-8') as file:#Using smaller GRN set for testing
#with open(ALL_CARDS_FILE_LOCATION, 'r', encoding='utf-8') as file: #This is the set of all cards in MTG
	file_string = json.load(file)

cards = json.loads(file_string)

features = []
labels = []
for card in cards:
	#print("Name: %s" % (card["name"]))
	features.append(computeFeatures(card))
	if (card["name"] in playedCards):
		print(card["name"] + " is played!")
		labels.append(1)
	else:
		labels.append(0)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features , labels)

print("Please enter a MTG card name to evaluate: ")
card_input = input()
card = getCardByName(card_input)

new_card_features = []
new_card_features.append(computeFeatures(card))
print(new_card_features)
print(clf.predict(new_card_features))
#print(clf.predict([[0, 0, 130]]))
