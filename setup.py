# encoding: utf-8
#
# Copyright 2020 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.
#
# MCL Sickbay: a clinical data prototype

import setuptools, os.path


_requirements = [
    'setuptools',
    'psycopg2',
    'sqlalchemy'
]


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), 'r') as f: desc = f.read()


setuptools.setup(
    name='mcl.sickbay',
    version='0.0.0',
    description='MCL Sickbay, a Clinical Data Prototype',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Sean Kelly',
    author_email='sean.kelly@jpl.nasa.gov',
    url='https://github.com/MCLConsortium/mcl.sickbay',
    namespace_packages=['mcl'],
    test_suite='mcl.sickbay.tests.test_suite',
    packages=setuptools.find_packages('src', exclude=['docs', 'bootstrap']),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'create-demo-db=mcl.sickbay.db:demo'
        ],
    },
    package_data={
        '': ['*.txt', '*.md', '*.rst']
    },
    include_package_data=True,
    zip_safe=True,
    install_requires=_requirements,
    extras_require={'test': []},
    license='ALv2',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
