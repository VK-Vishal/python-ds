'''
numpy is a package in python it stands for numerical python
supports N-dimenstional arrays objects  that can be used for processing multidenmentioal data
supports large number of mathematical functions to operate on these arrays 
suports different type of data

Numpy Array:is a grid of values  all of same type   and is indexed by a tuple of non -negative inteegers
the numbe of deimension is the rank of the  array
the shape of an array is a tuple of integers giving the size of the array along each dimension 
faster to read and use less bytes of memory
no type checking when iterating thorough objects
===>it uses contigous memeory blocks
  BENEFITS:Speed: NumPy operations are much faster than equivalent Python operations because
                  they are implemented in C and avoid Python loops.
           Memory Efficiency: NumPy uses less memory by storing data in a compact
                             binary format.
           Convenience: A rich set of functions for mathematical and statistical 
                        analysis simplifies complex operations.
    
    
    APPLICATIONS:--mathematics(matlab replacement)
                 --plotting(matplotlib)
                 backend(pandas,connecct 4,digital photography)
                 --machine learning(scikit-learn)
                 --
'''
import numpy as np

arr = np.array([list(range(10)), list(range(10))])
print(arr)
