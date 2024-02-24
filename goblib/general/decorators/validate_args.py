def validate_args(v_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            v_func(args, kwargs)
                    
            return func(*args, **kwargs)
        return wrapper
    return decorator