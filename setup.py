try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Brave The Dungeon, text based dungeon RPG',
    'author': 'Aaron Merten',
    'url': 'https://github.com/mertenar',
    'download_url': 'download location TBD.',
    'author_email': 'mertenar@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Brave_The_Dungeon'],
    'scripts': [],
    'name': 'Brave The Dungeon'
}

setup(**config)
