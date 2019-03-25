try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My SAS Training Plan',
        'author': 'Alan',
        'url': 'URL to find it',
        'download': 'URL to download it',
        'author_email': 'my email',
        'version': '0.1',
        'install_requires': 'nose',
        'packages': ['NAME'],
        'scripts': [],
        'name': 'training',
        }

setup(**config)
