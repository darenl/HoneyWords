
from collections import Counter
import re, nltk, functools, operator

class Segmentor:
    """
    Segmentor segments given password:
    "passwordpie" -> ["password", "pie"]

    # Code mostly taken from the link below
    # https://stackoverflow.com/questions/38125281/split-sentence-without-space-in-python-nltk
    """
    def __init__(self, corpus=nltk.corpus.brown.words()):
        dig4 = [i*4 for i in '0123456789'] 
        dig3 = [i*3 for i in '0123456789']
        digpattern = ['1234','123456789']
        likely_numbers = dig4+dig3+digpattern
        self.WORDS = corpus + likely_numbers
        self.COUNTS = Counter(self.WORDS)
        self.N = sum(self.COUNTS.values()) # Number of words in Brown
    
    def P(self, word):
         return self.COUNTS[word]/self.N

    def Pwords(self, words):
        "Probability of words, assuming each word is independent of others."
        return functools.reduce(operator.mul, [self.P(w) for w in words], 1)

    def splits(self, text, start=1, L=10):
        "Return a list of all (first, rest) pairs; start <= len(first) <= L."
        return [(text[:i], text[i:]) 
                for i in range(start, min(len(text), L)+1)]

    def segment(self, text):
        "Return a list of words that is the most probable segmentation of text."
        if not text: 
            return []
        candidates = [[first] + self.segment(rest) 
                        for (first, rest) in self.splits(text)]
        pwords = lambda x :self.Pwords(x) 
        return max(candidates, key=pwords)