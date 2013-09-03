resistor_combinator
===================

A script for calculating optimum arrangement of series / parallel resistors to hone in on an exact value.

How precise is a 1% resistor?  Dave Jones of EEVBlog made a great couple of videos exploring this topic (see http://www.youtube.com/watch?v=1WAhTdWErrU and http://www.youtube.com/watch?v=kSmiDzbVt_U)

If you have a bunch of the same nominal value resistors, you can arrange them in a series-parallel columns.  You retain the same nominal value, but if you carefully arrange them, you can greatly improve the precision of the overall value (and they run cooler as well, which reduces their temperature drift!).

These arrangements all have the same nominal value (1 ohm):

![One resistor](http://i.imgur.com/xWIRXFr.png)
![Four resistors](http://i.imgur.com/CFBntk4.png)
![Nine resistors](http://i.imgur.com/AG0E1xW.png)

So, if we've measured a bunch of resistors, we should be able to have a computer arrange the optimum selection of resistors to cancel out each others' error, resulting in an overall value which is much closer to the desired value (e.g. 1.0000 ohms).

If you don't have a good measurement rig yet, you can still play with the code by generating some example data:

Let's generate a random set of 25 resistors of 1 ohm and 5% precision.

![generate test data](http://i.imgur.com/8LhN9RK.png)

This will print out the random values, and also dump them into a file called random_values.csv.

Now, let's iterate towards the best possible 3x3 combination.

![compute ideal arrangement](http://i.imgur.com/VpdVcgm.png)

This script tries all possible combinations, and iteratively spits out the best value it has found thus far.  It's output will slow down as it runs, as better solutions become more scarce.  Right now the script is configured to 

TODO: when the user quits the script, spit out the actual arrangement, so they can solder up that particular arrangement.

