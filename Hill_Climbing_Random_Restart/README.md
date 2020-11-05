## Hill Climbing Algorithm (Random Restart)

Consider a simpler game involving 3 numbers and a 2 digit target:
Numbers=[2,5,9]
Target: 1
Solution: ((5)*2)-9 = 1
The operations are applied in order so you should ignore order of operations and just evaluate everything in order of appearance. 

Implement a random-restart hill climbing(pg 124) algorithm that attempts to find the expression that is as close as possible to the target. 
Keep track of the best value your search finds and print out the expressions and objective value each time you find a better expression.
Remember that local search starts at a random state on each run through, the first state of your search will be a complete expression. 
At each state the player can manipulate the sentence in one of two ways:


swap(n1,n2) - swaps the position of the number at index n1 with the one at index n2
change(s1,op) - changes the operator at s1 to op



Using the same example above but cast as local search:
Given:((5)+9)-2 (a random starting state)
Target: 1
Swap(2,3): ((5)+2)-9
Change(1,*): ((5)*2)-9
Solution: ((5)*2)-9 = 1

Considerations:

You can implement Swap and Change however you'd like (more arguments, different indexing system, etc)
You must use all the numbers
Division is not limited to integer quotients - i.e. you can have decimal answers. 
Using the same number pool and target each time, run your program for three different durations. 
The length of durations are up to you but make them interesting - i.e. each duration should terminate with a different best value.
