from pathlib import Path
from setuptools import setup

current_dir = Path(__file__).parent.resolve()
with open(current_dir / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'floem',
    packages = ['floem'],
    version = '0.1.1',
    author = 'BTaskaya',
    author_email = 'batuhanosmantaskaya@gmail.com',
    url = 'https://btaskaya/floem',
    description = 'Segmented Python preprocessor.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
)
