Problem A Analysis
------------------

_BAM! Robots gave us 6 extra seconds of cooperation. Good job, robots!_  
-- Cave Johnson (Portal 2)

Hopefully your robots were more focused on teamwork than Cave Johnson's were, or you would never get all the buttons pressed. Just be glad there were no mashy spike plates or potatoes to contend with! Perhaps in the finals...

Anyway, if you think about this problem from the perspective of a single robot, the strategy should be pretty intuitive: always move towards the next button and then push it as soon as it comes up in the sequence.

So the most natural solution to this problem is a straight simulation:

-   Keep track of which buttons have been pressed, and look ahead in the sequence to figure out which button is next for each robot.
-   One second at a time, have each robot move towards its next button.
-   Once it gets to the button, the robot should push it if it's next in the sequence, and just wait otherwise.

At most 100 buttons needs to be pressed altogether and the distance between buttons is at most 100, so this solution will run plenty fast.

If you get stuck on the implementation, remember that you can see other contestants' source code. There is no better way to learn!

