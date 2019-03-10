# Table of Contents

1.  [Prologue](#org8b6bf34)
2.  [Nalude](#org0812938)
3.  [Structure of Functions](#org658c0e2)
    1.  [Folds and Traversals](#orgebe257d)
    2.  [Lists](#org8fd809b)
    3.  [Miscellaneous](#orgd3b3bf1)
    4.  [String](#org8147070)
    5.  [Specials](#org2de95e8)
    6.  [Tuples](#orge6105ca)
    7.  [Zip and Unzip](#orgcdca5f7)
    8.  [Extra](#org5b1da39)
4.  [Get Start](#orgccf98f8)
    1.  [Install](#org1d1b386)
5.  [Epoligue](#orgd300cef)
    1.  [History](#org1d83dae)
        1.  [Version 0.3.0](#orga174a69)
        2.  [Version 0.2.0](#orga9ce38e)
        3.  [Version 0.1.0](#orgad971e1)



<a id="org8b6bf34"></a>

# Prologue

I like Haskell, also hope some of the prelude functions in Haskell can be used in Python.

Wish you enjoy coding with nalude.


<a id="org0812938"></a>

# Nalude

Nalude is a standard module, which is inspired by Haskell's Prelude.  Thus, nalude is also a
library of functional programming.

Nalude doesn't explicitly distinguish between Applicative's or monadic function since they are not
well differentiated in the basic structure of Python.  Of course, the main reason is that I am too
fresh.

The following functions, Nalude tries to implement:

1.  Folds and Traversals
2.  Lists
3.  Miscellaneous
4.  Specials
5.  Strings
6.  Tuples
7.  Zip and Unzip

At the same time, it also implements some functions which are only available in Python and are
included in \`extra\`.


<a id="org658c0e2"></a>

# Structure of Functions


<a id="orgebe257d"></a>

## Folds and Traversals

-   **foldr(f: Callable[[b, a], b], init: b, t: Sequence[a]):** Right-associative fold of a sequence.
-   **foldl(f, init, t):** Left-associative fold of an iterable.  The same as `reduce`.
-   **foldr1(f, t):** A variant of foldr without base case.
-   **foldl1(f, t):** A variant of foldl without base case.
-   **product(nums):** Computes the product of the numbers.
-   **(HELP WANTED) traverse:** Map each element of a structure to an action, evaluate these actions
    from left to right, and collect the results.
-   **(HELP WANTED) sequence:** Evaluate each actions in the structure from left to right, and collect
    the results.


<a id="org8fd809b"></a>

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
        -   **dropwhile(p, xs):** Return the suffix remaining after takewhile(p, xs).
        -   **(LAZY ONE HELP WANTED) span(p, xs):** Equal to (takewhile(p, xs), dropwhile(p, xs)).
        -   **(LAZY ONE HELP WANTED) break\_(p, xs):** Equal to (takewhile(not\_(p), xs),
            dropwhile(not\_(p), xs)).


<a id="orgd3b3bf1"></a>

## Miscellaneous

-   **id\_(x):** Identity function.
-   **const(x, \_):** Evaluates to x for all inputs.
-   **o(f1, f2):** (.) Function composition
-   **flip(f):** Flip takes its two arguments into the reverse order of f.
-   **until(p, f, x):** Yield the result of applying f until p holds.


<a id="org8147070"></a>

## String

-   **lines(s):** Break up a string into a list of strings at newline characters.
-   **unlines(xs):** The inverse operation of lines, append a newline to each.
-   **words(s):** Break a string up into a list of words, which were delimited by white space.
-   **unwords(xs):** The inverse operation of words, join words with space.


<a id="org2de95e8"></a>

## Specials

-   **not\_(f):** Boolean "not".
-   **all\_(p, xs):** Determine whether all elements of the structure satisfy the p.
-   **any\_(p, xs):** Determine whether sny elements of the structure satisfies the p.
-   **concat(xss):** The concatenation of all the elements of a container of Sequences.
-   **concatmap(f, xss):** Map a function over all the elements of a container and concatenate the
    resulting lists.


<a id="orge6105ca"></a>

## Tuples

-   **fst(t):** Extract the first component of a tuple.
-   **snd(t):** Extract the second component of a tuple.
-   **curry(f, a, b):** Converts an uncurried function to a curried function.
-   **uncurry(f, ab@(a, b)):** Converts a curried function to a function on pairs.


<a id="orgcdca5f7"></a>

## Zip and Unzip

-   **zipwith(f, \*seqs):** Zipwith is map(f, zip), but f accept separate args instead of tuple
-   **unzip(pairs):** Transform an iterable of pairs into a tuple of sequence. (Not lazy)


<a id="org5b1da39"></a>

## Extra

-   **flatten(xs,\*,ignore=(dict,)):** Flatten iterables of iterable to a single iterable.  It will
    ignore instances in `ignore` tuple.


<a id="orgccf98f8"></a>

# Get Start


<a id="org1d1b386"></a>

## Install

    pip install nalude


<a id="orgd300cef"></a>

# Epoligue


<a id="org1d83dae"></a>

## History


<a id="orga174a69"></a>

### Version 0.3.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Add:** -   Custom ignore when flatten iterable.


<a id="orga9ce38e"></a>

### Version 0.2.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Fri Feb 15, 2019&gt;</span></span>
-   **Add:** -   flatten in extra.


<a id="orgad971e1"></a>

### Version 0.1.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Feb 06, 2019&gt;</span></span>
-   **Commemorate Version:** First Release.
