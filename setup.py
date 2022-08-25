from setuptools import setup

setup(
    name='WikiCLI',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        main=main:cli
    ''',
)