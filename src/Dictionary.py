from PyDictionary import PyDictionary

dictionary = PyDictionary()


# Returns a dictionary of the definition of a word
def definition(word):
    return dictionary.meaning(word)


# Returns a list of synonyms for a word
def synonyms(word):
    return dictionary.synonym(word)


# Returns a list of antonyms for a word
def antonyms(word):
    return dictionary.antonym(word)

