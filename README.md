# Table of Contents

1.  [Prologue](#orgaa77cb0)
2.  [Nalude](#orgbf83b5c)
3.  [Structure of Functions](#org839c943)
    1.  [[-] Folds and Traversals <code>[5/7]</code>](#orgbff7da8)
    2.  [[X] Lists <code>[5/5]</code>](#org9ce12cc)
    3.  [[-] Miscellaneous <code>[2/6]</code>](#orgfa08ed4)
    4.  [[ ] String <code>[0/4]</code>](#org23adb09)
    5.  [[-] Specials <code>[1/5]</code>](#orgd0650e4)
    6.  [[ ] Tuples <code>[0/4]</code>](#orgec6e528)
    7.  [[ ] Zip and Unzip <code>[0/3]</code>](#org2e08d27)
4.  [Get Start](#org05ee837)
    1.  [Install](#orgbe63c29)
    2.  [Usage](#orgd2f3ae4)
5.  [Epoligue](#org589d9a8)



<a id="orgaa77cb0"></a>

# Prologue

I like Haskell, also hope some of basic functions in Haskell can be used in Python.

Wish you enjoy coding.


<a id="orgbf83b5c"></a>

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


<a id="org839c943"></a>

# Structure of Functions


<a id="orgbff7da8"></a>

## [-] Folds and Traversals <code>[5/7]</code>

-   [X] **foldr:** Right-associative fold of a sequence.
-   [X] **foldl:** Left-associative fold of a sequence.  The same as `reduce`
-   [X] **foldr1:** A variant of foldr without base case.
-   [X] **foldl1:** A variant of foldl without base case.
-   [X] **product:** Computes the product of the numbers.
-   [ ] **traverse:** Map each element of a structure to an action, evaluate these actions from left
    to right, and collect the results.
-   [ ] **sequence:** Evaluate each actions in the structure from left to right, and collect the
    results.


<a id="org9ce12cc"></a>

## [X] Lists <code>[5/5]</code>

-   [X] **head:** Extract the first element of a sequence.
-   [X] **last:** Extract the last element of a sequence.
-   [X] **null:** Test whether the sequence is empty.
-   [X] Infinite lists <code>[4/4]</code>
    -   [X] **iterate:** Yield a tuple of repeated applications of f to x.
    -   [X] **repeat:** Repeat x.
    -   [X] **replicate:** Return a list of length n with x the value of every element.
    -   [X] **cycle:** Tie a sequence to infinite circuler one.

-   [X] Sublists <code>[9/9]</code>
    -   [X] **tail:** Extract the elements after the head of a list.
    -   [X] **init:** Extract all the elements of a sequence except the last one.
    -   [X] **take:** Return the first n elements of sequence xs.
    -   [X] **drop:** Return the remaining elements of xs after the first n elements.
    -   [X] **splitat:** Return a tuple where the first element is xs prefix of length n and second
        element is the remainder of the sequence xs.
    -   [X] **takewhile:** Return the longest prefix of xs of elements that satisfy predicate p.
    -   [X] **dropwhile:** Returns the suffix remaining after takewhile(p, xs).
    -   [X] **span:** Equal to (takewhile(p, xs), dropwhile(p, xs)).
    -   [X] **break\_:** Equal to (takewhile(not\_(p), xs), dropwhile(not\_(p), xs)).


<a id="orgfa08ed4"></a>

## [-] Miscellaneous <code>[2/6]</code>

-   [ ] **id\_:**

-   [ ] **const:**

-   [X] **o:** (.) Function composition
-   [X] **flip:** Flip takes its two arguments into the reverse order of f.
-   [ ] **until:**

-   [ ] **seq:**


<a id="org23adb09"></a>

## [ ] String <code>[0/4]</code>

-   [ ] **lines:**

-   [ ] **unlines:**

-   [ ] **words:**

-   [ ] **unwords:**


<a id="orgd0650e4"></a>

## [-] Specials <code>[1/5]</code>

-   [X] **not\_:** Boolean "not".
-   [ ] **all\_:**

-   [ ] **any\_:**

-   [ ] **concat:**

-   [ ] **concatmap:**


<a id="orgec6e528"></a>

## [ ] Tuples <code>[0/4]</code>

-   [ ] **fst:** Extract the first component of a tuple.
-   [ ] **snd:** Extract the second component of a tuple.
-   [ ] **curry:** Converts an uncurried function to a curried function.
-   [ ] **uncurry:** Converts a curried function to a function on pairs.


<a id="org2e08d27"></a>

## [ ] Zip and Unzip <code>[0/3]</code>

-   [ ] **zipwith:**

-   [ ] **unzip:**

-   [ ] **unzipwith:**


<a id="org05ee837"></a>

# Get Start


<a id="orgbe63c29"></a>

## Install


<a id="orgd2f3ae4"></a>

## Usage


<a id="org589d9a8"></a>

# Epoligue
