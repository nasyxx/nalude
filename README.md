# Table of Contents

1.  [Prologue](#org19b18cf)
2.  [Nalude](#orgc77e6a3)
3.  [Structure of Functions](#orge0ad8b3)
    1.  [Folds and Traversals](#org814be7e)
    2.  [Lists](#org5921d0c)
    3.  [Miscellaneous](#orgd0fae96)
    4.  [String](#org9582c2a)
    5.  [Specials](#org5a96f6e)
    6.  [Tuples](#orgadf604e)
    7.  [Zip and Unzip](#org17b382b)
4.  [Get Start](#org5fa3150)
    1.  [Install](#org6298306)
5.  [Epoligue](#orgfe5301e)
    1.  [History](#orgfdeed81)
        1.  [Version 0.1.0](#orgf3aa613)



<a id="org19b18cf"></a>

# Prologue

I like Haskell, also hope some of basic functions in Haskell can be used in Python.

Wish you enjoy coding.


<a id="orgc77e6a3"></a>

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


<a id="orge0ad8b3"></a>

# Structure of Functions


<a id="org814be7e"></a>

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


<a id="org5921d0c"></a>

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
    -   **span(p, xs):** Equal to (takewhile(p, xs), dropwhile(p, xs)).
    -   **break\_(p, xs):** Equal to (takewhile(not\_(p), xs), dropwhile(not\_(p), xs)).


<a id="orgd0fae96"></a>

## Miscellaneous

-   **id\_(x):** Identity function.
-   **const(x, \_):** Evaluates to x for all inputs.
-   **o(f1, f2):** (.) Function composition
-   **flip(f):** Flip takes its two arguments into the reverse order of f.
-   **until(p, f, x):** Yield the result of applying f until p holds.


<a id="org9582c2a"></a>

## String

-   **lines(s):** Break up a string into a list of strings at newline characters.
-   **unlines(xs):** The inverse operation of lines, append a newline to each.
-   **words(s):** Breaks a string up into a list of words, which were delimited by white space.
-   **unwords(xs):** The inverse operation of words, join words with space.


<a id="org5a96f6e"></a>

## Specials

-   **not\_(f):** Boolean "not".
-   **all\_(p, xs):** Determine whether all elements of the structure satisfy the p.
-   **any\_(p, xs):** Determine whether sny elements of the structure satisfies the p.
-   **concat(xss):** The concatenation of all the elements of a container of Sequences.
-   **concatmap(f, xss):** Map a function over all the elements of a container and concatenate the
    resulting lists.


<a id="orgadf604e"></a>

## Tuples

-   **fst(t):** Extract the first component of a tuple.
-   **snd(t):** Extract the second component of a tuple.
-   **curry(f, a, b):** Converts an uncurried function to a curried function.
-   **uncurry(f, ab@(a, b)):** Converts a curried function to a function on pairs.


<a id="org17b382b"></a>

## Zip and Unzip

-   **zipwith(f, \*seqs):** Zipwith is map(f, zip), but f accept separate args instead of tuple
-   **unzip(pairs):** Transform an iterable of pairs into a tuple of sequence. (Not lazy)


<a id="org5fa3150"></a>

# Get Start


<a id="org6298306"></a>

## Install

    pip install nalude


<a id="orgfe5301e"></a>

# Epoligue


<a id="orgfdeed81"></a>

## History


<a id="orgf3aa613"></a>

### Version 0.1.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Feb 03, 2019&gt;</span></span>
-   **Commemorate Version:** First Release.
