This File contains list of errata. 

## Chapter 1 - Introduction to Python 
### Section 1.5.1 Data Structures 
#### Page 11 
Lines that start with >>> pertain to the code, the lines without >>> are output. In the code lines, # indicates start of comment

```
>>> a = ['python', 'scipy', 3.6]
>>> a.pop(-1) # will pop the last element in a, which is 3.6
3.6 
>>> print(a) # will print ['python','scipy']
['python','scipy']
>>> a.append('numpy') # 'numpy' will be appended to the end of the list
>>> print(a) # will print ['python','scipy', 'numpy']. Previously we mistakenly had 3.6 instead of 'numpy'
['python','scipy', 'numpy']
>>> print(a[0]) # will print python
python
>>> print(a[-1]) # will print numpy
numpy
>>> print(a[0:2]) # will print ['python', 'scipy']
['python','scipy']
```
