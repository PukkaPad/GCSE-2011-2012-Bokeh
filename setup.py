try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Analysis of GCSE data',
    'author': 'Mariana Souza',
    'url': 'https://www.theguardian.com/news/datablog/2012/jan/26/secondary-school-league-tables-data',
    'download_url': '',
    'author_email': 'xxxxx.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['GCSE_normalized.py', 'bokeh_categorical.py'],
    'name': 'GCSE-2011-2012-data-Bokeh'
}

setup(**config)