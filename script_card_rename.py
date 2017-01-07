import os
import json
import re
from pprint import pprint
from unidecode import unidecode

DATA_PATH = "./data/"
CARD_PATH = "./Cards_0.8.8_es/"


def format_km(str):
	str = unidecode(str.lower().replace(" ", "_").replace("'", "_"))
	if (str[-1:] == "_"):
		str = str[:-1]
	return (str)

def find_name(card, dict_json, lang_from, lang_to):
	card = re.sub('\.png', '', card).lower()

	test_infinite = card[-2:]
	isInfinite = False
	if test_infinite in ["_1", "_2", "_3"]:
		card = re.sub('_niveau' + test_infinite, '', card)
		isInfinite = True
	test_token = card[-6:]
	isToken = False
	if (test_token == "_token"):
		card = re.sub("_token", "", card)
		isToken = True
	newName = ""
	for key, value in dict_json.items():
		if (card == format_km(value["Texts"]["Name" + lang_from])):
			newName = format_km(value["Texts"]["Name" + lang_to])
			if (isInfinite):
				newName = newName + '_niveau' + test_infinite
			if (isToken):
				newName = newName + test_token
			break
	return newName
			

def rename(lang_from, lang_to):
	dict_json = dict()

	for filename in os.listdir(DATA_PATH):
		with open(DATA_PATH + filename, encoding="utf_8_sig") as data_file:
			data = json.load(data_file)
			dict_json[data['Name']] = data
	for card_file_name in os.listdir(CARD_PATH):
		name = find_name(card_file_name, dict_json, lang_from, lang_to)
		if (name != ""):
			try:
				os.rename(CARD_PATH + card_file_name, CARD_PATH + name + ".png")
			except:
				pass
	print("FINISHED")

if __name__ == '__main__':
	rename("FR", "ES")
