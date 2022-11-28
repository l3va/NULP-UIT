from math import sqrt, asin, fabs, sin, cos

# task 1
def calculate_func1(x, y, z):
    try:
        f = sqrt(10 * (x ** (1 / 3) + x ** (y + 2))) * (asin(z) ** 2 - fabs(x - y))  # -40.6306
    except Exception as e:
        f = None
        print('impossible to calculate f')
    finally:
        return f

try:
    x = float(input("x="))  # 0.01655
    y = float(input("y="))  # -2.75
    z = float(input("z="))  # 0.15
except Exception as e:
    x, y, z = 0, 0, 0
    print(f'incorrect input')

print(calculate_func1(x, y, z))
input()
