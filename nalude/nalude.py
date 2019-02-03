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
from typing import List, Tuple, Callable, Sequence, Generator
from functools import reduce

# Local Packages
from .types import G, Num, Predicate, a, b, c

# ----------------------------------------------------------------------
# Folds and Traversals
# ----------------------------------------------------------------------


def foldl(f: Callable[[b, a], b], init: b, t: Sequence[a]) -> b:
    """Left-associative fold of a sequence."""
    return reduce(f, t, init)


def foldr(f: Callable[[a, b], b], init: b, t: Sequence[a]) -> b:
    """Right-associative fold of a sequence."""
    return reduce(flip(f), reversed(t), init)


def foldl1(f: Callable[[a, a], a], t: Sequence[a]) -> a:
    """Left-associative fold of a sequence.

    This is avariant of foldl without base case.
    """
    t_ = iter(t)
    try:
        return reduce(f, t_, next(t_))
    except StopIteration:
        raise IndexError("Sequence is Empty")


def foldr1(f: Callable[[a, a], a], t: Sequence[a]) -> a:
    """Right-associative fold of a sequence.

    This is a variant of foldr without base case.
    """
    t_ = iter(reversed(t))
    try:
        return reduce(f, t_, next(t_))
    except StopIteration:
        raise IndexError("Sequence is Empty")


def product(nums: Sequence[Num]) -> Num:
    """Computes the product of the numbers."""
    try:
        return foldl1(lambda b, a: a * b, nums)
    except IndexError:
        raise IndexError("Numbers are empty")


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


def id_(x: a) -> a:
    """Identity function."""
    return x


def const(x: a, _: b) -> a:
    """Evaluates to x for all inputs."""
    return x


def o(f1: Callable[[b], c], f2: Callable[[a], b]) -> Callable[[a], c]:
    """Function composition.

    >>> o(f1, f2)(a) == f1(f2(a))
    """
    return lambda a_: f1(f2(a_))


def flip(f: Callable[[a, b], c]) -> Callable[[b, a], c]:
    """Flip takes its two arguments into the reverse order of f.

    >>> flip(f)(b, a) == f(a, b)
    """
    return lambda b_, a_: f(a_, b_)


def until(p: Predicate, f: Callable[[a], a], x: a) -> a:
    """Yields the result of applying f until p holds."""
    return p(x) and x or until(p, f, f(x))


# ----------------------------------------------------------------------
# Strings
# ----------------------------------------------------------------------


def lines(s: str) -> List[str]:
    """Break up a string into a list of strings at newline characters."""
    return s.splitlines()


def unlines(xs: Sequence[str]) -> str:
    """The inverse operation of lines, append a newline to each."""
    return "\n".join(xs) + "\n"


def words(s: str) -> List[str]:
    """Breaks a string up into a list of words, which were delimited by white
    space."""
    return s.split()


def unwords(xs: Sequence[str]) -> str:
    """The inverse operation of words, join words with space."""
    return " ".join(xs)


# ----------------------------------------------------------------------
# Specials
# ----------------------------------------------------------------------


def not_(f: Callable[..., bool]) -> Callable[..., bool]:
    """Boolean "not"."""

    def _wrap(*args: a, **kwds: b) -> bool:
        """Wrapper of not_."""
        return f(*args, **kwds)

    return _wrap


def all_(p: Predicate, xs: Sequence[a]) -> bool:
    """Determine whether all elements of the structure satisfy the p."""
    return all(map(p, xs))


def any_(p: Predicate, xs: Sequence[a]) -> bool:
    """Determine whether any element of the structure satisfies the p."""
    return any(map(p, xs))


def concat(xss: Sequence[Sequence[a]]) -> G:
    """The concatenation of all the elements of a container of Sequences."""
    for xs in xss:
        for x in xs:
            yield x


def concatmap(
    f: Callable[[Sequence[a]], Sequence[b]], xss: Sequence[Sequence[a]]
) -> Generator[b, None, None]:
    """Map a function over all the elements of a container and concatenate the
    resulting lists."""
    for xs in xss:
        for x in f(xs):
            yield x


# ----------------------------------------------------------------------
# Tuples
# ----------------------------------------------------------------------


def fst(t: Tuple[a, b]) -> a:
    """Extract the first component of a tuple."""
    return t[0]


def snd(t: Tuple[a, b]) -> b:
    """Extract the second component of a tuple."""
    return t[1]


def curry(f: Callable[[Tuple[a, b]], c], a_: a, b_: b) -> c:
    """Converts an uncurried function to a curried function."""
    return f((a_, b_))


def uncurry(f: Callable[[a, b], c], ab: Tuple[a, b]) -> c:
    """Converts a curried function to a function on pairs."""
    a_, b_ = ab
    return f(a_, b_)


# ----------------------------------------------------------------------
# Zip and Unzip
# ----------------------------------------------------------------------


def zipwith(
    f: Callable[[a], c], *seqs: Sequence[a]
) -> Generator[c, None, None]:
    """Zipwith is map(f, zip), but f accept separate args instead of tuple"""
    for zseq in zip(*seqs):
        yield f(*zseq)


def unzip(pairs: Sequence[Tuple[a, ...]]) -> Tuple[Sequence[a], ...]:
    """Transform a sequence of pairs into a tuple of sequence.

    Note: Not lazy."""
    pairs = list(pairs)
    if pairs:
        return tuple(
            [pair[i] for pair in pairs] for i in range(len(head(pairs)))
        )
    return tuple()
