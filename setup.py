from setuptools import setup

setup(
    name="define",
    version='0.12',
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
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'define=main:get_definition'
        ],
    }
)