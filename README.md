# COMP 170 SU25 WEEK 04

This assignment has two parts: a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.

# Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.

# Code

This assignment has 5 tasks. Write your code in file `week04.py`. The file comes with a bit of testing code. Do not modify the testing code. Write your methods *above* the testing code. If your methods are correct, running the testing code will show that you passed the tests. In addition to correct logic, your code must meet any specifications mentioned in the descriptions below.


## Find the longest word
Write a method with header
```python
def longest_word(words: list[str]) -> str:
```
that returns the longest word (that is the longest string) in list `words`.


## Find the shortest word
Write a method with header
```python
def shortest_word(words: list[str]) -> str:
```
that returns the shortest word (that is the longest string) in list `words`.


## Find odd words
Write a method with header
```python
def odd_word(words: list[str]) -> list[str]:
```
that returns a list with all the strings in list `words` whose length is an odd number.


## Find average words
Write a method with header
```python
def average_word(words: list[str]) -> list[str]:
```
that returns a list with all the strings in `words` whose length is $\pm 1$ from the average length of all strings in `words`.


## Find an intersection
Write a method with header
```python
def intersect(foo: list[str], bar: list[str]) -> bool:
```
that returns `True` if lists `foo` and `bar` have at least one element in common, anf `False` otherwise. This method must have one and only one return statement.

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
