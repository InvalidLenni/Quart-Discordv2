"""
Quart-Discord
-------------

An Discord OAuth2 quart extension.
"""

import re
import os

from setuptools import setup, find_packages


def __get_version():
    with open("quart_discord/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)


requirements = [
    'Quart',
    'pyjwt',
    'oauthlib',
    'Async-OAuthlib',
    'cachetools'
]


on_rtd = os.getenv('READTHEDOCS') == 'True'
if on_rtd:
    requirements.append('sphinxcontrib-napoleon')
    requirements.append('Pallets-Sphinx-Themes')

extra_requirements = {
    'docs': [
        'sphinx==1.8.3'
    ]
}


setup(
    name='Quart-Discordv2',
    version=__get_version(),
    url='https://github.com/InvalidLenni/Quart-Discordv2',
    license='MIT',
    author='Lennard M.',
    author_email='lenni.ghost.m@gmail.com',
    description='Discord OAuth2 extension for Quart.',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    extra_requirements=extra_requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
