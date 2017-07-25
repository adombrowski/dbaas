import re

class SEC:
	def __init__(self, text, file="\|"):
		REGEX_BASE = "[0-9]+[^\n]+%s[^\n]+\.txt"

		self._regex = REGEX_BASE % file
		


