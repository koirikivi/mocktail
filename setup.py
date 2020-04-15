from setuptools import setup, find_packages

setup(
    name='mock-when',
    version='0.0.1',
    url='https://github.com/koirikivi/mock-when.git',
    author='Rainer Koirikivi',
    author_email='rainer@koirikivi.fi',
    description='Dead-simple Mockito-style when-then utilities for unittest mock',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'testing': [
            'pytest',
            'pytest-watch',
            'flake8',
        ]
    }
)
