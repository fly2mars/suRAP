import logging

def unimplemented(func):
    '''
    A decorator function for print the current running function's name
    Just for the debug process. 
    '''
    def wrap_func(*args, **kwargs):       
        logging.debug('{}({}) is not implemented.'.format(func.__name__, args))
        func(*args, **kwargs)
    return wrap_func
