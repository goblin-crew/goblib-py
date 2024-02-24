def validate_args(v_func: function):
    def decorator(func: function):
        def wrapper(*args, **kwargs):
            
            v_func(args, kwargs)
                    
            return func(*args, **kwargs)
        return wrapper
    return decorator