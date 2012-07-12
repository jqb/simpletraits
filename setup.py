# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import simpletraits


setup(
    name='simpletraits',
    version=simpletraits.VERSION,
    description='',
    author='Kuba Janoszek',
    author_email='kuba.janoszek@gmail.com',
    include_package_data=True,
    url='https://github.com/jqb/simpletraits/tree/ver-%s' % simpletraits.VERSION,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
