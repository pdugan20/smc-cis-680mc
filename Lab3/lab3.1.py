#!/usr/local/bin/python3
# Douglas Putnam
# lab4.1.py  Functions
# July 11, 2011

import htmllib
from functions_lab3 import alphas, sum_all, get_volume, td_decorator

htmllib.content_type()
print('<h1><tt>lab3.1.1.py</h1>')


print('<div class="source-container">OUTPUT of alphas():<br>')
for a in alphas():
     print(a,end=' ')
print('</div>')

print('<div class="source-container">OUTPUT of sum_all(1,2,3,4,5,6):<br>')
print(sum_all(1,2,3,4,5,6))
print('</div>')
print('<div class="source-container">OUTPUT of get_volume(99,88,77):<br>')
print(get_volume(99,88,77))
print('</div>')
print('<div class="source-container">OUTPUT of td_decorator():<br>')
print('<table border="1"><tr>')
@td_decorator
def numbers(args):
    for a in args:
        print(a)
numbers(1,2,3,4,5,6,7)
print('</tr></table>')
print('</div>')

htmllib.print_source_code(__file__)
htmllib.print_source_code('functions_lab3.py')
