import os
import psutil
from pkg_resources import parse_version
from setuptools import setup, find_packages, __version__ as setuptools_version
from distutils.core import setup

setup(
    name='RBQ',
    version=2.0,
    url='http://saber.love',
    description='RBQ fuck',
    long_description=open('README.rst').read(),
    author='allvulples',
    maintainer='Demonkeyse Manell',
    author_email='allvulples@outlook.com',
    license='GPLv2',
    packages=['source','badapple','badapple/__MACOSX'],
    classifiers=[
        'Framework :: RBQ',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'psutil >= 5.2.2'
    ],
)
