Tide Goes In, Tide Goes Out
---

You are kayaking through a system of underground caves and suddenly realize that the tide is coming in and you are trapped! Luckily, you have a map of the cave system. You are stuck until the tide starts going out, so you will be here for a while. In the meantime, you want to determine the fastest way to the exit once the tide starts going out.

The cave system is an  **N**  by  **M**  grid. Your map consists of two  **N**  by  **M**  grids of numbers: one that specifies the height of the ceiling in each grid square, and one that specifies the height of the floor in each grid square. The floor of the cave system is porous, which means that as the water level falls, no water will remain above the water level.

You are trapped at the north-west corner of the map. The current water level is  **H**  centimeters, and once it starts going down, it will drop at a constant rate of 10 centimeters per second, down to zero. The exit is at the south-east corner of the map. It is now covered by water, but it will become passable as soon as the water starts going down.

At any time, you can move north, south, east or west to an adjacent square with the following constraints:

-   The water level, the floor height of your current square, and the floor height of the adjacent square must all be at least 50 centimeters lower than the ceiling height of the adjacent square. Note: this means that you will never be able to enter a square with less than 50 centimeters between the floor and the ceiling.
-   The floor height of the adjacent square must be at least 50 centimeters below the ceiling height of your current square as well.
-   You can never move off the edge of the map.

Note that you can go up or down as much as you want with your kayak. (You're very athletic from all this kayaking!) For example, you can go from a square with floor at height 10 centimeters to an adjacent square with floor at height 9000 centimeters (assuming the constraints given above are met).

These constraints are illustrated below: 

![Constraints](diagram.png)  

-   In the first image, you can't move to the right because the water level is less than 50 centimeters below the ceiling height of the adjacent square.
-   In the second image, you can't move to the right because the floor height of your current square is less than 50 centimeters below the ceiling height of the adjacent square.
-   In the third image, you can't move to the right because the floor height of the adjacent square is less than 50 centimeters below the ceiling height of the adjacent square. You'll never be able to enter that square from any direction.
-   In the fourth image, you can't move to the right because the floor height of the adjacent square is less than 50 centimeters below the ceiling height of the current square.

When moving from one square to another, if there are at least 20 centimeters of water remaining on the current square when you start moving from it, it takes 1 second to complete the move (you can use your kayak). Otherwise, it takes 10 seconds (you have to drag your kayak). Note that the time depends only on the water level in the square you are leaving, not in the square you are entering.

It will be a while before the tide starts going out, and so you can spend as much time moving as you want before the water starts going down. What matters is how much time you will need from the moment the water starts going down until the moment you reach the exit. Can you calculate this time?

### Input

-   The first line will contain a single integer,  **T**: the number of test cases
-   It is followed by  **T**  test cases, each starting with a line containing integers  **H**,  **N**  and  **M**, representing the initial water level height, in centimeters, and the map dimensions. The following 2**N**  lines contain the ceiling and floor heights as follows:
    -   The next  **N**  lines contain  **M**  space-separated integers each. The  _j_th integer in the  _i_th row represents  **Cij**, the height of the ceiling in centimeters at grid location  _(j, i)_, where increasing  _i_  coordinates go South, and increasing  _j_  coordinates go East.
    -   The next  **N**  lines contain  **M**  space-separated integers representing the heights of the floor, in the same format.
-   At the starting location, there will always be at least 50 cm of air between the ceiling and the starting water level, and at least 50 cm between the ceiling and the floor.
-   The exit location will always have at least 50 cm of air between the ceiling and the floor.
-   There will always be a way out (you got in, after all!).

### Output

For each test case, output one line containing "Case #x: t", where x is the case number (starting from 1), and t is the time, in seconds, starting from when the tide begins going out, that it takes you to make your way out of the cave system. Answers within an absolute or relative error of 10-6  of the correct answer will be accepted.

### Notes

It is possible that you can go through the whole cave system before the tide starts dropping. In this case you will be able to wait at the exit for the tide to start dropping, so the answer in this case should be zero (this is the case in the fourth of the sample test cases).

### Limits

#### Small dataset

1 ≤  **T**  ≤ 50.  
1 ≤  **N, M**  ≤ 10.  
1 ≤  **H**  ≤ 1000.  
1 ≤  **Fxy**  ≤  **Cxy**  ≤ 1000.

#### Large dataset

1 ≤  **T**  ≤ 50.  
1 ≤  **N, M**  ≤ 100.  
1 ≤  **H**  ≤ 10000.  
1 ≤  **Fxy**  ≤  **Cxy**  ≤ 10000.

### Sample

  
#### Input  
    4
    200 1 2
    250 233
    180 100
    100 3 3
    500 500 500
    500 500 600
    500 140 1000
    10 10 10
    10 10 490
    10 10 10
    100 3 3
    500 100 500
    100 100 500
    500 500 500
    10 10 10
    10 10 10
    10 10 10
    100 2 2
    1000 1000
    1000 1000
    100 900
    900 100
  
#### Output  
    Case #1: 11.7
    Case #2: 3.0
    Case #3: 18.0
    Case #4: 0.0

