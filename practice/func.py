"""TheFunctionWithin"""
def main(put_a, put_b, put_c, put_d):
    """_"""
    print(func_f(func_f(put_a)))
    print(func_g(func_f(put_a - put_b)))
    print(func_h(func_f(put_a + put_b), func_f(put_a + put_c), \
func_g(func_f(put_d**2))))
    print(func_i(func_h(func_f(put_a + put_b), func_f(put_a - put_c), \
func_g(func_f(put_d**2))), func_g(func_f(put_a - put_b)), func_f(func_f(func_f(func_f(func_f(put_c))))), (put_d**8)))

def func_f(var_x):
    """func_f"""
    func_f = 2*var_x
    return func_f

def func_g(var_x):
    """func_g"""
    func_g = (3*(var_x**4) - (var_x**3) + 2*(var_x**2) + 10)
    return func_g

def func_h(var_x, var_y, var_z):
    """func_h"""
    func_h = (((var_z + var_x)**2) - (var_x * var_y) + (var_y**2))
    return func_h

def func_i(var_a, var_b, var_c, var_d):
    """func_i"""
    func_i = (((var_a**2)+(var_b**2)+(var_c**2)) /((var_d**2) - (2*var_a*var_d) + (2*var_a)))
    return func_i
main(float(input()), float(input()), float(input()), float(input()))
