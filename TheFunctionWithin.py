"""TheFunctionWithin"""
 
 
def ans():
    """thefunctionwithin"""
    put_a = float(input())
    put_b = float(input())
    put_c = float(input())
    put_d = float(input())
    print(func1(func1(put_a)))
    print(func2(func1(put_a - put_b)))
    print(func3((func1(put_a + put_b)), (func1(put_a + put_c)), (func2(func1(put_d ** 2)))))
    print(func4((func3(func1(put_a + put_b), func1(put_a - put_c), func2(func1(put_d ** 2)))), \
func2(func1(put_a - put_b)), func1(func1(func1(func1(func1(put_c))))), put_d ** 8))
 
def func1(var_x):
    """funcf"""
    result_1 = 2 * var_x
    return result_1
 
def func2(var_x):
    """funcg"""
    result_2 = (3 * (var_x ** 4)) - (var_x ** 3) + (2 * (var_x ** 2)) + 10
    return result_2
 
def func3(var_x, var_y, var_z):
    """funch"""
    result_3 = ((var_z + var_x) ** 2) - (var_x * var_y) + (var_y ** 2)
    return result_3
 
def func4(var_a, var_b, var_c, var_d):
    """funci"""
    result_4 = ((var_a ** 2) + (var_b ** 2) - (var_c ** 2)) / ((var_d ** 2) - \
(2 * var_a * var_d) + (2 * var_a))
    return result_4
 