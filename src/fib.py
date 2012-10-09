def fib(n):
    print 'calc fib of: ', n
    if n > 1:
        return n * fib(n-1)
    else:
        print "that's the end"
        return 1
        
fib(20)