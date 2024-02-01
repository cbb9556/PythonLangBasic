"""
装饰类的装饰器 - 单例模式 - 一个类只能创建出唯一的对象
上下文语法：
__enter__ / __exit__
"""
import threading

from functools import wraps


def singleton(cls):
    """单例装饰器"""
    instances = {}
    lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            # 相当于，进入时加锁，退出时解锁，这里如果已经被锁住，则无法获取，已经创建直接返回创建的单例
            # ref https://zhuanlan.zhihu.com/p/360604465
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President():

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    print(President.__name__)
    p1 = President('特朗普', '美国')
    p2 = President('奥巴马', '美国')
    print(p1 == p2)
    print(p1)
    print(p2)


if __name__ == '__main__':
    main()
