# Josephus
The Josephus problem is a mathematical problem, where a group of soldiers are surrounded by the enemy. They prefer to die than be captured so they decide to stand in a circel. And the first soldier kills the second soldier, then the third soldier kills the fourth soldier and so on. When everyone has killed one soldier. they do the same thing; the first soldier kills the second and so on. Till the last soldier survives and that soldier has to kill him self.

But Josephus prefers to be captured instead of dying. But he can't surrender when everyone is alive because the soldiers will kill Josephus if he surrenders. So he has to calculate which spot in the circel he needs to stand at to die at last. So he can surrender when everyone is dead.

This problem is easy to solve when you are in a group of 3, 4 or 5 but as the number of soldiers goes up, it costs alot of time to calculate. Josephus was in a group of 41 people including himself.

These are the demands I used to rule out Josephus's position:

If the amount of soldiers is an even number or the power of two, then the soldier who dies at last stands on position #1.
If the amount doesn't meet demands above, then I will take the amount of soldiers minus the highest power of two with in that amount. Then we will use that subtraction x plus the power of two and increase with one.

Still no clue about what this problem is about? Watch this Numberphile episode dedicated to the Josephus math problem.

# https://youtu.be/uCsD3ZGzMgE
