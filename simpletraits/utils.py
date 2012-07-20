# -*- coding: utf-8 -*-
from itertools import chain

def collect_attribute(attr_name, objects, filterfun=lambda attr: attr is not None):
    result = []
    for obj in objects:
        attr = getattr(obj, attr_name, None)
        if filterfun(attr):
            result.append(attr)
    return result
