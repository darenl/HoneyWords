import math

class HoneyWordFactory:
    def __init__(self, training_data = None):
        self.T = training_data
    
    def create_honeyword(self, password):
        return password + '111'

    @staticmethod
    def sequence(password):
        seq = []
        return seq

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