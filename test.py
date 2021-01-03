import log_decorators
import log

class Log():
    @log_decorators.log_decorator
    def example(a, b, c):
        a = b + c
        b = a + c
        c = a + b
        d = "hi there"
        result = a + b + c
        return result
    
    example(a=5,b=4,c=3)