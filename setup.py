from setuptools import setup

setup(
    name="define",
    version='0.11',
    py_modules=[
        'main', 
        'lib.dictionary',
        'lib.reader',
        'lib.definition',
        'lib.configs'
        ],
    install_requires=[
        'Click',
        'pyyaml',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        define=main:lookup
    ''',
)