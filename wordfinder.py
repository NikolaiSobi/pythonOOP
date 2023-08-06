#!/usr/bin/env python3
"""Word Finder: finds random words from a dictionary."""
import random
words = []


#  with open("/home/nikolai/springboard/exercises/pythonOOP/words.txt") as file:
#      for i in file:
#          words.append(i.strip())

class WordFinder:
    def __init__(self, location):
        location = open(location)
        self.words = self.add_to_list(location)
        

    def find_word(self):
        return words[random.randint(0, len(words))]
    
    def add_to_list(self, location):
        with location as file:
            for i in file:
                words.append(i.strip())

class SpecialWordFinder(WordFinder):
    def add_to_list(self, location):
        with location as file:
            for i in file:
                if i.strip() and i[0] != "#":
                    words.append(i.strip()) 

