# alphabet-detector
[![Build Status](https://travis-ci.org/EliFinkelshteyn/alphabet-detector.svg?branch=master)](https://travis-ci.org/EliFinkelshteyn/alphabet-detector)
[![Coverage Status](https://coveralls.io/repos/EliFinkelshteyn/alphabet-detector/badge.svg?branch=master&service=github)](https://coveralls.io/github/EliFinkelshteyn/alphabet-detector?branch=master)

A library to detect what alphabet something is written in. **Works on Python 2.7+ and 3.3+**

## Author
Eli Finkelshteyn (founder [constructor.io](http://www.constructor.io))

## Installation
<code>pip install alphabet-detector</code>  

## Usage
To instantiate an AlphabetDetector (the object is used for speed optimization):

```python
from alphabet_detector import AlphabetDetector
ad = AlphabetDetector()
```

In general, you can just use the `only_alphabet_chars(unicode_str, alphabet)` method and expect a boolean response:

```python
ad.only_alphabet_chars(u"ελληνικά means greek", "LATIN") #False
ad.only_alphabet_chars(u"ελληνικά", "GREEK") #True
ad.only_alphabet_chars(u'سماوي يدور', 'ARABIC') #True
ad.only_alphabet_chars(u'שלום', 'HEBREW') #True
ad.only_alphabet_chars(u"frappé", "LATIN") #True
ad.only_alphabet_chars(u"hôtel lœwe 67", "LATIN") #True
ad.only_alphabet_chars(u"det forårsaker første", "LATIN") #True
ad.only_alphabet_chars(u"Cyrillic and кириллический", "LATIN") #False
ad.only_alphabet_chars(u"кириллический", "CYRILLIC") #True
```

You can also request free-style detection of any unicode string:

```python
ad.detect_alphabet(u'Cyrillic and кириллический') #{'CYRILLIC', 'LATIN'}
```

Convenience methods are also provided for some major languages:

```python
ad.is_cyrillic(u"Привет") #True  
ad.is_latin(u"howdy") #True
# NOTE: this only detects Chinese script characters (Hanzi/Kanji/Hanja).
# it does not detect other CJK script characters like Hangul or Katakana
ad.is_cjk(u"hi") #False
ad.is_cjk(u'汉字') #True
```

**NOTE: all strings are expected to be unicode to keep things consistent. Conversion is *never* done for you, and errors are thrown when a string is not unicode.**
