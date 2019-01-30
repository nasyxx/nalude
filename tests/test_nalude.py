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
filename : test_nalude.py
project  : nalude
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
import unittest

from nalude import __version__


class NaludeTest(unittest.TestCase):
    """Nasy prelude package test."""

    def test_version(self) -> None:
        """Test version of nalude."""
        with open("pyproject.toml") as f:
            for line in f:
                if "version" in line:
                    version = line.split()[-1].replace('"', "")
                    break
        self.assertEqual(__version__, version)


def run() -> None:
    """Run test."""
    unittest.main()


if __name__ == "__main__":
    run()
