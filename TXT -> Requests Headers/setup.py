from setuptools import setup, find_packages

setup(
    name = 'tth',
    version="1.0",
    description = 'Turns text to dict headers.',
    author = 'novitae',
    url = 'https://github.com/novitae/Aet-s-Tools',
    classifiers = [
        'Programming Language :: Python :: 3.9',
    ],
    packages = find_packages(),
    entry_points = {'console_scripts': ['tth = tth.tth:fromCLI']}
)
