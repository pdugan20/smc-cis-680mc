#!/usr/local/bin/python3
# Douglas Putnam
# functions_lab4.py

def main():
    print(sum_all(1,2,43))
    print(get_volume(c=12,b=2,a=99))
    for a in alphas():
        print(a)
    @td_decorator
    def test_td(alist):
        for a in alist:
            print(a)
    test_td(1,2,3,4)
# alphas()
# One Way
def alphas():
    str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in str:
        yield(i)

'''
A more elegant way:
# generator function to return successive uppercase and lowercase letters
# But be mindful of the non-alpha chars between 'Z' and 'a'.
def alphas():
    for i in range(ord('A'), ord('z')+1):
        if i <= ord('Z') or i >= ord('a'):
            yield chr((i))
'''

# sum_all()
def sum_all(*data):
    '''Assuming floats and ints in data.'''
    sum = 0
    for i in data: sum += i
    return sum

# td_decorator()
def td_decorator(func):
    def wrapper(*args):
        args = ["<td>{}</td>".format(a) for a in args]
        return func(args)
    return wrapper

# get_volume()
def get_volume(a=1,b=1,c=1):
    return a * b * c


if __name__ == '__main__':
    '''The usual test code...'''
    main()
