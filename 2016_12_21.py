# _*_ coding:utf-8 _*_
"""
在不调用函数的情况下，求一个数的开方
"""
import sys
sys.setrecursionlimit(5000)  # 设置递归深度


# radicand：被开方数，sqr_result：开方结果，误差：allowable_err， 指数：exponent
def figure_sqr(radicand=10.0, sqr_result=3.0, allowable_err=0.001, exponent=2.0):
    if (radicand - sqr_result ** exponent) > 0.1:
        sqr_result += allowable_err
        figure_sqr(radicand, sqr_result)
    else:
        print sqr_result
figure_sqr(100.0, 7.0, 0.1, 2.0)
