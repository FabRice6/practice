'''
Recursion is when a function calls itself.

It's an alternative to the for-loop.

Youtube: 
- https://www.youtube.com/watch?v=XkL3SUioNvo
- https://www.youtube.com/watch?v=TqqQld6m6A0
'''

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(50))