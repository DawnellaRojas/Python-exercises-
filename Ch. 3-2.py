def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

# do_twice(print_spam)

word = 'hola'

def do_twice(f, word):
    f(word)
    f(word)

def print_spam(word):
    print('word')

do_twice(print_spam, word)





