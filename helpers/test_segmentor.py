from unittest import TestCase
from segmentor import Segmentor
import nltk

digits = [i*4 for i in '0123456789'] + [i*3 for i in '0123456789'] + ['1234','123456789']
brown = nltk.corpus.brown.words()

seg = Segmentor(corpus= brown + digits)

class SegmentorTest(TestCase):
    def test_segmentor_can_split(self):
        splitted = [('a','bc'), ('ab','c'), ('abc','')]
        self.assertEqual(seg.splits('abc'), splitted)

    def test_segmentor_can_calc_probability(self):
        self.assertTrue(seg.Pwords(['giant','pear']) > 0)

    def test_segmentor_can_break_up_word(self):
        self.assertEqual(seg.segment('appletree'), ['apple', 'tree'])

    def test_segmentor_can_break_up_password(self):
        self.assertEqual(seg.segment('puppy1234'), ['puppy', '1234'])
        