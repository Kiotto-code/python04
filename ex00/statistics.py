# def ft_statistics(*args: any, **kwargs: any) -> None:
#     for i in kwargs.values:
#         print(i)


# ft_statistics(1, 42, 360, 11, 64, toto=13, tutu=345, tata=890)
def ft_mean(*args: any) -> float:
    """return the mean of the given arguments"""
    return sum(args) / len(args)


def ft_median(*args: any) -> float:
    """return the median of the given arguments"""
    median_index = len(args)//2 - 1
    if (len(args) % 2) == 0:
        median = (args[median_index - 1] + args[median_index]) / 2
    else:
        median = args[median_index]
    return median


def ft_quartile(*args: any) -> list[float, float]:
    """return the 25% and 75% quartile of the given arguments"""
    return [float(sorted(args)[len(args) // 4]),
            float(sorted(args)[len(args) // 4 * 3])]


def ft_std(*args: any) -> float:
    """return the standard deviation of the given arguments"""
    return ft_var(*args) ** 0.5


def ft_var(*args: any) -> float:
    """return the variance of the given arguments"""
    return sum((x - ft_mean(*args)) ** 2 for x in args) / len(args)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """identify functions and call them with the given arguments"""
    try:
        dict = {
            "mean": ft_mean,
            "median": ft_median,
            "quartile": ft_quartile,
            "std": ft_std,
            "var": ft_var
        }
        for value in kwargs.values():
            try:
                if value in dict.keys():
                    print(value, ":", dict.get(value)(*args))
            except Exception:
                print("value: ", "Error")
    except Exception as e:
        print(e)
