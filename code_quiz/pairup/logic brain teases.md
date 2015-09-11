# Questions

1. You're in a dark room and there are 52 cards, some of which are flipped upside down. You know how many are flipped, say 10. Your task is to create two stacks with an equal number of cards upside-down in each.
2. You have 63 bottles of water and 1 containing a poison that tastes, smells and looks and feels/weighs the same as water. You have only 6 pigs and 6 buckets. Any amount of the poison will kill a pig within 10 minutes. You have 20 minutes to find out which bottle has the poison before you must chose a bottle to drink yourself. How can you kill the fewest number of pigs and determine the bottle which contains the poison.
3. There are 100 people in a room what is the likelihood that 2 share the same birthday.
4. Compute the cumulative product of all the elements in an array except one element. And do that excluding one element at a time. So your output is an array of N cumulative products of N-1 values.

The key to these problems (as Jeremy pointed out in his "meta" explanation) is to simplify the example of the problem down to a to the simplest possible problem that is informative about the larger problem. Solve that problem and then try to build it up to the general solution that solves the bigger problem. Lateral thinking may also be required. Easier said than done.

# Answers

1. Jeremy: Start with the problem to only 1 flipped card in a stack of 2, if you flipped 1 card into 1 pile and dealt the other card into your second pile, you'd end up with either both flipped or both unflipped. Now imagine that you have 1 flipped out of 4 cards. Again flip one card then deal out the remainder into the other pile. You still have 1 flipped in each or none flipped in either.  The total number of cards in each isn't equal, but the number of flipped cards is. And this works with an odd total number of cards as well. So just flip 10 cards over and place them in one pile and deal the remainder into the other. Problem solved.
2. Hobson: You can get away with killing no more than 3 pigs. Mark each bottle with an 6 bit integer in binary. Pour each bottle into one of 6 buckets for which it has a bit set in its label. Have a 3 pigs drink from each of the least polluted/full buckets and wait 10 minutes before checking the remaining 3 buckets with 3 pigs, only if all 3 live. I think the binary label number is revealed by the pattern of pigs that die or live. My logic doesn't quite work, but it gets close.
3. Jeremy: Consider the problem of only 2 people (1/365). But as soon as you try 3 you realize the combinatorics start to help quickly (1/365 + 1/364 + 1/363). Then for 4 there are 1+2+3 combinations so aproxiately 6/365. So for 100 It's very certain. You'd be better off calculating the probability of not finding a pair that match and subtracting that from 1.
4. Mike: Multiply all the numbers together and then divide out each of the values in the array one by one and those quotients are your N answers in O(N) time!

Jeremy came up with the "meta" solution which is to always gs.




right side up and upside down.
What can you do to create 2 stacks of cards

create 2 piles that have the same number of cards flipped
