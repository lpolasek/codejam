Revenge of the Hot Dogs
---

Last year, several hot dog vendors were lined up along a street, and they had a tricky algorithm to spread themselves out. Unfortunately, the algorithm was very slow and they are still going. All is not lost though! The hot dog vendors have a plan: time to try a new algorithm!

The problem is that multiple vendors might be selling too close to each other, and then they will take each other's business. The vendors can move along the street at 1 meter/second. To avoid interfering with each other, they want to stand so that every pair of them is separated by a distance of at least  **D**  meters.

Remember that the street is really long, so there is no danger of running out of space to move in either direction. Given the starting positions of all hot dog vendors, you should find the minimum time they need before all the vendors are separated (each two vendors are at least  **D**  meters apart from each other).

### Input

Each point of the street is labeled with a number, positive, negative or zero. A point labeled  _p_  is  _|p|_  meters east of the point labeled  _0_  if  _p_  is positive, and  _|p|_  meters west of the point labeled  _0_  if  _p_  is negative. We will use this labeling system to describe the positions of the vendors in the input file.

The first line of the input file contains the number of cases,  **T**.  **T**  test cases follow. Each case begins with a line containing the number of points  **C**  that have at least one hot dog vendor in the starting configuration and an integer  **D**  -- the minimum distance they want to spread out to. The next  **C**  lines each contain a pair of space-separated integers  **P**,  **V**, indicating that there are  **V**  vendors at the point labeled  **P**.

### Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the minimum amount of time it will take for the vendors to spread out apart on the street. Answers with relative or absolute error of at most 10-6  will be accepted.

### Limits

1 ≤  **T**  ≤ 50.  
All the values  **P**  are integers in the range [-105, 105].  
Within each test case all  **P**  values are distinct and given in an increasing order. The limit on the sum of  **V**  values is listed below. All the  **V**  values are positive integers.

#### Small dataset

1 ≤  **D**  ≤ 5  
1 ≤  **C**  ≤ 20.  
The sum of all the  **V**  values in one test case does not exceed 100.

#### Large dataset

1 ≤  **D**  ≤ 106  
1 ≤  **C**  ≤ 200.  
The sum of all  **V**  values does not exceed 106

### Sample

  
#### Input  
    2
    3 2
    0 1
    3 2
    6 1
    2 2
    0 3
    1 1

#### Output  
    Case #1: 1.0
    Case #2: 2.5

