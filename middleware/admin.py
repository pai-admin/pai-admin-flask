from functools import wraps


def AdminAuth(name="", auth="*", needLogin=True, needAuth=True):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return inner

    return decorator
