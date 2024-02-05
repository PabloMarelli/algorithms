"""
Recursion

Algorithm that defines a function that calls itself until a certain condition is met. Its a simplified while loop as a way to describe it.

I like this quote by Leigh Caldwell
on Stack Overflow: “Loops may achieve a performance gain for
your program. Recursion may achieve a performance gain for your
programmer. Choose which is more important in your situation!”
"""

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

countdown(10)
