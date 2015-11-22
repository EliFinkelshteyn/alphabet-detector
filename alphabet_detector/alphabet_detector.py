import unicodedata as ud
from collections import defaultdict


class AlphabetDetector:
    def __init__(self, no_memory=False):
        self.alphabet_letters = defaultdict(dict)
        self.no_memory = no_memory

    def is_in_alphabet(self, uchr, alphabet):
        if self.no_memory:
            return alphabet in ud.name(uchr)
        try:
            return self.alphabet_letters[alphabet][uchr]
        except KeyError:
            return self.alphabet_letters[alphabet].setdefault(
                uchr, alphabet in ud.name(uchr))

    def only_alphabet_chars(self, unistr, alphabet):
        return all(self.is_in_alphabet(uchr, alphabet)
                   for uchr in unistr if uchr.isalpha())

    def detect_alphabet(self, unistr):
        return set(ud.name(char).split(' ')[0]
                   for char in unistr if char.isalpha())

    def is_greek(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'GREEK') else False

    def is_cyrillic(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'CYRILLIC') else False

    def is_latin(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'LATIN') else False

    def is_arabic(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'ARABIC') else False

    def is_hebrew(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'HEBREW') else False

    def is_cjk(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'CJK') else False

    def is_thai(self, unistr):
        return True if self.only_alphabet_chars(unistr, 'THAI') else False
