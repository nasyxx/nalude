# Table of Contents

1.  [Prologue](#org9309e20)
2.  [Nalude](#orgd146690)
3.  [Structure of Functions](#org239a9a3)
    1.  [Folds and Traversals](#org4359e86)
    2.  [Lists](#org657598d)
    3.  [Miscellaneous](#org31efb9c)
    4.  [String](#org20152d2)
    5.  [Specials](#orge3785b4)
    6.  [Tuples](#org26d2935)
    7.  [Zip and Unzip](#org139332a)
    8.  [Extra](#orgd58c472)
4.  [Get Start](#org5740bab)
    1.  [Install](#orge5fc1bc)
5.  [Epoligue](#orgc60fefa)
    1.  [History](#org19b33c7)
        1.  [Version 0.2.0](#org2786df5)
        2.  [Version 0.1.0](#orgd86b472)



<a id="org9309e20"></a>

# Prologue

I like Haskell, also hope some of the prelude functions in Haskell can be used in Python.

Wish you enjoy coding with nalude.


<a id="orgd146690"></a>

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


<a id="org239a9a3"></a>

# Structure of Functions


<a id="org4359e86"></a>

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


<a id="org657598d"></a>

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


<a id="org31efb9c"></a>

## Miscellaneous

-   **id\_(x):** Identity function.
-   **const(x, \_):** Evaluates to x for all inputs.
-   **o(f1, f2):** (.) Function composition
-   **flip(f):** Flip takes its two arguments into the reverse order of f.
-   **until(p, f, x):** Yield the result of applying f until p holds.


<a id="org20152d2"></a>

## String

-   **lines(s):** Break up a string into a list of strings at newline characters.
-   **unlines(xs):** The inverse operation of lines, append a newline to each.
-   **words(s):** Break a string up into a list of words, which were delimited by white space.
-   **unwords(xs):** The inverse operation of words, join words with space.


<a id="orge3785b4"></a>

## Specials

-   **not\_(f):** Boolean "not".
-   **all\_(p, xs):** Determine whether all elements of the structure satisfy the p.
-   **any\_(p, xs):** Determine whether sny elements of the structure satisfies the p.
-   **concat(xss):** The concatenation of all the elements of a container of Sequences.
-   **concatmap(f, xss):** Map a function over all the elements of a container and concatenate the
    resulting lists.


<a id="org26d2935"></a>

## Tuples

-   **fst(t):** Extract the first component of a tuple.
-   **snd(t):** Extract the second component of a tuple.
-   **curry(f, a, b):** Converts an uncurried function to a curried function.
-   **uncurry(f, ab@(a, b)):** Converts a curried function to a function on pairs.


<a id="org139332a"></a>

## Zip and Unzip

-   **zipwith(f, \*seqs):** Zipwith is map(f, zip), but f accept separate args instead of tuple
-   **unzip(pairs):** Transform an iterable of pairs into a tuple of sequence. (Not lazy)


<a id="orgd58c472"></a>

## Extra

-   **flatten(xs):** Flatten iterables of iterable to a single iterable.


<a id="org5740bab"></a>

# Get Start


<a id="orge5fc1bc"></a>

## Install

    pip install nalude


<a id="orgc60fefa"></a>

# Epoligue


<a id="org19b33c7"></a>

## History


<a id="org2786df5"></a>

### Version 0.2.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Fri Feb 15, 2019&gt;</span></span>
-   **Add:** -   flatten in extra.


<a id="orgd86b472"></a>

### Version 0.1.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Feb 06, 2019&gt;</span></span>
-   **Commemorate Version:** First Release.
