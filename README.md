# alphabet-detector
A library to detect what alphabet something is written in.

## Author
Eli Finkelshteyn (founder [constructor.io](http://www.constructor.io))

## Installation
<code>pip install alphabet-detector</code>  

## Usage
In general, you can just use the only_alphabet_chars(unicode_str, alphabet) method and expect a boolean response:


    from alphabet_detector import AlphabetDetector
    ad = AlphabetDetector()
    ad.only_alphabet_chars(u"ελληνικά means greek", "LATIN") #False
    ad.only_alphabet_chars(u"ελληνικά", "GREEK") #True
    ad.only_alphabet_chars(u'سماوي يدور', 'ARABIC')
    ad.only_alphabet_chars(u'שלום', 'HEBREW')
    ad.only_alphabet_chars(u"frappé", "LATIN") #True
    ad.only_alphabet_chars(u"hôtel lœwe 67", "LATIN") #True
    ad.only_alphabet_chars(u"det forårsaker første", "LATIN") #True
    ad.only_alphabet_chars(u"Cyrillic and кириллический", "LATIN") #False
    ad.only_alphabet_chars(u"кириллический", "CYRILLIC") #True

Convenience methods are also provided for some major languages:


    ad.is_cyrillic(u"Привет") #True  
    ad.is_latin(u"howdy") #True
    ad.is_cjk(u"hi") #False
    ad.is_cjk(u'汉字') #True
