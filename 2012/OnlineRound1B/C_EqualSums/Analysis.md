Problem C Analysis
---

**The Small Input**  

If you want to forget about the large input and go straight for the small, then Equal Sums might look like a classic dynamic programming problem. Here is a sketch of one possible solution in Python:

```
def GetSetWithSum(x, target):
  if target == 0: return []
  return GetSetWithSum(x, target - x[target]) + [x[target]]

def FindEqualSumSubsets(S):
  x = [0] + [None] * (50000 * 20)
  for s in S:
    for base_sum in xrange(50000 * 20, -1, -1):
      if x[base_sum] is not None:
        if x[base_sum + s] is None:
          x[base_sum + s] = s
        else:
          subset1 = GetSetWithSum(x, base_sum + s)
          subset2 = GetSetWithSum(x, base_sum) + [s]
          return subset1, subset2
  return None
```

The idea is that, in x, we store a way of obtaining every possible subset sum. If we reach a sum in two different ways, then we can construct two subsets with the same sum.

For the small input, this approach should work fine. However, x would have to have size 500 * 1012  for the large input. That is too big to work with, and you will need a different approach there.

  
**The Large Input**  

The first step towards solving the large input is realizing that the statement is very misleading! Let's suppose you have just 50 integers less than 1012. There are 250  ways of choosing a subset of them, and the sum of the integers in any such subset is at most 50 * 1012  < 250. By the  [Pigeonhole Principle](https://www.google.com/search?q=pigeonhole+principle), this means that there are two different subsets with the same sum.

So what does that mean for this problem? Well, even if you had just 50 integers to choose from instead of 500, the answer would never be "Impossible". You need to find some pair of subsets that have the same sum, and there is a lot of slack to work with. The trick is figuring out how to take advantage of that slack.

  
**The Birthday "Paradox" Method**

The simplest solution is based on a classic mathematical puzzle: the birthday paradox.

The birthday paradox says that if you have just 23 people in a room, then some two of them probably have the same birthday. This can be surprising because there are 365 possible days, and 23 is much smaller than 365. But it is true! One good way to look at is this: there are 23 choose 2 = 253 pairs of people, and each pair of people has a 1/365 chance of having the same birthday. In particular, the  _expected_  (aka average) number of pairs of people with the same birthday is 253 / 365 = 0.693... Once you write it that way, it is not too surprising that the probability of having at least  _one_  pair matching is about 0.5.

It turns out this exact reasoning applies to the Equals Sums problem just as well. Here is a simple algorithm:

-   Choose 6 random integers from  **S**, add them up, and store the result in a hash set. (Why 6? We'll come back to that later...)
-   Repeat until two sets of 6 integers have the same sum, then stop.

After choosing t sets, there will be t choose 2 pairs, and each set will have sum at most 6 * 1012. Therefore, the expected number of collisions would be approximately t2 / (12 * 1012). When t is around 106, this expectation will be near 1, and the reasoning from the birthday paradox says that we'll likely have our collision.

That's it! Since we can quickly generate 106  small subsets and put their sums into a hash-set, this simple algorithm will absolutely solve the problem. You may be worried about the randomness, but for this problem at least, you should not be. This algorithm is extremely reliable. By the way, this method will work on the small input as well, so you don't need to do the dynamic programming solution if you do not want to.

_Note:_  There are many similar approaches here that can work. For example, in our internal tests, one person solved the problem by only focusing on the first 50 integers, and trying random subsets from there. The proof below works for this algorithm, as well as many others.

  
**A Rigorous Proof**

If you have some mathematical background, we can actually prove rigorously that the randomness is nothing to worry about. It all comes down to the following version of the birthday theorem:

**Lemma:**  Let X be an arbitrary collection of N integers with values in the range [1, R]. Suppose you choose t + 1 of these integers independently at random. If N ≥ 2R, then the probability that these randomly chosen integers are all different is less than  `e-t2  / 4R`.

**Proof:**  Let xi  denote the number of integers in X with value equal to i. The number of ways of choosing t + 1 distinct integers from X is precisely

`sum(1 ≤ i1  < i2  < ... < it+1  ≤ R)  [ xi1  * xi2  * ... * xit+1  ]`.

For example, if t=1 and R=3, the sum would be  `x1  * x2  + x1  * x3  + x2  * x3`. Each term here represents the number of ways of choosing integers with a specific set of values. Unfortunately, this sum is pretty hard to work with directly, but  [Maclaurin's inequality](https://www.google.com/search?q=maclaurin%27s+inequality)  states that it is at most the following:

`(R choose t+1) * [ (x1  + x2  + ... + xR) / R ]t+1  
= (R choose t+1) * (N/R)t+1`.

On the other hand, the number of ways of choosing  _any_  t + 1 integers out of X is equal to  `N choose t+1`. Therefore, the probability p that we are looking for is at most:

`[ (R choose t+1) / (N choose t+1) ] * (N/R)t+1  
= R/N * (R-1)/(N-1) * (R-2)/(N-2) * ... * (R-t)/(N-t) * (N/R)t+1`.

Now, since N ≥ 2R, we know the following is true for all a ≤ t:

`(R-a) / (N-a)  
< (R - a/2)2  / [ R * (N-a) ] (this is because (R - a/2)2  ≥ R(R-a))  
≤ (R - a/2)2  / [ N * (R-a/2) ]  
= (R - a/2) / N.`

Therefore, p is less than:

`R * (R - 1/2) * (R - 2/2) * ... * (R - t/2) / Rt+1`.

It is now easy to check that  `(R-a/2) * (R-t/2+a/2) ≤ (R-t/4)2`, from which it follows that p is also less than:

`(R - t/4)t+1  / Rt+1  
= (1 - t/4R)t+1  
< (1 - t/4R)t.`

And finally, we use the very useful fact that  `1 - x ≤ e-x`  for all x. This gives us  `p < e-t2  / 4R`  as required.

  

In our case, X represents the sums of all 6-integer subsets. We have N = 500 choose 6 and R = 6 * 1012. You can check that N ≥ 2R, so we can apply the lemma to estimate the probability that the algorithm will still be going after t+1 steps:

-   If t = 106, the still-going probability is at most 0.972604477.
-   If t = 5*106, the still-going probability is at most 0.499351789.
-   If t = 107, the still-going probability is at most 0.062176524.
-   If t = 2*107, the still-going probability is at most 0.000014945.
-   If t = 3*107, the still-going probability is at most 0.00000000001.

In other words, we have a good chance of being done after 5,000,000 steps, and we will  _certainly_  be done after 30,000,000 steps. Note this is a mathematical fact, regardless of what the original 500 integers were.

**Comment:**  What happens if you look at 5-element subsets instead of 6-element subsets? The mathematical proof fails completely because N < R. In practice though, it worked fine on all test data we could come up with.

  
**A Deterministic Approach**

The randomized method discussed above is certainly the simplest way of solving this problem. However, it is not the only way. Here is another way, this time with no randomness:

-   Take 7,000,000 3-integer subsets of  **S**, sort them by their sum, and let the difference between the two closest sums be d1. Let X1  and Y1  be the corresponding subsets.
-   Remove X1  and Y1  from  **S**, and repeat 25 times to get Xi, Yi  and di  for i from 1 to 25.
-   Let Z = {d1, d2, ..., d25}. Calculate all 225  subset sums of Z.
-   Two of these subset sums are guaranteed to be equal. Find them and trace back through Xi  and Yi  to find two corresponding subsets of  **S**  with equal sum.

There are two things to show here, in order to justify that this algorithm works:

-   _**S**  will always have at least 7,000,000 3-integer subsets._  This is because, even after removing Xi  and Yi,  **S**  will have at least 350 integers, and 350 choose 3 > 7,000,000.
-   _Z will always have two subsets with the same sum._  First notice that the subsets in the first step have sum at most 3 * 1012, and so two of the sums must differ by at most 3 * 1012  / 7,000,000 < 500,000. Therefore, each di  is at most 500,000. Now, Z has 225  subsets, and each has sum at most 25 * 500,000 < 225, and so it follows from the Pigeonhole Principle that two subsets have the same sum.

Other similar methods are possible too. This is a pretty open-ended problem!

