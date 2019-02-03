# Table of Contents

1.  [Prologue](#orga84d1af)
2.  [Nalude](#org575d1ba)
3.  [Structure of Functions](#org98ca3a9)
    1.  [Folds and Traversals](#orgcdf0e4c)
    2.  [Lists](#org40096a0)
    3.  [Miscellaneous](#org0dd692c)
    4.  [String](#org0e42850)
    5.  [Specials](#org6b5065f)
    6.  [Tuples](#org495bc2b)
    7.  [Zip and Unzip](#orgc44f5b8)
4.  [Get Start](#orgf70ecde)
    1.  [Install](#orge328661)
5.  [Epoligue](#orge1161f8)
    1.  [History](#org79a6064)
        1.  [Version 0.1.0](#org81e5864)



<a id="orga84d1af"></a>

# Prologue

I like Haskell, also hope some of basic functions in Haskell can be used in Python.

Wish you enjoy coding.


<a id="org575d1ba"></a>

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


<a id="org98ca3a9"></a>

# Structure of Functions


<a id="orgcdf0e4c"></a>

## Folds and Traversals

-   **foldr(f: Callable[[b, a], b], init: b, t: Sequence[a]) -> b~:** Right-associative fold of a
    sequence.
-   **foldl(f, init, t):** Left-associative fold of a sequence.  The same as `reduce`.
-   **foldr1(f, t):** A variant of foldr without base case.
-   **foldl1(f, t):** A variant of foldl without base case.
-   **product(nums):** Computes the product of the numbers.
-   **(HELP WANTED) traverse:** Map each element of a structure to an action, evaluate these actions from left
    to right, and collect the results.
-   **(HELP WANTED) sequence:** Evaluate each actions in the structure from left to right, and collect the
    results.


<a id="org40096a0"></a>

## Lists

-   **head(xs):** Extract the first element of a sequence.
-   **last(xs):** Extract the last element of a sequence.
-   **null(xs):** Test whether the sequence is empty.
-   Infinite lists
    -   **iterate(f, x):** Yield a tuple of repeated applications of f to x.
    -   **repeat(x):** Repeat x.
    -   **replicate(n, x):** Return a list of length n with x the value of every element.
    -   **cycle(xs):** Tie a sequence to infinite circuler one.

-   Sublists
    -   **tail(xs):** Extract the elements after the head of a list.
    -   **init(xs):** Extract all the elements of a sequence except the last one.
    -   **take(n, xs):** Return the first n elements of sequence xs.
    -   **drop(n, xs):** Return the remaining elements of xs after the first n elements.
    -   **splitat(n, xs):** Return a tuple where the first element is xs prefix of length n and
        second element is the remainder of the sequence xs.
    -   **takewhile(p, xs):** Return the longest prefix of xs of elements that satisfy predicate p.
    -   **dropwhile(p, xs):** Returns the suffix remaining after takewhile(p, xs).
    -   **span(p, xs):** Equal to (takewhile(p, xs), dropwhile(p, xs)).
    -   **break\_(p, xs):** Equal to (takewhile(not\_(p), xs), dropwhile(not\_(p), xs)).


<a id="org0dd692c"></a>

## Miscellaneous

-   **id\_(x):** Identity function.
-   **const(x, \_):** Evaluates to x for all inputs.
-   **o(f1, f2):** (.) Function composition
-   **flip(f):** Flip takes its two arguments into the reverse order of f.
-   **until(p, f, x):** Yield the result of applying f until p holds.


<a id="org0e42850"></a>

## String

-   **lines(s):** Break up a string into a list of strings at newline characters.
-   **unlines(xs):** The inverse operation of lines, append a newline to each.
-   **words(s):** Breaks a string up into a list of words, which were delimited by white space.
-   **unwords(xs):** The inverse operation of words, join words with space.


<a id="org6b5065f"></a>

## Specials

-   **not\_(f):** Boolean "not".
-   **all\_(p, xs):** Determine whether all elements of the structure satisfy the p.
-   **any\_(p, xs):** Determine whether sny elements of the structure satisfies the p.
-   **concat(xss):** The concatenation of all the elements of a container of Sequences.
-   **concatmap(f, xss):** Map a function over all the elements of a container and concatenate the
    resulting lists.


<a id="org495bc2b"></a>

## Tuples

-   **fst(t):** Extract the first component of a tuple.
-   **snd(t):** Extract the second component of a tuple.
-   **curry(f, a, b):** Converts an uncurried function to a curried function.
-   **uncurry(f, ab@(a, b)):** Converts a curried function to a function on pairs.


<a id="orgc44f5b8"></a>

## Zip and Unzip

-   **zipwith(f, \*seqs):** Zipwith is map(f, zip), but f accept separate args instead of tuple
-   **unzip(pairs):** Transform a sequence of pairs into a tuple of sequence. (Not lazy)


<a id="orgf70ecde"></a>

# Get Start


<a id="orge328661"></a>

## Install

    pip install nalude


<a id="orge1161f8"></a>

# Epoligue


<a id="org79a6064"></a>

## History


<a id="org81e5864"></a>

### Version 0.1.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Feb 03, 2019&gt;</span></span>
-   **Commemorate Version:** First Release.
