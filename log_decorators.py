import sys, os, functools
from inspect import getframeinfo, stack
import log


def log_decorator(_func=None):
    def log_decorator_info(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Build logger object
            logger_obj = log.get_logger()
 
            result = 0
            py_file_caller = getframeinfo(stack()[1][0])
            extra_args = { 'func_name_override': func.__name__,
                           'file_name_override': os.path.basename(py_file_caller.filename) }
            for key, value in kwargs.items():
                logger_obj.debug("variable {} = {}" .format (key,value), extra=extra_args)
                result = value+result
            value = func(*args, **kwargs)
            logger_obj.debug(f"variable d = hi there", extra=extra_args)
            logger_obj.debug(f"variable result = {result!r}", extra=extra_args)
        # Return the pointer to the function
        return wrapper
    # Decorator was called with arguments, so return a decorator function that can read and return a function
    if _func is None:
        return log_decorator_info
    # Decorator was called without arguments, so apply the decorator to the function immediately
    else:
        return log_decorator_info(_func)