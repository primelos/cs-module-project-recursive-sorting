def sum_list(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum

# print(sum_list([1,2]))


def sum_list_recursive(n):
    if len(n) == 1:
        return n[0]
    
    return n[0] + sum_list_recursive(n[1:])

llist = [2,3,4]
# print(sum_list_recursive(llist))


def print_to_zero(n):
    print (n)
    if n <= 0:
        return
    return print_to_zero(n - 1)
# hi=int(input('enter '))
# print_to_zero(hi)

# print(llist[1:])

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n-1)

# print(recursive_factorial(5))

# print(recursive_factorial(5) == 120)
# print(recursive_factorial(4) == 100)

def iter_factorial(n):
    total = 1
    while n != 1:
        total *= n
        n -= 1
    return total

# print(recursive_factorial(4) == iter_factorial(4))


def  iter_power(a,b):




    if b == 0:
        return 1
    product = a
    while b != 1:
        product *= a
        b -= 1
    return product 

# print(iter_power(2,3))

def add_two(num):
    return num + 2


def add_four(num):
    return add_two(add_two(num))

# print(add_two(2))
# print(add_four(6))

def recursive_fib(n):
    if n <= 1:
        print(n)
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

print(recursive_fib(4))