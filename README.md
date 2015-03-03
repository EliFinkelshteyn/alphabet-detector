# alphabet-detector
A library to detect what alphabet something is written in.

## Author
Eli Finkelshteyn (founder [constructor.io](http://www.constructor.io))

## Installation
<code>pip install alphabet-detector</code>  

## Usage
In general, you can just use the only_alphabet_chars(unicode_str, alphabet) method and expect a boolean response:

<code> from alphabet_detector import AlphabetDetector  
ad = AlphabetDetector()  
ad.only_alphabet_chars(u"ελληνικά means greek", "LATIN") #False  
ad.only_alphabet_chars(u"ελληνικά", "GREEK") #True  
ad.only_alphabet_chars(u"frappé", "LATIN") #True  
ad.only_alphabet_chars(u"hôtel lœwe", "LATIN") #True  
ad.only_alphabet_chars(u"123 ångstrom ð áß", "LATIN") #True  
ad.only_alphabet_chars(u"russian: гага", "LATIN") #False  
ad.only_alphabet_chars(u"гага", "CYRILLIC") #True  </code>

Convenience methods are also provided for some major languages:

<code>
ad.is_cyrillic(u"гага") #True  
ad.is_latin(u"howdy") #True
</code>