"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: leo
Date: 2018-03-02
"""

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')