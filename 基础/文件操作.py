from pathlib import Path
import os

p = Path('.')
print(list(p.glob('**/*.py')))

os.getcwd()

file = open('./ceshi.txt', 'a')
file.write('abc')
file.close()