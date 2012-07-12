simpletraits
============

ver 0.1-beta

Lightweight lib that makes creation of python class less verbose.


Usage
=====

I'm constantly repeating attributes names for simple python classes.
So instead of this ::

    class User(object):
        def __init__(self, login, name, last_name, email=None):
            self.login = login
            self.name = name
            self.last_name = last_name
            self.email = email


I prefere to do this ::

    from simpletraits import baseclass

    class User(baseclass):
        _arg = ('login', 'name', 'last_name')
        _kwa = ('email', )


It does exactly the same thing, except that there's less code.


Details
-------

As may you expect "_arg" is telling the basaclass how many and
what are the names of *args for the object canstructor. "_kwa"
tells what are the names of the keyword arguments.


The default value for each keyword arg is ``simpletraits.NIL``.
If you want to add your own defaults you have two options:


1) make use of ``simpletraits.kwa`` objects::

    from simpletraits import baseclass, kwa

    class User(baseclass):
        _kwa = (kwa('email', 'default@email.com'), )


2) you can just asign dict to ``_kwa`` class variable::

    from simpletraits import baseclass

    class User(baseclass):
        _kwa = dict(
            email = 'default@email.com',
        )


Tests
-----

To run tests simply download / clone package and type ::

    $> python tests.py


Authors
-------

* Jakub Janoszek (kuba.janoszek@gmail.com)
