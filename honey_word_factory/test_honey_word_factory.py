from unittest import TestCase
from honey_word_factory.honey_word_factory import HoneyWordFactory


class HoneyWordFactoryTest(TestCase):
    def test_hwf_can_create_honeyword(self):
        hwf = HoneyWordFactory()
        test_pw = 'password1'
        honeyword1 = hwf.create_honeyword(test_pw)
        
        self.assertNotEqual(test_pw, honeyword1)
    
    def test_hwf_can_create_random_honeyword(self):
        hwf = HoneyWordFactory()
        test_pw = 'securityissecure'
        honeyword1 = hwf.create_honeyword(test_pw)
        honeyword2 = hwf.create_honeyword(test_pw)
        
        self.assertNotEqual(honeyword1, honeyword2)

    def test_hwf_can_calculate_entropy(self):
        ent1 = HoneyWordFactory.calc_entropy('password1')
        ent2 = HoneyWordFactory.calc_entropy('WhatsMYname?123')
        ent3 = HoneyWordFactory.calc_entropy('q72j4rac98cgq!@#$')

        self.assertTrue(ent2 > ent1)
        self.assertTrue(ent3 > ent2)
        

