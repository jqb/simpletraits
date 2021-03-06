# -*- coding: utf-8 -*-
from .utils import collect_attribute, chain


class NIL(object):
    def __nonzero__(self):
        return False

    def __str__(self):
        return u'<NIL>'

    __repr__ = __unicode__ = __str__


NIL = NIL()


# TODO: make use of it, document it
class lazy(object):
    def __init__(self, toinvoke, *args, **kwargs):
        self.toinvoke = toinvoke
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.toinvoke(*self.args, **self.kwargs)


class kwa(object):
    def __init__(self, name, default=NIL):
        self.name = name
        self.default = default


class basemeta(type):
    def __new__(cls, cls_name, bases, attrs):
        super_new = super(basemeta, cls).__new__

        _arg = attrs.pop('_arg', ())
        _kwa = attrs.pop('_kwa', ())

        if not isinstance(_arg, tuple):
            raise TypeError('"_arg" variable of class "%s" need to be a tuple' % (
                cls
            ))

        if not isinstance(_kwa, (tuple, dict)):
            raise TypeError('"_kwa" variable of class "%s" need to be a tuple OR dict' % (
                cls
            ))

        if isinstance(_kwa, dict):
            _kwa = attrs['_kwa'] = tuple([kwa(name, _kwa[name]) for name in _kwa])
        else:
            _kwa = attrs['_kwa'] = tuple([
                kw if isinstance(kw, kwa) else kwa(kw)
                for kw in _kwa
            ])

        args = collect_attribute('_arg', bases[::-1]) + [list(_arg)]
        kwas = collect_attribute('_kwa', bases[::-1]) + [list(_kwa)]

        attrs['_arg'] = _arg = tuple(chain(*args))
        attrs['_kwa'] = _kwa = tuple(chain(*kwas))

        new_class = super_new(cls, cls_name, bases, attrs)
        return new_class


    def __call__(cls, *args, **kwargs):
        self = type.__call__(cls, *args, **kwargs)
        return self


class baseclass(object):
    __metaclass__ = basemeta

    _arg = ()
    _kwa = ()

    def __init__(self, *args, **kwargs):  # just need to be defined
        self._validate_args(args)
        self._set_args(args)
        self._validate_kwargs(kwargs)
        self._set_kwargs(kwargs)

    def _validate_args(self, args):
        assert len(args) == len(self.__class__._arg), \
            "There should be exactly %s arguments but there is %s" % (
                len(self.__class__._arg), len(args)
            )

    def _set_args(self, args):
        for index, attrname in enumerate(self.__class__._arg):
            setattr(self, attrname, args[index])

    def _validate_kwargs(self, kwargs):
        pass

    def _set_kwargs(self, kwargs):
        allkwargs = [
            (kwarg.name, kwarg.default) if isinstance(kwarg, kwa) else (kwarg, NIL)
            for kwarg in self.__class__._kwa
        ]

        for name, default in allkwargs:
            val = kwargs.pop(name, NIL)

            if val == NIL:
                val = getattr(self.__class__, name, default)

            try:
                val = val()
            except TypeError:  # not callable
                pass
            setattr(self, name, val)

        if kwargs:
            raise AttributeError("%s key word attributes are not supported with %s" % (
                kwargs.keys(), self.__class__.__name__
            ))
