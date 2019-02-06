# Table of Contents

1.  [Prologue](#orgf3d623c)
2.  [Nalude](#org860f92d)
3.  [Structure of Functions](#orge217ccf)
    1.  [Folds and Traversals](#orgd4b0575)
    2.  [Lists](#org9bfd24f)
    3.  [Miscellaneous](#org9c502c4)
    4.  [String](#orga5b8e5c)
    5.  [Specials](#orga37547b)
    6.  [Tuples](#orgafb497a)
    7.  [Zip and Unzip](#org68a3559)
4.  [Get Start](#org9ecdb64)
    1.  [Install](#orge3e4d68)
5.  [Epoligue](#orgefb4c33)
    1.  [History](#orgadc1be2)
        1.  [Version 0.1.0](#org3c811ad)



<a id="orgf3d623c"></a>

# Prologue

I like Haskell, also hope some of basic functions in Haskell can be used in Python.

Wish you enjoy coding.


<a id="org860f92d"></a>

# Nalude

Nalude is a standard module, which is inspired by Haskell's Prelude.  Thus, nalude is also a
library of functional programming.

Nalude doesn't specifically distinguish between Applicative's or monadic function, since they are
not well differentiated in the basic structure of Python.

The following functions, Nalude tries to implement:

1.  Folds and Traversals
2.  Lists
3.  Miscellaneous
4.  Specials
5.  Strings
6.  Tuples
7.  Zip and Unzip


<a id="orge217ccf"></a>

# Structure of Functions


<a id="orgd4b0575"></a>

## Folds and Traversals

-   **foldr(f: Callable[[b, a], b], init: b, t: Sequence[a]):** Right-associative fold of a
    sequence.
-   **foldl(f, init, t):** Left-associative fold of an iterable.  The same as `reduce`.
-   **foldr1(f, t):** A variant of foldr without base case.
-   **foldl1(f, t):** A variant of foldl without base case.
-   **product(nums):** Computes the product of the numbers.
-   **(HELP WANTED) traverse:** Map each element of a structure to an action, evaluate these actions from left
    to right, and collect the results.
-   **(HELP WANTED) sequence:** Evaluate each actions in the structure from left to right, and collect the
    results.


<a id="org9bfd24f"></a>

## Lists

-   **head(xs):** Extract the first element of an iterable.
-   **last(xs):** Extract the last element of an iterable.
-   **null(xs):** Test whether the sequence is empty.
-   Infinite lists
    -   **iterate(f, x):** Yield a tuple of repeated applications of f to x.
    -   **repeat(x):** Repeat x.
    -   **replicate(n, x):** Return a list of length n with x the value of every element.
    -   **cycle(xs):** Tie an iterable to infinite circuler one.

-   Sublists
    -   **tail(xs):** Extract the elements after the head of a list.
    -   **init(xs):** Extract all the elements of an iterable except the last one.
    -   **take(n, xs):** Return the first n elements of sequence xs.
    -   **drop(n, xs):** Return the remaining elements of xs after the first n elements.
    -   **splitat(n, xs):** Return a tuple where the first element is xs prefix of length n and
        second element is the remainder of the sequence xs.
    -   **takewhile(p, xs):** Return the longest prefix of xs of elements that satisfy predicate p.
    -   **dropwhile(p, xs):** Returns the suffix remaining after takewhile(p, xs).
    -   **(LAZY ONE HELP WANTED) span(p, xs):** Equal to (takewhile(p, xs), dropwhile(p, xs)).
    -   **(LAZY ONE HELP WANTED) break\_(p, xs):** Equal to (takewhile(not\_(p), xs),
        dropwhile(not\_(p), xs)).


<a id="org9c502c4"></a>

## Miscellaneous

-   **id\_(x):** Identity function.
-   **const(x, \_):** Evaluates to x for all inputs.
-   **o(f1, f2):** (.) Function composition
-   **flip(f):** Flip takes its two arguments into the reverse order of f.
-   **until(p, f, x):** Yield the result of applying f until p holds.


<a id="orga5b8e5c"></a>

## String

-   **lines(s):** Break up a string into a list of strings at newline characters.
-   **unlines(xs):** The inverse operation of lines, append a newline to each.
-   **words(s):** Breaks a string up into a list of words, which were delimited by white space.
-   **unwords(xs):** The inverse operation of words, join words with space.


<a id="orga37547b"></a>

## Specials

-   **not\_(f):** Boolean "not".
-   **all\_(p, xs):** Determine whether all elements of the structure satisfy the p.
-   **any\_(p, xs):** Determine whether sny elements of the structure satisfies the p.
-   **concat(xss):** The concatenation of all the elements of a container of Sequences.
-   **concatmap(f, xss):** Map a function over all the elements of a container and concatenate the
    resulting lists.


<a id="orgafb497a"></a>

## Tuples

-   **fst(t):** Extract the first component of a tuple.
-   **snd(t):** Extract the second component of a tuple.
-   **curry(f, a, b):** Converts an uncurried function to a curried function.
-   **uncurry(f, ab@(a, b)):** Converts a curried function to a function on pairs.


<a id="org68a3559"></a>

## Zip and Unzip

-   **zipwith(f, \*seqs):** Zipwith is map(f, zip), but f accept separate args instead of tuple
-   **unzip(pairs):** Transform an iterable of pairs into a tuple of sequence. (Not lazy)


<a id="org9ecdb64"></a>

# Get Start


<a id="orge3e4d68"></a>

## Install

    pip install nalude


<a id="orgefb4c33"></a>

# Epoligue


<a id="orgadc1be2"></a>

## History


<a id="org3c811ad"></a>

### Version 0.1.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Feb 06, 2019&gt;</span></span>
-   **Commemorate Version:** First Release.
