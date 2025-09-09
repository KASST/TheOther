import time
from my_lib.decorators import timer, logger

@logger
@timer
def add(a, b):
    """一个简单的加法函数，并模拟耗时"""
    print("--- 开始执行 add 函数核心逻辑 ---")
    time.sleep(1) # 模拟一些计算
    result = a + b
    print("--- add 函数核心逻辑执行完毕 ---")
    return result

if __name__ == "__main__":
    add(4, 5)
