Problem C Analysis
---

This was a hard problem to wrap your head around, as evidenced by the results. The final solution was, however, surprisingly simple (although the argumentation for it is not).

Let us first consider a single case, with a single acceleration value a, and an arbitrarily large N. Suppose some strategy S1 takes you home in time T. Obviously a*T2 / 2 ≥ D, as a*T2 / 2 is the distance we travel if we start accelerating immediately and never brake.

We can propose an alternate strategy S2: first stop and wait for time T - sqrt(2 D/ A), and then start accelerating full speed and never brake. This will also bring you home in time T.

We have to prove that if S1 did not collide with the other car, neither will S2. We prove this by checking that S2 arrives at any point between the top of the hill and your home no earlier than S1.

Assume S1 was at some point X later than S2. Notice that the speed of S1 coming into X had to be larger than the speed of S2 — otherwise even accelerating full speed will not let S1 catch up with S2. But it is impossible to achieve a faster speed at X than S2: strategy S2 accelerated all the way from the top of the hill to X.

So, now we only need to consider strategies such as S1. We now just need to determine how long do we need to wait on the top of the hill.

One last thing to notice is that if the other car moves at constant speed between xi and xi+1, and our strategy does not put us in front of the other car at xi or at xi+1, then it does not intercept the other car in any intermediate point either. We know that because if we did intercept it in some intermediate point, it would mean that we were moving faster than the other car at the time of interception; and since we're accelerating, and the other car's speed is constant, we would end up in front of it at xi+1. Therefore passing the other car between xi and xi+1 leads to a contradiction, and it must be the case that we don't pass it.

With this reasoning complete, we now have two possible algorithms. One is a binary search: To check if a given waiting time T is long enough, we just need to check all the N points at which the other car can change its speed. To achieve a precision of 10-6, we will need around 40 iterations in the binary search. This means we solve each test case in O(N A) time, with the constant 40 hidden in the big-O notation — fast enough.

If we are worried about the constant factor of 40, we can also iterate over all points xi, and for each calculate the minimum waiting time needed not to intercept the other car at this point: ti - sqrt(2xi/a) for all i such that xi < D (you also have to include the moment where the other car reaches your house). This will make our solution run in O(N A) time without the pesky constant.

