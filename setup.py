#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', encoding='utf-8') as history_file:
    history = history_file.read()

install_requires = [
    "numpy>=1.18.0,<1.20.0;python_version<'3.7'",
    "numpy>=1.20.0,<2;python_version>='3.7'",
    'pandas>=1.1.3,<2',
    'torch>=1.8.0,<2',
    'tqdm>=4.15,<5',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'pytest-rerunfailures>=9.0.0,<10',
    'jupyter>=1.0.0,<2',
    'rundoc>=0.4.3,<0.5',
]

development_requires = [
    # general
    'setuptools<49.2',
    'bumpversion>=0.5.3,<0.6',
    'pip>=9.0.1',
    'watchdog>=0.8.3,<0.11',

    # style check
    'flake8>=3.7.7,<4',
    'flake8-absolute-import>=1.0,<2',
    'flake8-docstrings>=1.5.0,<2',
    'flake8-sfs>=0.0.3,<0.1',
    'isort>=4.3.4,<5',
    'pylint>=2.5.3,<3',
    'flake8-builtins>=1.5.3,<1.6',
    'flake8-debugger>=4.0.0,<4.1',
    'flake8-mock>=0.3,<0.4',
    'dlint>=0.11.0,<0.12',
    'flake8-eradicate>=1.1.0,<1.2',
    'flake8-mutable>=1.2.0,<1.3',
    'flake8-fixme>=1.1.1,<1.2',
    'flake8-multiline-containers>=0.0.18,<0.1',
    'flake8-quotes>=3.3.0,<4',
    'flake8-variables-names>=0.0.4,<0.1',
    'pep8-naming>=0.12.1,<0.13',
    'flake8-expression-complexity>=0.0.9,<0.1',
    'flake8-print>=4.0.0,<4.1',

    # fix style issues
    'autoflake>=1.1,<2',
    'autopep8>=1.4.3,<1.6',

    # distribute on PyPI
    'twine>=1.10.0,<4',
    'wheel>=0.30.0',

    # Advanced testing
    'coverage>=4.5.1,<6',
    'tox>=2.9.1,<4',

    # Invoking test commands
    'invoke'
]

setup(
    author='DataCebo, Inc.',
    author_email='info@sdv.dev',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    description='Create sequential synthetic data of mixed types using a GAN.',
    extras_require={
        'test': tests_require,
        'dev': development_requires + tests_require,
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords='deepecho deepecho DeepEcho',
    license='BSL-1.1',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='deepecho',
    packages=find_packages(include=['deepecho', 'deepecho.*']),
    python_requires='>=3.6,<3.10',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/sdv-dev/DeepEcho',
    version='0.3.1.dev0',
    zip_safe=False,
)
