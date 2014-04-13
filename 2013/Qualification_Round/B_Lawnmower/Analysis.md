Problem B Analysis
------------------

### The Small Input

For a problem like this, it can be helpful to think through a few cases. Let's look at the first two examples from the problem statement:

    2 2 2 2 2
    2 1 1 1 2    2 1 2
    2 1 2 1 2    1 1 1
    2 1 1 1 2    2 1 2
    2 2 2 2 2

All the grass needs to be cut to either height 1 or 2. Thus, we can begin by cutting the whole lawn to height 2. The question that remains is which rows and which columns to cut to height 1. Note that if we cut a row (or column) to height 1, all the squares in this row or column will be height 1 in the final pattern since we can't grow grass back.

In the left example, we must at some point do a cut with the lawnmower at height 1. Otherwise, we would never get any grass that low. However, there is nowhere that it is safe to make a cut like that. Every row and every column has at least one square where we want the final grass height to be 2, so we can never run the lawnmower through that row or column while at height 1. This pattern is impossible.

In the second example, we also must do some cuts with the lawnmower at height 1. However, in this case, there are two places where we can safely make that cut: the middle row and the middle column. If we do both, we get the desired pattern.

More generally, there are some rows and columns we cannot cut to height 1. By avoiding those rows and columns, we ensure nothing will be made too low. What remains is to check if it is still possible to get all the grass low  _enough_. Well, if our only goal is to get the grass low, we should do all the cuts we can!

This suggests the following approach:

-   Determine which rows and columns it is safe to cut at height 1 (meaning the pattern has no square with height > 1 in that row or column).
-   Do a cut on each of these rows and columns at height 1.
-   Check if we got every square low enough. If so, the pattern is possible. Otherwise, it is not.

### The Large Input

For the large input, we can use almost the exact same strategy. You just have to think through what that means!

We can cut any row or column at a height that is equal to the maximum height appearing in this row (or column). As long as we follow this rule, we will never cut a square too low, and then as above, we just need to try to get everything low enough. For that purpose, we want to use all the cuts we can. The full algorithm is then:

-   Iterate over every row and find the largest height that the pattern has in this row. Cut the row at this height.
-   Do the same thing for every column.
-   Output "YES" if this achieved the desired pattern, and "NO" if not.

