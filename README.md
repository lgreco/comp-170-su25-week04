# COMP 170 SU25 WEEK 03

This assignment has two parts: a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.

# Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.

# Code

## Diamond shape

Write a function `draw_diamond` that draws a diamond shape of a specified height passed as a parameter to the function. To solve this problem, first think what instructions you'll give someone drawing the diamong by pressing three keys on their keyboard: the space key, the hash mark key, and the enter key. For example, here's a 5-lines diamond and the keyboard instructions. It's important to *discover* if there is a connection between the line number and the number of spaces and hash marks (hint: there is).

```text
  #     : 1st line : space space hash enter
 ###    : 2nd line : space hash hash hash enter
#####   : 3rd line : hash hash hash hash hash enter
 ###    : 4th line : space hash hash hash enter
  #     : 5th line : space space hash enter
```

Solve this problem on paper first. Avoid the temptation to ask AI or to search online for a solution. It is an easy problem to code and the internet is full of solutions. This exercise however is about designing the solution on paper. Take out a piece of paper. Draw a few vertical and horizontal lines creating a square grid. Fill the squares to produce a diamond shape. Count the number of empty squares (spaces) and the number of filled squares (hashmarks) and discover how they relate to the line you are on (first line, second line etc.)

## Right triangle

Write a function `draw_right_triangle` that draws a right angle triangle whose height is specified as a parameter to the function.


## Compound interest

Write a function `compound_interst` that computes the compound interest for a given amount, a given annual interest rate, and a given period of time. For example, over a 5 year period, an initial investment of $1,000, earning 5% interest will accumulate as follows:

* 1st year: $1,000 principal + $1,000 x 0.05 interest = $1,050
* 2nd year: $1,050 principal + $1,050 x 0.05 interest = $1,102.50
* 3rd year: $1,102.50 principal + $1,102.50 x 0.05 interest = $1,157.62
* 4th year: $1,157.62 principal + $1,157.62 x 0.05 interest = $1,215.50
* 5th year = $1,215.50 principal + $1,215.50 x 0.05 interest = $1,276.27

The amount of $1,276.27 is the compound interest for this specific example. Your function *should not use* any exponential operations. Just loops, additions, and multiplications.

## Hollow square 

Write a function `draw_hollow_square` that draws a square that is empty in the middle. The size of the square's and the thickness of its edge should be given as parameters. For example `draw_hollow_square(8,2)` should produce the following drawing:

```text
########
########
##    ## 
##    ## 
##    ## 
##    ##  
########
########
```

# Reflect

Review the posted [solutions from the previous assignment](./solutions.py). Compare the posted solutions with your solutions. Notice the differences between your code and the solutions code and describe them. Trivial differences like the names of variables are not that important unless your names are really - I mean, *really -* weird.

## Frequent mistakes expected at this point

**Returning an *f-string* without understanding how it works.** Function `greet` has only one statement:
```python
return f"Hello {name}. How are you?"
```
Do you really understand what the f-string is and how it works? Can you explain it during an interview? Using code that you are not certain about can cause problems. It's fine to look up how others solve similar problems -- it's important however that you understand how the solution works and be in position to describe your understading. **In your reflection** describe how the f-string works by discussing couple of different scenarios they can be used.

**Iterating over a list without understanding how the `for` statement works.** Or, for that matter, how lists work. For-loops and lists are two core topics in programming. Everyone will expect you to know how the work and to be able to describe their functionality. **In your reflection** describe the for-statement iterates over a list by using a couple of examples.

**Repeating arithmetic operations.** When solving the quadratic equation, the quantity $b^2-4ac$ plays a major role. If the equation has real solutions, we use the quantity (called the *discriminant)* in three places. We don't have to evaluate it everytime, i.e., we do not have to perform the operation `b*b-4*a*c` in three different places. That's where using a variable comes handy. We can define a variable
```python
discriminant = b*b - 4*a*c
``` 
and use it as needed without repeating the arithmetic.

**Code has no comments.** Your code needs to have comments. Avoid trivial comments like:
```python
# compute the discriminant
discriminant = b*b-4*a*c
```
and try to come with more substative comments
```python
# compute the discriminant to use later for finding the real solutions
discriminant = b*b-4*a*c
```

## Read more about:

* [Type hints in Python](https://docs.python.org/3/library/typing.html); also useful [cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#functions)
* [f-strings in Python](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
* [lists in Python](https://docs.python.org/3/tutorial/datastructures.html). Also chapters 7.1 and 7.2 of the textbook.
* [the for statement](https://docs.python.org/3/reference/compound_stmts.html#for) and [for loop over a list in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements). Also chapter 2.3 and 7.1 of the textbook.
