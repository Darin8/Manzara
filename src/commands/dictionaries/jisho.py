import re

from definitions.arguments_command import ManzaraWithArgumentsCommand
from typing import Tuple
from urllib.parse import quote

JISHO_URL_BASE  = "https://www.jisho.org/"
JISHO_URL_SEARCH = JISHO_URL_BASE + "search/"
WORDS = quote(" #words")
KANJI = quote(" #kanji")
SENTENCES = quote(" #sentences")
NAMES = quote(" #names")

class Jisho(ManzaraWithArgumentsCommand):

    def redirect(self, args: Tuple[str]) -> str:
        if len(args) > 1:

            root_arg = args[0].lower()
            rest_arg = quote(' '.join(args[1:]))

            # Order by frequency
            if root_arg == "jw":
                return JISHO_URL_SEARCH + rest_arg + WORDS
            elif root_arg == "jk":
                return JISHO_URL_SEARCH + rest_arg + KANJI
            elif root_arg == "js":
                return JISHO_URL_SEARCH + rest_arg + SENTENCES
            elif root_arg == "jn":
                return JISHO_URL_SEARCH + rest_arg + NAMES
                
        else:
            return JISHO_URL_BASE

    @property
    def description(self) -> str:
        return """For making searches on Jisho"""
    
    @property
    def bindings(self) -> Tuple[re.Pattern]:
        return [
            re.compile(r'^j[wksn]?(?:\ .+)?$', re.IGNORECASE),
            re.compile(r'^jisho(?:\ .+)?$', re.IGNORECASE)
        ]