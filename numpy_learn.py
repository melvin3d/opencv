"""Basics of numpy library.

Name: numpy_leanring.py
Date: 06/18/24
Source: https://numpy.org/doc/stable/user/quickstart.html
"""

from pprint import pprint
import numpy


"""
NumPy`s main object is the homogeneous multidimensional array.
It is a table of elements (usually numbers), all of the same type,
indexed by a tuple of non-negative integers. In NumPy dimensions
are called axes.

[
    [1, 2, 1],
    [1, 3, 4],
]

The array has 2 axis and each has 3 elements, or length of 3.
"""

a = numpy.arange(15).reshape(3, 5)
pprint(a)
pprint(a.shape)
pprint(a.ndim)
pprint(a.dtype.name)
pprint(a.itemsize)
pprint(a.size)
pprint(type(a))

b = numpy.array([3, 4, 5])
pprint(b)
pprint(type(b))
pprint(b.dtype)

c = numpy.array([1.2, 2.43, 3.12])
pprint(c)
pprint(type(c))
pprint(c.dtype)

"""
A frequent error consists in calling array with multiple arguments,
rather than providing a single sequence as an argument.
"""

a1 = numpy.array([(1, 2, 3), (5, 6, 7)])
pprint(a1)

"""
Often, the elements of an array are originally unknown, but its size is known.
Hence, NumPy offers several functions to create arrays with initial placeholder
content. These minimize the necessity of growing arrays, an expensive operation.
"""

b1 = numpy.zeros((3, 4))
pprint(b1)

b2 = numpy.ones((3, 4))
pprint(b2)

b3 = numpy.empty((3, 4), dtype="int16")
pprint(b3)

"""
To create sequences of numbers, NumPy provides the arange function which 
is analogous to the Python built-in range, but returns an array.
"""

a2 = numpy.arange(10, 20, 3)
pprint(a2)

a3 = numpy.arange(0.25, 1.0, 0.1)
pprint(a3)


"""
When arange is used with floating point arguments, it is generally not possible 
to predict the number of elements obtained, due to the finite floating point 
precision. For this reason, it is usually better to use the function linspace 
that receives as an argument the number of elements that we want, 
instead of the step:
"""

a4 = numpy.linspace(1.0, 2.0, 7)
pprint(a4)
pprint(a4.size)
pprint(a4.dtype)
pprint(a4.ndim)
pprint(type(a4))


"""
How ndarrays are printed.
"""

# One dimensional array.
