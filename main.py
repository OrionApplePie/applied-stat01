# coding=utf-8
import math
import matplotlib.pyplot as plt
import numpy as np



class Sample:
    u"""Класс выборки."""
    
    def __init__(self, sample=[], name=u'New sample'):
        self.sample = sample
        self.name = name
        self.avg = self._get_avg(self.sample)
        self.disp = self._get_sample_dispersion()
        self.sko = self._get_std_deviation()

    @staticmethod
    def _get_avg(sample):
        u"""Среднее значение выборки."""
        return sum(sample) / len(sample)

    def _get_sample_dispersion(self):
        u"""Выборочная дисперсия."""
        squares_of_sample = list(
            map(lambda x: x**2, self.sample)
        )
        return (
            self._get_avg(squares_of_sample)
            - self._get_avg(self.sample) ** 2
        )

    def _get_std_deviation(self):
        u"""Оценка среднеквадратического отклонения."""
        return math.sqrt(
            self._get_sample_dispersion()
        )
    
    def get_sum_of_prod(self, other):
        
        xy_pairs = zip(self.sample, other.sample)
        xy_prod_list = list(
            map(
                lambda x_y: x_y[0] * x_y[1],
                xy_pairs
            )
        )
        
        return self._get_avg(xy_prod_list) 
    
    def get_correlation_coef(self, other):
        # if type(other) == type(self):
        #     print('cool!!!----')
        
        xy_pairs = zip(self.sample, other.sample)
        xy_prod_list = list(
            map(
                lambda x_y: x_y[0] * x_y[1],
                xy_pairs
            )
        )
        
        return (
            (self._get_avg(xy_prod_list) 
             - self.avg * other.avg) 
             / (self.sko * other.sko)
        )
    
    def get_correlation_equation(self, other):
        
        ro = self.get_correlation_coef(other)
        
        def x_to_y(y):
            return (
                self.avg + ro * (self.sko / other.sko) * (y - other.avg) 
            )
        
        def y_to_x(x):
            return (
                other.avg + ro * (other.sko / self.sko) * (x - self.avg) 
            )

        return x_to_y

    def get_parameters_as_string(self):
        return u"""---> {name}
               Average = {avg},
               D = {disp},
               S = {sko},""".format(
                   name=self.name,
                   avg=self.avg,
                   disp=self.disp,
                   sko=self.sko
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

words = [
    3, 8, 19,
    41, 22, 12,
    35, 9, 72,
    53
]

letters = [
    12, 41, 122,
    203, 106, 52,
    197, 42, 439,
    247
]

rrr = [
    2.01, 2.01,
    2.00, 2.00,
    1.98, 1.99
]
# Words = Sample(words, 'Words')
# Letters = Sample(letters, 'Letters')

# print(Words.get_parameters_as_string())
# print(Letters.get_parameters_as_string())

# print('Ro = {}'.format(
#     Words.get_correlation_coef(Letters)
# ))

# x_to_y_eq = Words.get_correlation_equation(Letters)

# # plots

# t = np.arange(0., 150., 5.)

# plt.plot(words, letters, 'ro', t, x_to_y_eq(t), 'b')
# # plt.axis([0, 6, 0, 20])
# plt.show()

x = Sample(X, 'X')
y = Sample(Y, 'Y')

rgr2 = Sample(rrr, 'rgr-2')

print(x.get_parameters_as_string())
print(y.get_parameters_as_string())
# print(rgr2.get_parameters_as_string())

print('Ro = {}, '.format(
    x.get_correlation_coef(y)
))
print('Sum of xy = {}'.format(
     x.get_sum_of_prod(y)
))
x_to_y_eq = x.get_correlation_equation(y)

# plots

t = np.arange(50., 130., 3.)

plt.plot(Y, X, 'ro', t, x_to_y_eq(t), 'b')
plt.show()