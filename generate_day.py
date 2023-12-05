import os
import argparse

parser = argparse.ArgumentParser(description='Make new day\'s directory structure')
parser.add_argument('name', type=str, help='Name of directory')

args = parser.parse_args()

dir_name = args.name

lines = None
with open('template.py') as fin:
    lines = fin.readlines()

os.mkdir(dir_name)
os.chdir(dir_name)

with open('problem1.py', 'w') as fout:
    for line in lines:
        fout.write(line)

with open('problem2.py', 'w') as fout:
    for line in lines:
        fout.write(line)

with open('input.txt', 'w'):
    pass

with open('sample.txt', 'w'):
    pass