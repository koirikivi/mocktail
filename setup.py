from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mocktail',
    version='0.0.2',
    url='https://github.com/koirikivi/mocktail.git',
    author='Rainer Koirikivi',
    author_email='rainer@koirikivi.fi',
    description='Non-alcoholic Mockito-style when-then utilities for unittest.mock',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'testing': [
            'pytest',
            'pytest-watch',
            'flake8',
        ]
    },
    keywords=['testing', 'mock', 'unittest', 'mockito', 'when'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
