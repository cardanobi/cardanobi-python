import pathlib
from setuptools import setup, find_packages

LOC = pathlib.Path(__file__).parent

long_description = (LOC / 'README.md').read_text(encoding='utf-8')

setup(
    name='cardanobi-python',
    version='0.1.0',
    description='Python 3 SDK for the CardanoBI API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cardanobi/cardanobi-python',
    author='cardanobi.io',
    author_email='contact@cardanobi.io',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'aiohttp>=3.7',
    ],
    python_requires='>=3.7',
)