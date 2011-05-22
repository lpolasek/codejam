Problem A Analysis
---

The problem statement explains exactly what to do here. You just need to follow the instructions and not get too confused! We wanted to give you something to warm up with before the next two problems, which are both quite tricky.

First the winning percentage (WP) of each team needs to be calculated. This is fairly straightforward since the WP of team i only depends on team i's record. To do this part, we need to know the total number of wins for each team, as well as the total number of games played. We can then calculate WP[i] = Wins[i] / Total[i].

Next the OWP of each team needs to be calculated, but the OWP requires a modified WP for each opponent. Let's consider WP'[i][j], the winning percentage of team i if you exclude games against team j. To calculate WP'[i][j], we have to examine three possible cases.

1.  If team i never played versus team j, then WP' has no relevance and can be ignored.
2.  If team i did play versus team j and won the game, then WP'[i][j] = (Wins[i]-1) / (Total[i]-1).
3.  If team i did play versus team j and lost the game, then WP'[i][j] = (Wins[i]) / (Total[i]-1).

All that is left to do to calculate WP' is to try all pairs of teams and calculate the value if the two teams played.

Now that we have WP' for every pair of teams, we can calculate the OWP values. Let S[i] be the set of teams that team i played against. Then we can calculate OWP[i] as follows:

OWPSum[i] = 0  
for team j in S[i]:  
OWPSum[i] += WP'[j][i]  
OWP[i] = OWPSum[i] / size(S[i]).

Lastly, we need to calculate the OOWP for every team i. The OOWP uses the OWP which we already calculated:

OOWPSum[i] = 0  
for team j in S[i]:  
OOWPSum[i] += OWP[j]  
OOWP[i] = OOWPSum[i] / size(S[i]).

Finally, we can combine everything with the formula:  
RPI[i] = WP[i] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25.

By the way, this formula really is in use. It is not always very good at ranking teams though!

