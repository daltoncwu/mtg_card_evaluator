# mtg_card_evaluator

Uses machine learning to evaluate Magic the Gathering (MTG) cards. The model is a work in progress, and is not yet very accurate/useful. However, this project currently demonstrates how to implement a lot of the required pre-processing logic.

Currently, this project evaluates if a card is playable in the Modern format. A card is determined to be playable in the format if it is used in a deck list that is a top metagame deck (more details below).

Set up:
1. Run mtg_sdk_download.py once in order to download card information: <br>
`python mtg_sdk_download.py` <br>
This will save the card information in JSON format, so that we won't have to repeatedly download the same information. This uses mtg-sdk-python (https://github.com/MagicTheGathering/mtg-sdk-python)
2. Use the mtgutil (https://github.com/daltoncwu/mtgutil) tool to download the top metagame decks for modern and place them in the "resources/modern_decks" directory of this project
3. Run card_evaluator.py <br>
`python card_evaluator.py` <br>
You will then be prompted to enter the card name you want to evaluate:<br>
`Please enter a MTG card name to evaluate: `
