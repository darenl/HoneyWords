from collections import defaultdict, Counter
import math
import random
import nltk
from helpers.segmentor import Segmentor

class HoneyWordFactory:
    def __init__(self, training_data = None):
        self.T = training_data
        ints = '0123456789'
        self.digits = [i*4 for i in ints] + [i*3 for i in ints] + ['1234',ints]
        self.brown = nltk.corpus.brown.words()
        self.pos_words = self.build_pos_dict()
        self.seg = Segmentor(corpus= self.brown + self.digits)

    def build_pos_dict(self):
        counts = Counter(self.brown)
        tagged = nltk.corpus.brown.tagged_words(tagset='universal')
        words = defaultdict(list)
        for word, pos in tagged:
            if counts[word] < 100 and counts[word] > 5:
                words[pos].append(word)
        return words

    def create_honeyword(self, password):
        return self.tweak(password)
    
    def tweak(self, password):
        words = self.seg.segment(password)
        parts_of_speech = nltk.pos_tag(words, tagset='universal')

        index = random.randint(0,len(words)-1)
        pos = parts_of_speech[index][1]
        
        if pos == 'CD':
            tweaked_num = str(int(words[index]) + 1)
            words[index] = random.choice(self.digits + [tweaked_num]*random.randint(0,len(self.digits)))
        else:
            words[index] = random.choice(self.pos_words[pos])
        return ''.join(words)

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