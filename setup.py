from setuptools import setup, find_packages

setup(
    name='mocktail',
    version='0.0.1',
    url='https://github.com/koirikivi/mocktail.git',
    author='Rainer Koirikivi',
    author_email='rainer@koirikivi.fi',
    description='Non-alcoholic Mockito-style when-then utilities for unittest.mock',
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
