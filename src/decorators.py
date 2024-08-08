def log_decorator(filename=""):
    """This decorator creates Log information"""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time_1 = time
                result = func(*args, **kwargs)
                time_2 = time
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


@log_decorator(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
my_function(1, "2")