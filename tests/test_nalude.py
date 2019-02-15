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
from typing import Tuple

# Other Packages
from nalude import (o, fst, id_, snd, all_, any_, drop, flip, head, init,
                    last, not_, null, span, tail, take, const, curry, cycle,
                    foldl, foldr, lines, until, unzip, words, break_, concat,
                    foldl1, foldr1, repeat, flatten, iterate, product,
                    splitat, uncurry, unlines, unwords, zipwith, concatmap,
                    dropwhile, replicate, takewhile, __version__,)


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

    def test_folds_folds(self) -> None:
        """Test folds and traversals."""
        self.assertEqual(
            foldl(lambda x, y: x + y, 0, range(10)),
            foldr(lambda x, y: x + y, 0, range(10)),
        )
        self.assertEqual(
            foldl1(lambda x, y: x + y, range(10)),
            foldr1(lambda x, y: x + y, range(10)),
        )
        self.assertEqual(
            foldl1(lambda x, y: x + y, range(10)),
            foldr(lambda x, y: x + y, 0, range(10)),
        )

    def test_folds_product(self) -> None:
        """Test folds product."""
        self.assertEqual(product([1, 2, 3, 4, 5]), 5 * 4 * 3 * 2 * 1)
        self.assertEqual(product(range(10)), 0)

    def test_lists_head_last(self) -> None:
        """Test lists head and last."""
        self.assertEqual(head(range(1)), last(range(1)))
        self.assertEqual(head("yoooo!"), last("!ooooy"))
        self.assertRaises(IndexError, head, list())
        self.assertRaises(IndexError, last, list())

    def test_lists_tail_init(self) -> None:
        """Test lists tail and init."""
        self.assertEqual(list(tail(range(5))), list(init([1, 2, 3, 4, 0])))
        self.assertEqual(list(tail(range(1))), list(init(range(1))))
        self.assertRaises(IndexError, lambda x: next(tail(x)), list())
        self.assertRaises(IndexError, lambda x: next(init(x)), list())

    def test_lists_null(self) -> None:
        """Test lists null."""
        self.assertTrue(null(range(0)))
        self.assertFalse(null(range(1)))

    def test_lists_iterate(self) -> None:
        """Test lists iterate."""
        for i, e in zip(range(1, 6), iterate(lambda x: x + 1, 1)):
            with self.subTest(i=i, e=e):
                self.assertEqual(e, i)

        for i, e in zip(range(1, 6), iterate(lambda x: [1] + x, [1])):
            with self.subTest(i=i, e=e):
                self.assertEqual(e, [1] * i)

    def test_lists_repeat_replicate(self) -> None:
        """Test lists repeat and replicate."""
        for r1, r2 in zip(replicate(10, 5), repeat(5)):
            with self.subTest(r1=r1, r2=r2):
                self.assertEqual(r1, r2)

    def test_lists_cycle(self) -> None:
        """Test lists cycle."""
        for c1, c2 in zip([1, 2, 3] * 3, cycle([1, 2, 3])):
            with self.subTest(str(c1), c1=c1, c2=c2):
                self.assertEqual(c1, c2)
        self.assertRaises(IndexError, lambda x: next(cycle(x)), list())

    def test_lists_take_drop_splitat(self) -> None:
        """Test lists take, drop and splitat."""
        self.assertEqual(list(take(5, [])), list(drop(5, [])))
        self.assertEqual(list(take(-1, [1, 2, 3])), [])
        self.assertEqual(list(take(1, [1, 2, 3])), [1])
        self.assertEqual(list(drop(-1, [1, 2, 3])), [1, 2, 3])
        self.assertEqual(list(drop(1, [1, 2, 3])), [2, 3])

        self.assertEqual(
            list(take(5, range(5))), list(splitat(5, range(5))[0])
        )
        self.assertEqual(
            list(drop(5, range(5))), list(splitat(5, range(5))[1])
        )
        xs = range(10)
        self.assertEqual(
            (list(take(5, (i for i in xs))), list(drop(5, (i for i in xs)))),
            tuple(map(list, splitat(5, (i for i in xs)))),
        )

    def test_lists_takewhile_dropwhile_span_break(self) -> None:
        """Test lists takewhile and dropwhile, span and break."""
        self.assertEqual(
            list(takewhile(lambda x: x < 3, range(10))), [0, 1, 2]
        )
        self.assertEqual(list(dropwhile(lambda x: x < 8, range(10))), [8, 9])
        self.assertEqual(
            span(lambda x: x < 3, [1, 2, 3, 4, 1, 2, 3, 4]),
            break_(lambda x: x > 2, [1, 2, 3, 4, 1, 2, 3, 4]),
        )
        self.assertEqual(
            span(lambda x: x < 9, [1, 2, 3]),
            break_(lambda x: x > 9, [1, 2, 3]),
        )
        self.assertEqual(
            span(lambda x: x > 9, [1, 2, 3]),
            break_(lambda x: x < 9, [1, 2, 3]),
        )

    def test_miscellaneous_id_const(self) -> None:
        """Test miscellaneous id and const."""
        self.assertEqual(id_(0), 0)
        self.assertEqual(const(0, 1), 0)

    def test_miscellaneous_o_flip(self) -> None:
        """Test miscellaneous o and flip."""

        def f1(x: int) -> int:
            """Function f1."""
            return x * 2

        def f2(x: int) -> int:
            """Function f2."""
            return x + 2

        def f(x: int, y: int) -> str:
            """Function f."""
            return str(x) + str(y)

        self.assertEqual(o(f1, f2)(1), f1(f2(1)))
        self.assertEqual(o(f1, o(f2, f1))(1), f1(f2(f1(1))))
        self.assertEqual(flip(f)(1, 2), f(2, 1))

    def test_miscellaneous_until(self) -> None:
        """Test miscellaneous until."""
        self.assertEqual(until(lambda x: x > 10, lambda x: x * 2, 1), 16)

    def test_strings_lines_unlines(self) -> None:
        """Test strings lines and unlines."""
        self.assertEqual(lines(""), [])
        self.assertEqual(lines("\n"), [""])
        self.assertEqual(lines("one\n"), ["one"])
        self.assertEqual(lines("one\n\n"), ["one", ""])
        self.assertEqual(lines("one\ntwo"), ["one", "two"])
        self.assertEqual(lines("one\ntwo\n"), ["one", "two"])
        self.assertEqual(unlines(lines("one\ntwo")), "one\ntwo\n")

    def test_strings_words_unwords(self) -> None:
        """Test strings words and unwords."""
        self.assertEqual(
            words("Lorem ipsum\ndolor"), ["Lorem", "ipsum", "dolor"]
        )
        self.assertEqual(
            unwords(["Lorem", "ipsum", "dolor"]), "Lorem ipsum dolor"
        )

    def test_specials_not(self) -> None:
        """Test specials not."""
        self.assertTrue(not_(bool)(False))
        self.assertTrue(not_(bool)([]))
        self.assertFalse(not_(bool)(True))

    def test_specials_any_all(self) -> None:
        """Test specials any and all."""
        self.assertTrue(any_(lambda x: x >= 5, range(6)))
        self.assertFalse(all_(lambda x: x < 5, range(6)))

    def test_special_concat_map(self) -> None:
        """Test specials concat and concatmap."""
        self.assertEqual(
            list(concat([[1, 2, 3], [2, 3, 4]])), [1, 2, 3, 2, 3, 4]
        )
        self.assertEqual(
            list(concat(((i for i in ii) for ii in [[1, 2, 3], [2, 3, 4]]))),
            [1, 2, 3, 2, 3, 4],
        )
        self.assertEqual(
            list(
                concatmap(
                    lambda x: [1] + list(x), [[1, 2, 3, 4], [2, 3, 4, 5]]
                )
            ),
            [1, 1, 2, 3, 4, 1, 2, 3, 4, 5],
        )

    def test_tuple_fst_snd(self) -> None:
        """Test tuple fst and snd."""
        t = (1, 2)
        self.assertEqual((fst(t), snd(t)), t)

    def test_tuple_curry_uncurry(self) -> None:
        """Test tuple curry and uncurry."""

        def f(ab: Tuple[int, str]) -> Tuple[str, int]:
            """Function f."""
            return str(ab[0]), int(ab[1])

        def f_(a: str, b: int) -> Tuple[int, str]:
            """Function f."""
            return int(a), str(b)

        self.assertEqual(curry(f, 1, "2"), ("1", 2))
        self.assertEqual(uncurry(f_, ("1", 2)), (1, "2"))

    def test_zip_and_unzip(self) -> None:
        """Test zipwith and unzip."""

        def fzw(a: int, b: int) -> int:
            """Function zipwith."""
            return a + b

        self.assertEqual(
            list(zipwith(fzw, range(10), range(2, 12))),
            list(map(lambda xy: xy[0] + xy[1], zip(range(10), range(2, 12)))),
        )
        self.assertEqual(
            unzip([(1, 2), (2, 3), (3, 4)]), ([1, 2, 3], [2, 3, 4])
        )

    def test_extra_flatten(self) -> None:
        """Test extra flatten."""
        self.assertEqual(
            list(
                flatten(
                    [
                        1,
                        2,
                        3,
                        4,
                        "123",
                        [
                            1,
                            2,
                            3,
                            [
                                dict(a=12),
                                ["12", "12", (1, 2, 3), (i for i in range(3))],
                            ],
                        ],
                    ]
                )
            ),
            [
                1,
                2,
                3,
                4,
                "123",
                1,
                2,
                3,
                dict(a=12),
                "12",
                "12",
                1,
                2,
                3,
                0,
                1,
                2,
            ],
        )


def run() -> None:
    """Run test."""
    unittest.main()


if __name__ == "__main__":
    run()
