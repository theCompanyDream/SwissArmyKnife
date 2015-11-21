try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Timothy Brantley II',
    'url': '',
    'download_url': '',
    'author_email': 'brantleyiit@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'jinja2'],
    'packages': ['sync', 'email'],
    'scripts': [],
    'name': 'AutomatedServices'
}

setup(**config)
