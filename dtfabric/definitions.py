# -*- coding: utf-8 -*-
"""Definitions."""

from __future__ import unicode_literals


BYTE_ORDER_BIG_ENDIAN = 'big-endian'
BYTE_ORDER_LITTLE_ENDIAN = 'little-endian'
BYTE_ORDER_MIDDLE_ENDIAN = 'middle-endian'
BYTE_ORDER_NATIVE = 'native'

BYTE_ORDERS = frozenset([
    BYTE_ORDER_BIG_ENDIAN,
    BYTE_ORDER_LITTLE_ENDIAN,
    BYTE_ORDER_NATIVE])

FORMAT_SIGNED = 'signed'
FORMAT_UNSIGNED = 'unsigned'

SIZE_NATIVE = 'native'

TYPE_INDICATOR_BOOLEAN = 'boolean'
TYPE_INDICATOR_CHARACTER = 'character'
TYPE_INDICATOR_CONSTANT = 'constant'
TYPE_INDICATOR_ENUMERATION = 'enumeration'
TYPE_INDICATOR_FLOATING_POINT = 'floating-point'
TYPE_INDICATOR_FORMAT = 'format'
TYPE_INDICATOR_INTEGER = 'integer'
TYPE_INDICATOR_SEQUENCE = 'sequence'
TYPE_INDICATOR_STREAM = 'stream'
TYPE_INDICATOR_STRING = 'string'
TYPE_INDICATOR_STRUCTURE = 'structure'
TYPE_INDICATOR_UNION = 'union'
TYPE_INDICATOR_UUID = 'uuid'

TYPE_INDICATORS = frozenset([
    TYPE_INDICATOR_BOOLEAN,
    TYPE_INDICATOR_CHARACTER,
    TYPE_INDICATOR_CONSTANT,
    TYPE_INDICATOR_ENUMERATION,
    TYPE_INDICATOR_FLOATING_POINT,
    TYPE_INDICATOR_FORMAT,
    TYPE_INDICATOR_INTEGER,
    TYPE_INDICATOR_SEQUENCE,
    TYPE_INDICATOR_STREAM,
    TYPE_INDICATOR_STRING,
    TYPE_INDICATOR_STRUCTURE,
    TYPE_INDICATOR_UNION,
    TYPE_INDICATOR_UUID])
