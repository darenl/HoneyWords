import math
import random
import nltk
from helpers.segmentor import Segmentor

class HoneyWordFactory:
    def __init__(self, training_data = None):
        self.T = training_data
        self.digits = [i*4 for i in '0123456789'] + [i*3 for i in '0123456789'] + ['1234','123456789']
        self.brown = nltk.corpus.brown.words()
        self.seg = Segmentor(corpus= self.brown + self.digits)

    def create_honeyword(self, password):
        words = self.seg.segment(password))
        parts_of_speech = nltk.pos_tag(words)

        return password + str(random.randint(0,9))*random.randint(1,3)

    @staticmethod
    def calc_entropy(string):
        """
        Calculates the Shannon entropy of a string. 
        Taken from https://stackoverflow.com/questions/2979174/how-do-i-compute-the-approximate-entropy-of-a-bit-string
        """

        # get probability of chars in string
        prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
        entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
        return entropy