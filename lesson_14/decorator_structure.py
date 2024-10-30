import time

storage = {
    # "key": "value"
}

def my_decorator(func): # приймає декоровану функцію
    a = 10
    def wrapper(): # імітує поведінку оригінальної функції
        print("-> ACTION BEFORE")
        if "key" in storage:
            print("GET FROM STORAGE")
            result = storage.get("key")
        else:
            print(f"EXECUTE FUNCTION {func.__name__}")
            result = func()
            # result = 0

        print("ACTION AFTER ->")
        return result
    return wrapper


def measure_time(func, *args):
    print(f"Decorator measure_time get: func={func} {args}")
    def wrapper(*wrapper_args): # та приймає ії аргументи
        print(f"Wrapper measure_time get: {wrapper_args}")
        start_time = time.time()
        func_result = func(*wrapper_args)
        duration = (time.time() - start_time) * 1000
        print(f"Execute {func.__name__} in {duration} ms")
        return func_result
    return wrapper

def validate_args(func, *args):
    print(f"Decorator validate_args get: func={func} {args}")
    def wrapper(*wrapper_args): # та приймає ії аргументи

        print(f"Wrapper validate_args get: {wrapper_args}")
        new_args = []
        for a in wrapper_args:
            if isinstance(a, str):
                new_args.append(a.lower())
            else:
                new_args.append(int(a))
        print("Valid", new_args)

        func_result = func(new_args)
        return func_result
    return wrapper

@measure_time
@validate_args
def my_decorated_function(*args):
    print("Hello from function")

my_decorated_function(1, 2, 43, 5, "l") # -> wrapper()



@my_decorator
@measure_time
def get_user_email():
    time.sleep(2)
    return "user@beetroot.com"

# email = get_user_email()
# print("\n>>>",  email)
get_user_email = measure_time(get_user_email)
print("WITHOUT SYNTAX SUGAR", get_user_email())

@measure_time
@validate_args
def func_with_args(arg_1, arg_2):
    print(f"{arg_2} or {arg_1} 🤔")
    time.sleep(1)
    return arg_2 or arg_1



# result = func_with_args(-20, "0")
# print(result)


# def backend_user_route(func):
#     def wrapper(*args):
#         user_id = request.user_id
#         user = find_in_db("user", id=user_id)
#         result = func(user=user)
#         return result
#     return wrapper
#
#
#
# @backend_user_route
# def get_user_orders(user = None):
#     ...
#
#
# @backend_user_route
# def get_user_payments()


# get_user_orders()