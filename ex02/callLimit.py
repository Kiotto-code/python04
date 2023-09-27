def callLimit(limit: int):
    """set the count to 0 and return a function that will limit by the count"""
    try:
        count = 0

        def callLimiter(function):
            """set the function as an object inside"""
            def limit_function(*args: any, **kwds: any):
                """check the limit times of func being called and apply the\
func with given args or kwargs"""
                nonlocal count
                if count < limit:
                    result = function(*args, **kwds)
                    count += 1
                    return result
                else:
                    print(f"Error: {function} called too many times.")

            return limit_function

        return callLimiter
    except Exception as e:
        print(e)
