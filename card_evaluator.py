import json
from sklearn import tree
import os
import re

GRN_SET_FILE_LOCATION = 'resources/grn_mtg_sdk_data.json'
ALL_CARDS_FILE_LOCATION = 'resources/python_mtg_sdk_data.json'
SIDEBOARD_PREFIX = "SB: "

def getSize(collection1):
	if collection1 is None:
		return 0
	else:
		return len(collection1)

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

print(len(cards))
features = []
labels = []
for card in cards:
	print("Name: %s, colors: %s, cmc: %s, textLength: %s" % (card["name"], getSize(card["colors"]), card["cmc"], getSize(card["text"])))
	features.append((getSize(card["colors"]), card["cmc"], getSize(card["text"])))
	if (card["name"] in playedCards):
		print(card["name"] + " is played!")
		labels.append(1)
	else:
		labels.append(0)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features , labels)

print(clf.predict([[0, 0, 130]]))