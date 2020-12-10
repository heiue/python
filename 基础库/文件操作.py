from pathlib import Path
import os

p = Path('.')
print(list(p.glob('**/*.py')))

os.getcwd()