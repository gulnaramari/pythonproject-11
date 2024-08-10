from datetime import datetime


def log_decorator(filename=""):
    """Decorator create log about function operation."""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            time_1 = datetime.now()
            try:
                result = func(*args, **kwargs)
                time_2 = datetime.now()
                message = (f"{func.__name__} ok."
                           f" Begin of work:{time_1}."
                           f" Final of work {time_2}.\n")
                if not filename:
                    print(message)
                else:
                    with open(filename, "a") as file:
                        file.write(message)
                return result
            except Exception as e:
                time_2 = datetime.now()
                error_message = (f"{func.__name__} error:"
                                 f" {e.__class__.__name__}. "
                                 f"Inputs: {args}, {kwargs}."
                                 f" Begin of work: {time_1}, "
                                 f"Error occurred at: {time_2}\n")
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
