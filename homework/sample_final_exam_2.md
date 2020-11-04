# Python Sample Final Exam 2
## Question 1
Write code, using a loop, to print out the following sequence:
```
100, 90, 80, 70, 60, 50, 40, 30, 20, and 10
```
Your sequence should look the same, including commas, spaces, and "and".

## Question 2

Use Turtle to draw the following shapes:

![Image of turtle task](sample_final_exam_2_turtle.jpg)

The sides of the inner square are 50pt. The sides of the outer square are 250pt.

The distances between the left side of the outer square and the left side of the inner square is 50pt. The distance between the bottoms of the squares is also 50pt.


## Question 3
Use the following code which contains the key states in the United States presidential election, the number of electoral votes for the states, and the current number of votes for Biden and Trump in each state.

```python
#    ['state name', electoral votes, Biden votes, Trump votes]
MI = ['Minnesota', 10, 1671129, 1436422]
ME = ['Maine', 4, 327878, 254049]
FL = ['Florida', 29, 5269926, 5646949]
OH = ['Ohio', 18, 2576590, 3038247]
TX = ['Texas', 38, 5145367, 5810522]
NC = ['North Carolina', 15, 2655383, 2732120]
GA = ['Georgia', 16, 2279736, 2381870]
WI = ['Wisconsin', 10, 1420855, 1529223]
AZ = ['Arizona', 11, 1367211, 1236546]
NV = ['Nevada', 6, 553484, 528442]
MI = ['Michigan', 16, 1956696, 2198132]
PA = ['Pennsylvania', 20, 2286865, 2964853]

key_states = [MI, ME, FL, OH, TX, NC, GA, WI, AZ, NV, MI, PA]

print('STATE             ELECTORAL VOTES   BIDEN VOTES   TRUMP VOTES   PROJECTED')
```

Sort the key_states list so that the states and their votes are sorted with the highest electoral votes first and the lowest electoral votes last. Determine whether each state is projected to be a Biden win (Biden votes > Trump votes) or a Trump win (Trump votes > Biden votes).

```
STATE             ELECTORAL VOTES   BIDEN VOTES   TRUMP VOTES   PROJECTED
 North Carolina    15                2655383       2732120       Trump
 Wisconsin         10                1420855       1529223       Trump
```

Note: make sure you maintain data integrity, each state must have their correct votes.

Bonus: At the end, calculate how many electoral votes are projected to go to each presidential candidate.
