simple_slug
===========

Script to create slugs of a given string


How to use
==========

'''
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
'''
