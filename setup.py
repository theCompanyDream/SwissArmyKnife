try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Timothy Brantley II',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'brantleyiit@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'jinja2'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Email'
}

setup(**config)
