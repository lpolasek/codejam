Problem D Analysis
------------------

### The Solution
This problem is very mathematical in nature, requiring a lot of thought and only a little code to solve correctly. We put it as a problem on the Qualifying Round to give you something different to try without having to worry about time pressure or advancement. We hope you enjoyed it!

For an arbitrary array A, let n(A) be the number of elements that are not already in the correct position. It turns out that the answer you are looking for is simply n(A). Once you realize this, it is easy to calculate with a simple loop, but how do you prove it?


The Proof
Let's first show that the expected number of hits is never more than n(A). Suppose Goro always holds down only those elements that are already in position, and then he randomly permutes the rest. Let x(A) be the expected number of hits required for him to sort A using this strategy.

Lemma: x(A) = n(A) for all A.

We prove this by induction on n(A). If n(A) = 0, then the array is already sorted, and we're done. To set up the induction, let's suppose we have proven the lemma already for smaller values of n(A) and we are now trying to prove it for A. Let pt be the probability that exactly t elements are still out of position after the first hit, and let x't be the expected number of hits required in this case. We make three observations:

p0 * 0 + p1 * 1 + p2 * 2 + ... + pN * N = N - 1. In English, this is saying that the expected number of elements that are out of position after the first hit is exactly N - 1, or equivalently, the expected number of elements that are put into position by the first hit is exactly 1. This follows from "linearity of expectation": Goro is permuting N elements; each one has probability exactly 1/N of ending up in the correct position, and hence, the expected number of elements that end up in the correct position is N * 1/N = 1.
x't = t for t ≤ N - 1. This is true by the inductive hypothesis.
x'N = x(A). If no elements are put into the correct position by the first hit, then we will just randomly permute them all again in the next step, so nothing has changed, and hence x'N = x(A).
Now let's write down a formula for x(A):
1 + p0 * x'0 + p1 * x'1 + ... + pN * x'N
= 1 + p0 * 0 + p1 * 1 + ... + pN * N + pN * (x(A) - N)
= N + pN * (x(A) - N),

which simplifies to (N - x(A)) * (1 - pN) = 0. Since pN < 1, we must have x(A) = N, and the lemma is proven.


To complete the proof, we need to calculate y(A), the expected number of hits required for Goro to sort A if he uses the (still unknown) optimal strategy. Since y(A) ≤ x(A) by definition, we have already proven y(A) ≤ n(A).

To conversely prove n(A) ≤ y(A), it would be nice to just extend the proof of the previous lemma. There is one big technical issue though: it is possible for n(A) to go up if Goro doesn't hold down enough elements, and so it is tricky to set up an induction on n(A). We'll resolve this by having a separate proof for this part, and this time use a slightly different induction hypothesis. We can then follow the previous argument very closely.

Lemma 2: Let K be a non-negative integer. Then for any k ≤ K, the statement y(A) = k is equivalent to the statement n(A) = k.

We will prove this by induction on K. Both y(A) = 0 and n(A) = 0 are equivalent to the array already being sorted, so the K = 0 case is clear. Now, let's suppose we have proven the lemma for K already, and are trying to prove it for K+1. Choose A such that y(A) is the smallest possible value larger than K and consider the optimal strategy for Goro. Let T be the number of elements that are either (a) not in the correct position in A, or (b) permuted when Goro hits the table. Define pi and x'i as we did before. Note that T ≥ n(A) ≥ K+1 by the inductive hypothesis.

As in the previous lemma, we can now prove the following:

p0 * 0 + p1 * 1 + p2 * 2 + ... pT * T ≥ T - 1.
x'i = i for i ≤ K. This follows directly from the inductive hypothesis.
x'i ≥ y(A) for i > K. By the inductive hypothesis, n(A') > K implies y(A') > K, which then implies y(A') ≥ y(A).
As before, we can now write y(A) as

1 + p0 * x'0 + p1 * x'1 + ... pT * x'T
≥ 1 + (p0 * 0 + p1 * 1 + ... + pT * T) + (pK+1 + pK+2 + ... + pT) * (y(A) - T)
≥ T + (pK+1 + pK+2 + ... + pT) * (y(A) - T)

which simplifies to (y(A) - T) * (1 - pK+1 - ... - pT) ≥ 0. The second term has to be positive (if not, then y(A) ≥ min(x'K+1, x'K+2, ...) + 1, which contradicts the third bullet point above is therefore impossible), so we must have y(A) ≥ T ≥ n(A) ≥ K+1. Equality holds only if n(A) = K+1. The first lemma guarantees y(A) ≤ x(A) ≤ K+1 in this case, and the proof is complete!


Comments
If you go over the proof carefully, you can see there are two things Goro needs to do in order to be optimal. (1) He needs to always hold down elements that are already in the correct position, and (2) he needs to ensure that for each element x that is permuted, the element in x's correct position is also permuted. This means he actually has some choice about what to do.
On a programming contest, of course you do not need to work through a formal proof to implement a correct solution. The best contestants can solve this kind of problem by looking at small examples to see a pattern, and then using intuitive reasoning to see what's going on without formalizing everything. Mastering this kind of reasoning is a difficult art though!

