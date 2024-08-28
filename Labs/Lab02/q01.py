# Name: Muhammad Ali
# Date: 28/8/24
# Desc: functions to cal area of different shapes

def cal_trapezoid(a, b, h):
    return (a+b)/2*h


def cal_parallelogram(b, h):
    return 1/2*b+h


def cal_cylinder_area(r, h):
    return (2 * 3.14 * r * r) + (2 * 3.14 * r * h)


def cal_cylinder_volume(r, h):
    return 3.14 * r * r * h


print(cal_trapezoid(2,3,6))
print(cal_parallelogram(6,4))
print(cal_cylinder_volume(6,5))
print(cal_cylinder_area(6,5))
