# mtg_card_evaluator

Uses machine learning to evaluate Magic the Gathering (MTG) cards

Set up:
1. Run mtg_sdk_download.py once in order to download card information via mtg-sdk-python (https://github.com/MagicTheGathering/mtg-sdk-python) <br>
This will save the card information in JSON format, so that we won't have to repeatedly download the same information
2. Use the mtgutil (https://github.com/daltoncwu/mtgutil) tool to download the top metagame decks for modern and place them in the "resources/modern_decks" directory of this project
3. Run card_evaluator.py
