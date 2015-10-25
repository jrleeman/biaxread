try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'biaxtools',
    'author': 'John R. Leeman',
    'url': 'Project URL https://github.com/jrleeman/biaxtools',
    'download_url': 'https://github.com/jrleeman/biaxtools',
    'author_email': 'kd5wxb@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'numpy', 'matplotlib'],
    'packages': ['biaxtools'],
    'scripts': [],
    'name': 'biaxtools'
}

setup(**config)
