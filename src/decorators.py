def log_decorator(filename=""):
    """Decorator create log about function operation."""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            # time_1 = datetime.now()
            try:
                result = func(*args, **kwargs)
                # time_2 = datetime.now()
                message = (f"{func.__name__} ok")
                if not filename:
                    print(message)
                else:
                    with open(filename, "a") as file:
                        file.write(message)
                return result
            except Exception as e:
                # time_2 = datetime.now()
                error_message = (f"{func.__name__}:"
                                 f" {e.__class__.__name__}."
                                 f" Inputs: {args}, {kwargs}")
                if not filename:
                    print(error_message)
                else:
                    with open(filename, "a") as file:
                        file.write(error_message)
                raise

        return wrapper

    return my_decorator


@log_decorator()
def function(x, y):
    return x + y


function(1, 3)
