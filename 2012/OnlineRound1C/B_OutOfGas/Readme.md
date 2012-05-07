Out of Gas
---

Your car is out of gas, and you want to get home as quickly as possible! Fortunately, your home is at the bottom of a hill and you (in your car) are at the top of it. Unfortunately, there is a car in front of you, and you can't move past it. Fortunately, your brakes are working and they are  _very_  powerful.

You  _start_  at the top of the hill with speed 0 m/s at time 0 seconds. Gravity is pulling your car down the hill with a constant acceleration. At any time, you can use your brakes to reduce your speed, or temporarily reduce your acceleration, by any amount.

How quickly can you reach your home if you use your brakes in the best possible way?

### Input

The first line of the input gives the number of test cases,  **T**.  **T**  test cases follow. The first line of each test case contains three space-separated numbers: a real-valued number  **D**, the distance in meters to your home down the hill; and two integers,  **N**  and  **A**. The distance  **D**  will be given in  _exactly 6 decimal places_.

**N**  lines follow, each of which contains two space-separated, real-valued numbers: a time  **t**i  in seconds, and a position  **x**i  in meters. The  **t**i  and  **x**i  values will be given in  _exactly 6 decimal places_.

One line follows, with  **A**  space-separated, real-valued numbers  **a**i, which are accelerations in  `m/s2`. The accelerations will be given in  _exactly 2 decimal places_.

The other car's position is specified by the (**t**i,  **x**i) pairs. The car's position at time  **t**i  seconds is  **x**i  meters measured from the top of the hill (i.e. your initial position). The car travels at constant speed between time  **t**i  and  **t**i+1. The positions and times will both be given in increasing order, with  **t**0=0.

For example, if t5=10, x5=20, t6=20, x6=40, then 10 seconds after the  _start_, the other car is 20 meters down the hill; 15 seconds after the  _start_, the other car is 30 meters down the hill; and 20 seconds after the  _start_, the other car is 40 meters down the hill.

### Output

For each test case, output one line containing "Case #c:", where c is the case number (starting from 1). Then output  **A**  lines, the ith  of which contains the minimum number of seconds it takes you to reach your home if your acceleration down the hill due to gravity is  **a**i, and you use your brakes in the best possible way. Answers within an absolute or relative error of 10-6  of the correct answer will be accepted. There should be no blank lines in the output.

### Notes

**Position and Acceleration:**  An object with a constant acceleration  `a m/s2`  and starting speed of  `v0  m/s`  will move a distance of v0*t + 0.5*a*t2  after  `t`  seconds.

**Distance on the slope:** All the distances and accelerations are given with respect to the straight line down the hill. They are **not**, for example, horizontal distances; so if your car is accelerating at `2 m/s2` with an initial speed of `0 m/s`, and the other car is stopped at x=1, it will take exactly 1 second to reach the other car.

**The other car:**  You may never pass the other car, which means that at no time shall your distance down the hill be greater than that of the other car. It may be equal. The cars should be considered as point masses.

**Output values:**  You can print as many decimal places as you like in the output. We will read and compare your answers with ours, and at that time we will be using 10-6  as a threshold for inaccuracy. So 25, 25.0 and 25.000000 are the same from our perspective. Trailing zeros after the decimal point does not matter.

### Limits

1 ≤  **T**  ≤ 20.  
1.0 ≤  **D**  ≤ 104.  
1.0 ≤  **a**i  ≤ 9.81.  
0.0 ≤  **t**i  ≤ 105.  
0.0 ≤  **x**i  ≤ 105.  
**t**i  <  **t**i+1.  
**x**i  <  **x**i+1.  
**t**0  = 0  
**x**N-1  ≥  **D**.  

#### Small dataset

1 ≤  **N**  ≤ 2.  
1 ≤  **A**  ≤ 10.  

#### Large dataset

1 ≤  **N**  ≤ 2000.  
1 ≤  **A**  ≤ 250.  

### Sample

### Input  
    3
    1000.000000 2 3
    0.000000 20.500000
    25.000000 1000.000000
    1.00 5.00 9.81
    50.000000 2 2
    0.000000 0.000000
    100000.000000 100.000000
    1.00 1.01
    10000.000000 3 1
    0.000000 0.000000
    10000.000000 0.100000
    10000.100000 100000.000000
    1.00

#### Output  
    Case #1:
    44.7213595
    25.000000
    25
    Case #2:
    50000
    50000
    Case #3:
    10140.974143

