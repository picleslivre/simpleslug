simple_slug
===========

Script to create slugs of a given string


How to use
==========

'''
Python 3.4.0 (default, Apr  9 2014, 11:51:10)
[GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> from simpleslug import slugfy

>>> slugfy('São Paulo Futebol Clube')
'sao-paulo-futebol-clube'

>>> slugfy('São  Paulo    Futebol Clube')
'sao-paulo-futebol-clube'

>>> slugfy('São Paulo Futebol Clube', separator='#')
'sao#paulo#futebol#clube'

>>> slugfy('must be empty of crazy chars @çÇ&$%^&*()-_+=¡£¢§¶•–‘“÷≥≤')
'must-be-empty-of-crazy-chars-cc'

>>> slugfy('   without separators in the begining and end of a string   ')
'without-separators-in-the-begining-and-end-of-a-string'
>>>
'''
