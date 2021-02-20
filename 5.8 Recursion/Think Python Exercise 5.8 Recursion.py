"""As an exercise, draw a stack diagram for print_n called with s = 'Hello' and n=2. Then
write a function called do_n that takes a function object and a number, n, as arguments, and
that calls the given function n times."""

def do_n(s, n):
    if n <= 0:
        return
    print(s)
    do_n(s, n-1)

do_n('Hello',2)

# Stack Diagram
#  __main__ ------>
# countdown -----> 1 ----> Hello
# countdown -----> 0 ----> Hello
