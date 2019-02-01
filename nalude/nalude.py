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
date     : Jan 31, 2019
email    : Nasy <nasyxx+nalude@gmail.com>
filename : nalude.py
project  : nalude
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
from typing import Tuple, Callable, Sequence, Generator
from functools import reduce

# Local Packages
from .types import G, Num, Predicate, a, b, c

# ----------------------------------------------------------------------
# Folds and Traversals
# ----------------------------------------------------------------------


def foldl(func: Callable[[b, a], b], init: b, t: Sequence[a]) -> b:
    """Left-associative fold of a sequence."""
    return reduce(func, t, init)


def foldr(func: Callable[[a, b], b], init: b, t: Sequence[a]) -> b:
    """Right-associative fold of a sequence."""
    return reduce(flip(func), reversed(t), init)


def foldl1(func: Callable[[a, a], a], t: Sequence[a]) -> a:
    """Left-associative fold of a sequence.

    This is avariant of foldl without base case.
    """
    t_ = iter(t)
    return reduce(func, t_, next(t_))


def foldr1(func: Callable[[a, a], a], t: Sequence[a]) -> a:
    """Right-associative fold of a sequence.

    This is a variant of foldr without base case.
    """
    t_ = iter(reversed(t))
    return reduce(func, t_, next(t_))


def product(nums: Sequence[Num]) -> Num:
    """Computes the product of the numbers."""
    return foldl1(lambda b, a: a * b, nums)


# ----------------------------------------------------------------------
# Lists
# ----------------------------------------------------------------------


def head(xs: Sequence[a]) -> a:
    """Extract the first element of a sequence."""
    try:
        return next(iter(xs))
    except StopIteration:
        raise IndexError("Sequence is empty.")


def tail(xs: Sequence[a]) -> G:
    """Extract the elements after the head of a sequence."""
    try:
        ixs = iter(xs)
        next(ixs)
        for x in ixs:
            yield x
    except StopIteration:
        raise IndexError("Sequence is empty.")


def last(xs: Sequence[a]) -> a:
    """Extract the last element of a sequence."""
    try:
        return next(iter(reversed(xs)))
    except StopIteration:
        raise IndexError("Sequence is empty.")


def init(xs: Sequence[a]) -> G:
    """Extract all the elements of a sequence except the last one."""
    ixs = iter(xs)
    try:
        x_ = next(ixs)
        n = True
        while n:
            try:
                x = next(ixs)
                yield x_
                x_ = x
            except StopIteration:
                n = False
    except StopIteration:
        raise IndexError("Sequence is empty.")


def null(l: Sequence[a]) -> bool:
    """Test whether the sequence is empty."""
    try:
        next(iter(l))
        return False
    except StopIteration:
        return True


def iterate(f: Callable[[a], a], x: a) -> Generator[Tuple[a, ...], None, None]:
    """Yield a tuple of repeated applications of f to x."""
    res = []
    while True:
        res.append(x)
        yield tuple(res)
        x = f(x)


def repeat(x: a) -> G:
    """Repeat x."""
    while True:
        yield x


def replicate(n: int, x: a) -> G:
    """Return a iterator of length n with x the value of every element."""
    for _ in range(n):
        yield x


def cycle(xs: Sequence[a]) -> G:
    """Tie a sequence to infinite circuler one."""
    xs_ = []  # if x is a finite iterator, this can save the value.
    for x in xs:
        yield x
        xs_.append(x)
    while True:
        for x in xs_:
            yield x


def take(n: int, xs: Sequence[a]) -> G:
    """Return the first n elements of sequence xs."""
    for _, x in zip(range(n), xs):
        yield x


def drop(n: int, xs: Sequence[a]) -> G:
    """Return the remaining elements of xs after the first n elements."""
    ixs = iter(xs)
    try:
        for _ in range(n):
            next(ixs)
        while True:
            yield next(ixs)
    except StopIteration:
        pass


def splitat(n: int, xs: Sequence[a]) -> Tuple[G, G]:
    """Equal to (take(n, xs), drop(n, xs)).

    Return a tuple where the first element is xs prefix of length n and second
    element is the remainder of the sequence xs.
    """
    return (take(n, xs), drop(n, xs))


def takewhile(p: Predicate, xs: Sequence[a]) -> G:
    """Return the longest prefix of xs of elements that satisfy predicate p."""
    for x in xs:
        if p(x):
            yield x
        else:
            break


def dropwhile(p: Predicate, xs: Sequence[a]) -> G:
    """Returns the suffix remaining after takewhile(p, xs)."""
    ixs = iter(xs)
    for x in ixs:
        if not p(x):
            yield x
            break
    for x in xs:
        yield x


def span(p: Predicate, xs: Sequence[a]) -> Tuple[G, G]:
    """Equal to (takewhile(p, xs), dropwhile(p, xs))."""
    return takewhile(p, xs), dropwhile(p, xs)


def break_(p: Predicate, xs: Sequence[a]) -> Tuple[G, G]:
    """Equal to (takewhile(not_(p), xs), dropwhile(not_(p), xs))."""
    return takewhile(not_(p), xs), dropwhile(not_(p), xs)


# ----------------------------------------------------------------------
# Miscellaneous
# ----------------------------------------------------------------------


def flip(f: Callable[[a, b], c]) -> Callable[[b, a], c]:
    """Flip takes its two arguments into the reverse order of f.

    >>> flip(f)(b, a) == f(a, b)
    """
    return lambda b_, a_: f(a_, b_)


def o(f1: Callable[[b], c], f2: Callable[[a], b]) -> Callable[[a], c]:
    """Function composition.

    >>> o(f1, f2)(a) == f1(f2(a))
    """
    return lambda a_: f1(f2(a_))


# ----------------------------------------------------------------------
# Specials
# ----------------------------------------------------------------------


def not_(f: Callable[..., bool]) -> Callable[..., bool]:
    """Boolean "not"."""

    def _wrap(*args: a, **kwds: b) -> bool:
        """Wrapper of not_."""
        return f(*args, **kwds)

    return _wrap
