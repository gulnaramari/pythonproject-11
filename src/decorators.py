from datetime import datetime

def log_decorator(filename=""):
    """Decorator create log about function operation."""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "w") as file:
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
def function(x, y):
    return x + y


def timer(func):
    def wrapper(*args, **kwargs):
        time_1 = datetime.now()
        result = func(*args, **kwargs)
        time_2 = datetime.now()
        print(time_2 - time_1)
        return result

    return wrapper



function = timer(function)



function(1, 7)
