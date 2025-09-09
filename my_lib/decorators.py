import time
import functools

def timer(func):
    """一个打印函数执行时间的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"函数 {func.__name__!r} 执行耗时: {run_time:.4f} 秒")
        return result
    return wrapper

def logger(func):
    """一个记录函数参数和返回值的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__!r}，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__!r} 返回: {result!r}")
        return result
    return wrapper

def cache(func):
    """一个简单的缓存函数调用结果的装饰器"""
    cache_storage = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 将可变的kwargs转换为不可变的元组，以便作为字典的键
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key not in cache_storage:
            print(f"缓存未命中，开始计算 {func.__name__}...")
            cache_storage[cache_key] = func(*args, **kwargs)
        else:
            print(f"缓存命中 {func.__name__}!")
        return cache_storage[cache_key]
    return wrapper