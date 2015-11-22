# -*- coding: utf-8 -*-
import pytest
from alphabet_detector.alphabet_detector import AlphabetDetector


@pytest.fixture
def ad():
    return AlphabetDetector()


@pytest.fixture
def ad_no_mem():
    return AlphabetDetector(no_memory=True)


class TestAlphabetDetector:
    def test_is_in_alphabet(self, ad, ad_no_mem):
        assert ad.is_in_alphabet(u"a", "LATIN")
        assert not ad.is_in_alphabet(u"λ", "LATIN")
        assert not ad.is_in_alphabet(u"?", "LATIN")
        assert ad.alphabet_letters == {'LATIN': {u"?": False, u"a": True,
                                                 u"λ": False}}
        assert ad_no_mem.is_in_alphabet(u"a", "LATIN")
        assert not ad_no_mem.is_in_alphabet(u"λ", "LATIN")
        assert not ad_no_mem.is_in_alphabet(u"?", "LATIN")
        assert not ad_no_mem.alphabet_letters

    def test_only_alphabet_chars(self, ad):
        assert not ad.only_alphabet_chars(u"ελληνικά means greek", "LATIN")
        assert ad.only_alphabet_chars(u"ελληνικά", "GREEK")
        assert ad.only_alphabet_chars(u"سماوي يدور", "ARABIC")
        assert ad.only_alphabet_chars(u"שלום", "HEBREW")
        assert ad.only_alphabet_chars(u"frappé", "LATIN")
        assert ad.only_alphabet_chars(u"hôtel lœwe 67", "LATIN")
        assert ad.only_alphabet_chars(u"det forårsaker første", "LATIN")
        assert not ad.only_alphabet_chars(u"Cyrillic кириллический", "LATIN")
        assert ad.only_alphabet_chars(u"кириллический", "CYRILLIC")

    def test_detect_alphabet(self, ad):
        assert ad.detect_alphabet(u"Cyrillic and кириллический") == \
            {"CYRILLIC", "LATIN"}
        assert ad.detect_alphabet(u".%?") == set([])
        assert ad.detect_alphabet(u"hello?") == {"LATIN"}
        assert ad.detect_alphabet(u"кириллический?") == {"CYRILLIC"}

    def test_is_greek(self, ad):
        assert ad.is_greek(u"ελληνικά")
        assert not ad.is_greek(u"Привет")
        assert ad.is_greek(u"?")

    def test_is_cyrillic(self, ad):
        assert not ad.is_cyrillic(u"howdy")
        assert ad.is_cyrillic(u"Привет")
        assert ad.is_cyrillic(u"?")

    def test_is_latin(self, ad):
        assert ad.is_latin(u"howdy")
        assert not ad.is_latin(u"ελληνικά")
        assert ad.is_latin(u"?")

    def test_is_arabic(self, ad):
        assert ad.is_arabic(u"سماوي يدور")
        assert not ad.is_arabic(u"שלום")
        assert ad.is_arabic(u"?")

    def test_is_hebrew(self, ad):
        assert ad.is_hebrew(u"שלום")
        assert not ad.is_hebrew(u"سماوي يدور")
        assert ad.is_hebrew(u"?")

    def test_is_cjk(self, ad):
        assert ad.is_cjk(u'汉字')
        assert not ad.is_cjk(u"Привет")
        assert ad.is_cjk(u"?")

    def test_is_thai(self, ad):
        assert ad.is_thai(u"พยัญชนะ")
        assert not ad.is_thai(u"Привет")
        assert ad.is_thai(u"?")
