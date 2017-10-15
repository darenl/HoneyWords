import sys
from honey_word_factory.honey_word_factory import HoneyWordFactory

#algorithm1.py, n, input_file, output_file
_, n, input_file, output_file = sys.argv

with open(input_file,'r') as real_pwf:
    passwords = real_pwf.read().splitlines()

hwf = HoneyWordFactory()

with open(output_file, 'w') as honeyfile:
    for password in passwords:
        line = ','.join([hwf.create_honeyword(password) for i in range(int(n))])
        honeyfile.write(line + '\n')
