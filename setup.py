# -*- coding: utf-8 -*-
"""Installer for the forests.content package."""

from setuptools import find_packages, setup

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

version = '1.0a1'

setup(
    name='forests.content',
    version=version,
    description="FORESTS Content",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='"EEA: IDM2 S-Team"',
    author_email='Christian.Prosperini@eea.europa.eu',
    url='https://pypi.python.org/pypi/forests.content',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['forests'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'requests',
        # 'plone.app.iterate >= 3.3.1',
        # 'plone.app.contenttypes',
        # 'plone.directives.dexterity',
        # 'plone.directives.form',
        # 'python-redmine',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ],
    },
)
