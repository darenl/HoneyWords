from unittest import TestCase
from honey_word_factory import HoneyWordFactory


class HoneyWordFactoryTest(TestCase):
    def test_hwf_can_create_honeyword(self):
        hwf = HoneyWordFactory()
        test_pw = 'password1'
        self.assertNotEqual(test_pw, hwf.create_honeyword(test_pw))