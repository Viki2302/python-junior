def time_execution(function):
    def wrapper(n):
        import time
 
        # начальное время
        start_time = time.time()
        function(n)
        # конечное время
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
 
    return wrapper
    
def factorial(n):
    count = 0
    while n >=5:
        n //= 5
        count += n
    return count

decorate = time_execution(factorial)
decorate(5)
