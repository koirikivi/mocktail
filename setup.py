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
    },
    keywords=['testing', 'mock', 'unittest', 'mockito', 'when'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
