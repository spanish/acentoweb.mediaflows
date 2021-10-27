# -*- coding: utf-8 -*-
"""Installer for the acentoweb.mediaflows package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='acentoweb.mediaflows',
    version='1.0a2',
    description="Mediaflows add-on for Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Acento Web',
    author_email='correo@acentoweb.com',
    url='https://github.com/collective/acentoweb.mediaflows',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/acentoweb.mediaflows',
        'Source': 'https://github.com/collective/acentoweb.mediaflows',
        'Tracker': 'https://github.com/collective/acentoweb.mediaflows/issues',
        # 'Documentation': 'https://acentoweb.mediaflows.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['acentoweb'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
        'plone.app.relationfield',
        'plone.app.vocabularies',
        'collective.easyform>=3.0.5',
        'collective.taxonomy>=2.1.0'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = acentoweb.mediaflows.locales.update:update_locale
    """,
)
