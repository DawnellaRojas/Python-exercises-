'''As an exercise, rewrite the function print_n from Section 5.8 using iteration instead of
recursion'''

# Exercise 5.8

'''def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)'''



def countdown(s,n):
    while n > 0:
        print(s)
        n = n - 1

countdown(3,6)