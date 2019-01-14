from setuptools import setup

setup(
    name = 'pypassgen',
    version = '0.1.0',
    packages = ['pypassgen'],
    entry_points = {
        'console_scripts': [
            'pypassgen = pypassgen.__main__:main'
        ]
    })
