# coding=utf-8
import math
import matplotlib as mp
import numpy as np


def get_avg(sample):
    u"""Среднее значение выборки."""
    return sum(sample) / len(sample)


def get_sample_dispersion(sample):
    u"""Выборочная дисперсия."""
    squares_of_sample = list(
        map(lambda x: x**2, sample)
    )
    return (
        get_avg(squares_of_sample)
        - get_avg(sample) ** 2
    )


def get_std_deviation(sample):
    u"""Оценка среднеквадратического отклонения."""
    return math.sqrt(
        get_sample_dispersion(sample)
    )


def get_correlation(X, Y):

    xy_pairs = zip(X, Y)
    xy_prod_list = list(
        map(
            lambda x_y: x_y[0] * x_y[1],
            xy_pairs
        )
    )

    x_avg = get_avg(
        X
    )

    y_avg = get_avg(
        Y
    )

    Sx = get_std_deviation(X)
    Sy = get_std_deviation(Y)
    
    return (
        (get_avg(xy_prod_list) - x_avg * y_avg) / (Sx * Sy)
    )


test = [1, 2, 3]
# avg = 2
# disp = 14 / 3 - 4 = 0.6666

test2 = [4, 5, 6]

cor = get_correlation(
    test,
    test2
)

X = [
    0, 4, 10,
    15, 21, 29,
    36, 51, 68
]

Y = [
    66.7, 71.0, 76.3,
    80.6, 85.7, 92.9,
    99.4, 113.6, 125.1
]

a = [
    3, 8, 19,
    41, 22, 12,
    35, 9, 72,
    53
]

b = [
    12, 41, 122,
    203, 106, 52,
    197, 42, 439,
    247
]


x_avg = get_avg(
    X
)

y_avg = get_avg(
    Y
)

Dsx = get_sample_dispersion(
    X
)

Dsy = get_sample_dispersion(
    Y
)

Sx = get_std_deviation(X)
Sy = get_std_deviation(Y)

cor = get_correlation(
    X, Y
)

print(
    u"""Average x = {0}, Average y = {1}
    Dsx = {2}, Dsy = {3},
    Sx = {4}, Sy ={5},
    Ro = {6} """.format(
        x_avg,
        y_avg,
        Dsx,
        Dsy,
        Sx,
        Sy,
        cor
    )
)