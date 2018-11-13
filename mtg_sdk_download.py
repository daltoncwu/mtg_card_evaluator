from mtgsdk import Card
import json

GRN_SET_FILE_LOCATION = 'resources/grn_mtg_sdk_data.json'
ALL_CARDS_FILE_LOCATION = 'resources/python_mtg_sdk_data.json'

def obj_dict(obj):
    return obj.__dict__

#Example of downloading a smaller set (GRN)
grn_cards = Card.where(set='grn').all()
cards_json = json.dumps(grn_cards, default=obj_dict)
with open(GRN_SET_FILE_LOCATION, 'w') as outfile:
	json.dump(cards_json, outfile)

#Download all cards in MTG
all_cards = Card.all()
cards_json = json.dumps(all_cards, default=obj_dict)
with open(ALL_CARDS_FILE_LOCATION, 'w') as outfile:
	json.dump(cards_json, outfile)
