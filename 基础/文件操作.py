from pathlib import Path
import os

p = Path('.')
print(list(p.glob('**/*.py')))

os.getcwd()

file = open('./ceshi.txt', 'r+')
# print(file.readline())
# file.seek(9)
# print(file.readline())
# print(file.tell())
print(file.write('i like you'))
file.close()

