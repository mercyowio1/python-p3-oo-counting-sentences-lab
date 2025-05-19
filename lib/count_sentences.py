#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, sentence=""):
        self._sentence = ""
        self.sentence = sentence

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, value):
        if isinstance(value, str):
            self._sentence = value
        else:
            print("The value must be a string.")

    # Alias `value` to `sentence`
    value = property(
        fget=lambda self: self.sentence,
        fset=lambda self, val: setattr(self, 'sentence', val)
    )
    
    def is_sentence(self):
        return self._sentence.endswith(".")

    def is_question(self):
        return self._sentence.endswith("?")

    def is_exclamation(self):
        return self._sentence.endswith("!")

    def count_sentences(self):
        return len(re.findall(r'[^.!?]+[.!?]', self._sentence))