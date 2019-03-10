#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Feb 15, 2019
email    : Nasy <nasyxx+nalude@gmail.com>
filename : extra.py
project  : nalude
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
from typing import Type, Tuple, Iterable

# Local Packages
from .types import G, a


def flatten(xs: a, *, ignore: Tuple[Type, ...] = (dict,)) -> G:
    """Flatten iterables of iterable to a single one.

    The true type of it is:: `T = Iterable[Untion[a, T]]` ."""
    if not (isinstance(xs, (str, *ignore)) or not isinstance(xs, Iterable)):
        for x in xs:
            for x_ in flatten(x, ignore=ignore):
                yield x_
    else:
        yield xs
