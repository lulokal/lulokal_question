## Problem 1
 Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence 
after sorting them alphabetically.
Suppose the following input is supplied to the program:

Input:
>without,hello,bag,world

Output should be:

>bag,hello,without,world

## Problem 2
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
```
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

Example:

If the following tuples are given as input to the program:
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
```
## Problem 3
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:

1. Sort based on name;
2. Then sort based on age;
3. Then sort by score.

The priority is that name > age > score.
If the following tuples are given as input to the program:
- Tom,19,80
- John,20,90
- Jony,17,91
- Jony,17,93
- Jason,21,85

Then, the output of the program should be:

```[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]```
