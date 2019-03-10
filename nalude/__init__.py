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
date     : Jan 30, 2019
email    : Nasy <nasyxx+nalude@gmail.com>
filename : __init__.py
project  : nalude
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
__version__ = "0.3.0"
# Local Packages
from .extra import flatten
from .nalude import (o, fst, id_, snd, all_, any_, drop, flip, head, init,
                     last, not_, null, span, tail, take, const, curry,
                     cycle, foldl, foldr, lines, until, unzip, words,
                     break_, concat, foldl1, foldr1, repeat, iterate,
                     product, splitat, uncurry, unlines, unwords, zipwith,
                     concatmap, dropwhile, replicate, takewhile,)

if __name__ == "__main__":
    # Folds and Traversals
    assert foldl
    assert foldl1
    assert foldr
    assert foldr1
    assert product

    # Lists
    assert head
    assert last
    assert init
    assert tail
    assert null
    assert iterate
    assert repeat
    assert replicate
    assert cycle
    assert take
    assert drop
    assert splitat
    assert takewhile
    assert dropwhile
    assert span
    assert break_

    # Miscellaneous
    assert id_
    assert const
    assert flip
    assert o
    assert until

    # String
    assert lines
    assert unlines
    assert words
    assert unwords

    # Specials
    assert not_
    assert all_
    assert any_
    assert concat
    assert concatmap

    # TUple
    assert fst
    assert snd
    assert curry
    assert uncurry

    # Zip and Unzip
    assert zipwith
    assert unzip

    # Extra
    assert flatten
