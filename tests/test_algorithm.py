from unittest import TestCase
from pathlib import Path
import os
import subprocess

class AlgorithmTest(TestCase):
    def test_algorithm_reads_pws_and_outputs_honeywords(self):
        input_fname = "tests/passwords.txt"
        output_fname = "output.txt"
        num_honeywords = 4
        
        run_command = ["python", "algorithm1.py", str(num_honeywords), input_fname, output_fname]
        px = subprocess.run(run_command, stdout=subprocess.PIPE)

        output = Path(output_fname)
        self.assertTrue(output.is_file())
        
        with open(input_fname, 'r') as input_f:
            num_lines = len(input_f.readlines())

        with open(output_fname, 'r') as output_f:
            lines = output_f.readlines()
            self.assertEqual(num_lines,len(lines))

            honeys_per_line = len(lines[0].split(','))
            self.assertEqual(honeys_per_line, num_honeywords)
        
        os.remove(output_fname)

    def test_algorithm_can_make_honeywords(self):
        input_fname = "tests/passwords.txt"
        output_fname = "some_output.txt"
        num_honeywords = 20
        
        run_command = ["python", "algorithm1.py", str(num_honeywords), input_fname, output_fname]
        px = subprocess.run(run_command, stdout=subprocess.PIPE)

        output = Path(output_fname)
        self.assertTrue(output.is_file())
        
        with open(input_fname, 'r') as input_f:
            num_lines = len(input_f.readlines())

        with open(output_fname, 'r') as output_f:
            lines = output_f.readlines()
            self.assertEqual(num_lines,len(lines))

            honeys_per_line = len(lines[0].split(','))
            self.assertEqual(honeys_per_line, num_honeywords)

        os.remove(output_fname)